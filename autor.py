class Autor:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __str__(self):
        return f"{self.nome} ({self.data_nascimento})"
