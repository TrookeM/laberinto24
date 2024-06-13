from Command.Command import Command


class Coger(Command):
    
    def ejecutar(self, obj):
        self.receiver.entrar(obj)

    def esCoger(self):
        return True
    
    def __str__(self):
        return "Coger"
    def equals(self,comando):
        if comando.esCoger():
            return True
        return False