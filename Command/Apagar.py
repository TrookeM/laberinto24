from Command.Command import Command

class Apagar(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def ejecutar(self, obj):
        print(f"Apagando el fuego de {self.receiver}")
        # Aquí puedes agregar la lógica para apagar el fuego

    def esApagar(self):
        return True

    def __str__(self):
        return "Apagar"

    def equals(self, comando):
        if comando.esApagar():
            return True
        return False
