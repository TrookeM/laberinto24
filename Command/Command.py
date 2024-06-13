from abc import ABC, abstractmethod
class Command(ABC):
    
    def __init__(self):
        self.receiver = None
        
    @abstractmethod
    def ejecutar(self, ente):
        pass

    def esAbrir(self):
        return False
    
    def esSoltar(self):
        return False
    
    def esCerrar(self):
        return False
    
    def esEntrar(self):
        return False
    
    def esCoger(self):
        return False
    
    def esUsar(self):
        return False
    
    @abstractmethod
    def equals(self,command):
        pass
    