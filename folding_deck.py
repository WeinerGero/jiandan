from genanki import Model, Note, Deck, Package
from random import randrange


class Anki():
    def __init__(self):
        self.id_model = randrange(1 << 30, 1 << 31)
        self.id_deck = randrange(1 << 30,1 << 31)
        # print(self.id_model)
        # print(self.id_deck)

    def create_model(self, name_model: str = 'IKBFU HSLS English lessons'):
        my_note_model = Model(
            self.id_model, # a unique ID for the model
            name_model, # the name of the model
            fields=[
                {'name': 'English'},
                {'name': 'Transcription'},
                {'name': 'Russian'},
                {'name': 'Sound'},
                {'name': 'Image'}
            ],
            templates=[
                {
                    'name': 'Eng|Tra+Rus',
                    'qfmt': '{{English}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{Transcription}}'
                            '<div style=\'font-family: "Arial"; font-size: 20px;\'>{{Russian}}</div>',
                },
                {
                    'name': 'Rus|Eng+Tra',
                    'qfmt': '{{Russian}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{English}}'
                            '<div style=\'font-family: "Arial"; font-size: 20px;\'>{{Transcription}}</div>',
                },
            ],
            css='.card {font-family: arial;font-size: 20px;text-align: center;color: black;background-color: white;'
        )
        self.my_note_model = my_note_model

    def create_note(self, values: list):
        my_note = Note(
            model=self.my_note_model,
            fields=values,
            )
        return my_note

    def create_deck(self, name_deck: str = 'My Deck'):
        my_deck = Deck(
            self.id_deck, # a unique ID for the deck
            name_deck, # the name of the deck
        )
        self.my_deck = my_deck

    def add_note(self, my_note):
        self.my_deck.add_note(my_note)

    def folding(self, output_path: str = '', name_deck: str = 'My Deck'):
        Package(self.my_deck).write_to_file(f'{output_path}/{name_deck}.apkg')


if __name__ == "__main__":
    an = Anki()
    an.create_model()
    an.create_deck()

    my_note = an.create_note(['English', 'Transcription', 'Russian', 'Sound', 'Image'])
    an.add_note(my_note)
    my_note = an.create_note(['Hello', '`hello', 'Привет', 'Sound', 'Image'])
    an.add_note(my_note)

    an.folding()