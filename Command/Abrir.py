from Command.Command import Command


class Abrir(Command):
    
    def ejecutar(self, obj):
        self.receiver.abrir(obj)
    
    def esAbrir(self):
        return True
    
    def __str__(self):
        return "Abrir"
    def equals(self,comando):
        if comando.esAbrir():
            return True
        return False