import genanki
import random


class Algorithm():
    def __init__(self):
        self.id_model = random.randrange(1 << 30, 1 << 31)
        self.id_deck = random.randrange(1 << 30,1 << 31)
        # print(self.id_model)
        # print(self.id_deck)

    def create_model(self, name_model: str = 'IKBFU HSLS English lessons'):
        my_note_model = genanki.Model(
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
        my_note = genanki.Note(
            model=self.my_note_model,
            fields=values,
            )
        return my_note

    def create_deck(self, name_deck: str = 'My Deck'):
        my_deck = genanki.Deck(
            self.id_deck, # a unique ID for the deck
            name_deck, # the name of the deck
        )
        self.my_deck = my_deck

    def add_note(self, my_note):
        self.my_deck.add_note(my_note)

    def folding(self):
        genanki.Package(self.my_deck).write_to_file('output.apkg')


if __name__ == "__main__":
    al = Algorithm()
    al.create_model()
    al.create_deck()

    my_note = al.create_note(['English', 'Transcription', 'Russian', 'Sound', 'Image'])
    al.add_note(my_note)
    my_note = al.create_note(['Hello', '`hello', 'Привет', 'Sound', 'Image'])
    al.add_note(my_note)

    al.folding()