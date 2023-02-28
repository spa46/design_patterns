# Abstract Factory Pattern

## Definition
Abstract Factory lets you produce families of related objects without specifying their concrete classes.

## Diagram
![alt text](concept/structure.png)

1. Abstract Products declare interfaces for a set of distinct but related products which make up a product family.

2. Concrete Products are various implementations of abstract products, grouped by variants. Each abstract product (chair/sofa) must be implemented in all given variants (Victorian/Modern).

3. The Abstract Factory interface declares a set of methods for creating each of the abstract products.

4. Concrete Factories implement creation methods of the abstract factory. Each concrete factory corresponds to a specific variant of products and creates only those product variants.

5. Although concrete factories instantiate concrete products, signatures of their creation methods must return corresponding abstract products. This way the client code that uses a factory doesn’t get coupled to the specific variant of the product it gets from a factory. The Client can work with any concrete factory/product variant, as long as it communicates with their objects via abstract interfaces.

- - [Click Code](concept/example.py)

## Pseudo Example
- [example](pseudocode)

## Other Examples
- [without_abstract_factory.py](other_examples/without_abstract_factory.py)
- [abstract_factory.py](other_examples/abstract_factory.py) 

## reference
1. https://refactoring.guru/design-patterns/abstract-factory
2. https://www.geeksforgeeks.org/abstract-factory-method-python-design-patterns/
