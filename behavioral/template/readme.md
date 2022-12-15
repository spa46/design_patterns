# Template Method Pattern

## Definition
Template Method defines the skeleton of an algorithm in the superclass but 
lets subclasses override specific steps of the algorithm without changing its structure.


## Diagram
![template](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/spa46/design_patterns/master/behavioral/template/class_diagram.uml)


## source file
- problematic code:
  - [redundant_code.java](redundant_code.java)
  - 
- apply template pattern:
  - [use_template.java](use_template.java) (java ver.)
  - [use_template.py](use_template.py) (python ver.)
  - 
- best code:
  - [template and interface+abstract](template_with_interface_and_abstract.java) (java ver.)
  - [multiple_inheritance.py](multiple inheritance.py) (python ver.)


## reference
1. https://refactoring.guru/design-patterns/state
2. https://brownbears.tistory.com/571 (in Korean)
