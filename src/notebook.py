# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime


class Note:
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'



    def __init__(self, code: str, tiltle: str, text: str, importance: str) :
        self.code = code
        self.tiltle = tiltle
        self.text = text
        self.importance = importance
        self.creation_date = datetime.now()
        self.tags = []

    def add_tag(self, tag: str):
         if tag not in self.tags:
            self.tags.append(tag)
    def __str__(self):
        return f"date: {self.creation_date}, tiltle: {self.tiltle}, text: {self.text}"

