
from datetime import datetime


class Note:
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'



    def __init__(self, code: int, tiltle: str, text: str, importance: str) :
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



class Notebook:
    def __init__(self):
        self.list = []

    def add_Note(self, title: str, text: str, importance: str) -> int:
        def generar_nuevo_codigo(notas):
            codigos_existentes = {nota['codigo'] for nota in notas}
            nuevo_codigo = len(notas) + 1

            # Asegurarse de que el código no esté repetido
            while nuevo_codigo in codigos_existentes:
                nuevo_codigo += 1

            return nuevo_codigo






