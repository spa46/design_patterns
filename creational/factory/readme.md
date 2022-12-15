# Factory Method Pattern

## Definition
Factory Method provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

## Diagram
![factory method](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/spa46/design_patterns/master/creational/factory/class_diagram.uml)

## Example source file
- problem code: [problem.py](problem.py)
  - Adding Database Information violates SRP(single responsibility principle), Add Factory
- [factory.py](factory.py) 

## reference
1. https://refactoring.guru/design-patterns/command
2. https://brownbears.tistory.com/491
