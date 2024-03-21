# Proyecto del laberinto del curso 23-24

The code (maze.py) in this repository has been developed with the assistance of SourceGraph Cody

**Initial prompt:**
```ruby
Escriba un programa en Python con los siguientes objetos: Laberinto, Pared, Puerta y Habitación.
El objeto Laberinto tiene una colección de objetos Sala.
El objeto Habitación tiene cuatro lados (norte, este, oeste, sur), inicialmente cada lado es un objeto Pared.
El objeto Puerta tiene dos lados que podrían ser objetos Habitación.
El objeto Maze tiene una operación addRoom con un objeto Room como parámetro.
```

**Decorator prompt:**
```ruby
Incluye una nueva clase llamada Decorador. Esta nueva clase es una subclase de MapElement
```

**Composite prompt:**
```ruby
Aplique el patrón de diseño compuesto a esta solución: MapElement es la clase Componente,
Container es una subclase de MapElement y Room es una subclase de la clase Container.
Una nueva clase Leaf es una subclase de MapElement.
La clase Decorator ahora es una subclase de Leaf
```

**Prompt para crear un laberinto de 4 habitaciones y 4 bichos**
```ruby
Duplica createMaze2RoomFM en el juego. Cambie el nombre del método duplicado para crear4Room2BeastFM,
lo que creará 4 habitaciones (Room). La habitación 1 se conecta con la habitación 2 por una puerta en el sur de la habitación 1.
La habitación 1 se conecta con la habitación 3 al este de la habitación 1.
La habitación 3 se conecta con la habitación 4 por el sur de la habitación 3. La habitación 2 se conecta con la habitación 4 por el este de la habitación 3.
También incluye 4 instancias de bestia (clase Bestia), dos en modo agresivo y dos en modo perezoso.
La bestia agresiva estará en las habitaciones 1 y 3. Las bestias perezosas estarán en las habitaciones 2 y 4.
```

**Prompt to correct the result:**
```ruby
Usa los métodos existentes en el juego para crear bestias agresivas y perezosas.
```
