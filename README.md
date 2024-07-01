# Proyecto del laberinto del curso 23-24

The code of this repository has been developed with the assistance of SourceGraph Cody

**Ajustes del entorno**
```ruby
En mi caso he tenido quer poner la ruta en el archivo config del repositoro de esta manera ya que me dejaron de ir los import
{
    "python.envFile": "${workspaceFolder}/.env",
    "terminal.integrated.env.windows": {
      "PYTHONPATH": "C:/Users/yorch/Desktop/laberinto24"
    }
  }
```


**Modificaciones**
```ruby
---Nuevos comandos---
He implementado el comando coger, que sirve para que el personaje pueda coger los objetos del entorno y
almacenarlos en su mochila la cual también ha sido implementada como artefacto;
El comando soltar, que sirve para soltar los objetos del inventario; Usar, que sirve para usar estos objetos
(Una poción o un pan, los cuales ha sido implementada como artefactos y curan al personaje 50 de vida y 20 respectivamente);
Apagar, que sirve para que el personaje pueda apagar un fuego y así evitar recibir daño.

Decorador: Fuego

Forma: Triangle

Modo: Curativo

Cuerpo

Artefactos:
  Mochila
  Pan
  Pocion
  BatePinchos
```
