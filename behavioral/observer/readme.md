# Observer Pattern

## Definition
 Observer lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.

## Diagram
![observer](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/spa46/design_patterns/master/behavioral/observer/class_diagram.uml)

## source file
- problem
  - tight_coupling([source](tight_coupling.java)): changes affect other classes 
  - loose_coupling([source](loose_coupling.java)): it solves above problem but another problem rises: cannot send multiple notifications.
  - use observer pattern
- push:
  - [push.py](push.py) (python ver.)
  - [push.java](push.java) (java ver.)
- pull:
  - [pull.py](pull.py) (python ver.)
  - [pull.java](pull.java) (java ver.)

## reference
1. https://refactoring.guru/design-patterns/observer
2. https://brownbears.tistory.com/555 (in Korean)
