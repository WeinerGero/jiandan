"""
Для связки всех модулей
"""
from read_pdf import Reader
from folding_deck import Anki

def input_path(input_path):
    # pdf_path = input("Укажите путь до PDF файла: ")
    # pdf_path = "006_Relationships.pdf"
    pdf_path = input_path
    print(pdf_path)
    return pdf_path

def main(input_path, output_path, name_output_file):
    # Reader part
    reader = Reader(input_path)
    try:
        reader.read_file('pdf')
    except FileNotFoundError:
        return 0
    except:
        return 1
    json_data = reader.read_file('json')
    json_data = reader.clean_json(json_data)
    reader.upload_file(json_data, type_file='json')
    data = reader.convert_json_to_list_values(json_data)

    # Algorithm part
    an = Anki()
    an.create_model()
    an.create_deck(name_output_file)
    for row in data:
        my_note = an.create_note(row)
        an.add_note(my_note)
    try:
        an.folding(output_path, name_output_file)
    except FileNotFoundError:
        return 2

    print("End!")


if __name__ == "__main__":
    input_path = "006_Relationships.pdf"
    output_path, name_output_file = '', ''
    main(input_path, output_path, name_output_file)