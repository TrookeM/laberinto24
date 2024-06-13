from Command.Command import Command

class Soltar(Command):
    
    def ejecutar(self, obj):
        self.receiver.soltar(obj)

    def esSoltar(self):
        return True
    
    def equals(self, comandin):
        if comandin.esSoltar():
            return True
        return False
    
    def __str__(self):
        return "Suelta el " + str(self.receiver)
    def equals(self,comando):
        if comando.esSoltar():
            return True
        return False
