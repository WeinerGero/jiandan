"""
Для связки всех модулей
"""
from read_pdf import Reader
from folding_deck import Algorithm
from GUI import window

def input_path(res):
    # pdf_path = input("Укажите путь до PDF файла: ")
    # pdf_path = "006_Relationships.pdf"
    pdf_path = res
    print(pdf_path)
    return pdf_path

def main(res):
    # Reader part
    pdf_path = input_path(res)
    reader = Reader(pdf_path)
    reader.read_file('pdf')
    json_data = reader.read_file('json')
    json_data = reader.clean_json(json_data)
    reader.upload_file(json_data, type_file='json')
    data = reader.convert_json_to_list_values(json_data)

    # Algorithm part
    al = Algorithm()
    al.create_model()
    al.create_deck()
    for row in data:
        my_note = al.create_note(row)
        al.add_note(my_note)
    al.folding()

    print("End!")


if __name__ == "__main__":
    main()