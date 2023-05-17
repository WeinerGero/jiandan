"""
python 3.11.2, sys 3.11.2, PyPDF2 3.0.1, py-anki 0.0.6, tabula 2.7.0, json
"""
from json import dump, load
from tabula import read_pdf


class Reader():
    def __init__(self, pdf_path: str, count_columns: int = 3, mode:str = 'eng,tra,rus'):
        self.pdf_path = pdf_path
        # self.pdf_path = "006_Relationships.pdf"
        self.json_temp_path = 'temporary.json'
        self.count_columns = count_columns
        self.mode = mode

    def read_file(self, type_file):
        if type_file == "pdf":
            read_pdf(self.pdf_path, pages='all', output_path=self.json_temp_path, output_format='json', encoding='utf-8', stream=True)
            # read_pdf returns list of json object into file
        elif type_file == "json":
            with open(self.json_temp_path, 'r', encoding='utf-8') as json_file:
                json_data = load(json_file)
            return json_data
        else:
            print("Неизвестный тип файла")

    def clean_json(self, json_data: list) -> list:
        del_page = []
        for num_page in range(len(json_data)):
            page = json_data[num_page]['data']
            del_list = []

            for row in range(len(page)):
                if len(page[row]) != self.count_columns:
                    del_list.append(row)
                    continue

                for i in range(self.count_columns):
                    if page[row][i]['text'] == '':
                        for k in range(self.count_columns):
                            page[row - 1][k]['text'] = page[row - 1][k]['text'] + ' ' + page[row][k]['text']
                        del_list.append(row)
                        break

            json_data[num_page]['data'] = [page[row] for row in range(len(page)) if row not in del_list]

            if len(json_data[num_page]['data']) == 0:
                del_page.append(num_page)

        json_data = [json_data[num_page] for num_page in range(len(json_data)) if num_page not in del_page]
        return json_data

    def convert_json_to_list_values(self, json_data):
        default_values = ['Sound', 'Image']
        converted_data = []
        for num_page in range(len(json_data)):
            page = json_data[num_page]['data']
            for row in range(len(page)):
                if self.mode == 'eng,tra,rus':
                    english_text = page[row][0]['text']
                    transcription_text = page[row][1]['text']
                    russian_text = page[row][2]['text']

                converted_data.append([english_text, transcription_text, russian_text] + default_values)
        return converted_data

    def convert_jsondata_to_txtdata(self, json_data: list):
        tab = '\t'
        separator = '#separator:tab\n'
        html = '#html:true\n'
        notetype_column = '#notetype column:1\n'
        deck_column = '#deck column:2\n'
        record_type = 'IKBFU HSLS English lessons'
        name_deck = input("Укажите название колоды: ")
        txt_data = separator + html + notetype_column + deck_column

        for num_page in range(len(json_data)):
            page = json_data[num_page]['data']
            for row in range(len(page)):
                if self.mode == 'eng,tra-rus':
                    english_text = page[row][0]['text']
                    transcription_text = page[row][1]['text']
                    russian_text = page[row][2]['text']

                txt_data = txt_data + record_type + tab + name_deck + tab + english_text + ', ' +transcription_text + tab + russian_text + '\n'
        return txt_data

    def convert_jsoondata_to_csvdata(self, json_data: list):
        separator = ','
        csv_data = ''

        for num_page in range(len(json_data)):
            page = json_data[num_page]['data']
            for row in range(len(page)):
                if self.mode == 'eng,tra,rus':
                    english_text = page[row][0]['text']
                    transcription_text = page[row][1]['text']
                    russian_text = page[row][2]['text']

                    csv_data = csv_data + english_text + separator + transcription_text + separator + russian_text + '\n'
        return csv_data

    def upload_file(self, data: list or str, type_file: str = 'txt', file_path: str = 'temporary'):
        if type_file == 'json':
            with open(f'{file_path}.json', 'w', encoding='utf-8') as file:
                dump(data, file, ensure_ascii=False, indent=4)
        elif type_file == 'txt':
            with open(f'{file_path}.txt', 'w', encoding='utf-8') as file:
                file.write(data)
        elif type_file == 'csv':
            with open(f'{file_path}.csv', 'w', encoding='utf-8') as file:
                file.write(data)


if __name__ == "__main__":
    pdf_path = '006_Relationships.pdf'
    read_file('pdf', pdf_path)
    json_data = read_file('json')
    json_data = clean_json(json_data)
    upload_file(json_data, type_file='json')
    csv_data = convert_jsoondata_to_csvdata(json_data)
    upload_file(csv_data, type_file='csv')


