"""
python 3.11.2, sys 3.11.2, PyPDF2 3.0.1, py-anki 0.0.6, tabula 2.7.0, json
"""

import sys
from py_anki import AnkiApi
import tabula
import json


def input_path():
    pdf_path = input("Укажите путь до PDF файла: ")
    pdf_path = "006_Relationships.pdf"
    return pdf_path


def read_pdf(pdf_path: str):
    tabula.read_pdf(pdf_path, pages='all', output_path='temporary.json', output_format='json', encoding='utf-8', stream=True)
    # read_pdf returns list of json object into file


def read_json(json_path: str = 'temporary.json'):
    with open(json_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    return json_data


def clean_json(json_data: list, count_columns: int = 3):
    del_page = []
    for num_page in range(len(json_data)):
        page = json_data[num_page]['data']
        del_list = []

        for row in range(len(page)):
            if len(page[row]) != count_columns:
                del_list.append(row)
                continue

            for i in range(count_columns):
                if page[row][i]['text'] == '':
                    for k in range(count_columns):
                        page[row - 1][k]['text'] = page[row - 1][k]['text'] + ' ' + page[row][k]['text']
                    del_list.append(row)
                    break

        json_data[num_page]['data'] = [page[row] for row in range(len(page)) if row not in del_list]

        if len(json_data[num_page]['data']) == 0:
            del_page.append(num_page)

    json_data = [json_data[num_page] for num_page in range(len(json_data)) if num_page not in del_page]
    return json_data


def upload_file(data: list or str, type_file: str = 'txt', file_path: str = 'temporary'):
    if type_file == 'json':
        with open(f'{file_path}.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    elif type_file == 'txt':
        with open(f'{file_path}.txt', 'w', encoding='utf-8') as file:
            file.write(data)


def convert_jsondata_to_txtdata(json_data: list, mode: str = 'eng,tra-rus'):
    tab = '\t'
    separator = '#separator:tab\n'
    html = '#html:true\n'
    notetype_column = '#notetype column:1\n'
    deck_column = '#deck column:2\n'
    record_type = 'Basic'
    name_deck = input("Укажите название колоды: ")
    txt_data = separator + html + notetype_column + deck_column

    for num_page in range(len(json_data)):
        page = json_data[num_page]['data']
        for row in range(len(page)):
            if mode == 'eng,tra-rus':
                english_text = page[row][0]['text']
                transcription_text = page[row][1]['text']
                russian_text = page[row][2]['text']

            txt_data = txt_data + record_type + tab + name_deck + tab + english_text + ', ' +transcription_text + tab + russian_text + '\n'
    return txt_data


if __name__ == "__main__":
    pdf_path = input_path()
    read_pdf(pdf_path)
    json_data = read_json()
    json_data = clean_json(json_data)
    upload_file(json_data, type_file='json')
    txt_data = convert_jsondata_to_txtdata(json_data)
    upload_file(txt_data)
