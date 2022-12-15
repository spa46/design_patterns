# Factory Method Pattern

## Definition
Factory Method provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

## Diagram
![factory method](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/spa46/design_patterns/master/creational/factory/class_diagram.uml)

## Example source file
- example1
  - problem code: [problem.py](problem.py)
    - Adding Database Information violates SRP(single responsibility principle), Add Factory
  - solution: [factory.py](factory.py) 
- example2: [example2.py](example2.py)

## reference
1. https://refactoring.guru/design-patterns/factory-method
2. https://brownbears.tistory.com/491
