# Factory Method Pattern

## Definition
Factory Method provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

## Diagram
![alt text](pattern.png)

1. Product interface: common to all objects that can be produced by the creator and its subclasses.

2. Concrete Products: different implementations of the product interface.

3. Creator(Factory Method): returns new product objects. It’s important that the return type of this method matches the product interface. 
   
   
   You can declare the factory method as abstract to force all subclasses to implement their own versions of the method. As an alternative, the base factory method can return some default product type.
   
   Note, despite its name, product creation is not the primary responsibility of the creator. Usually, the creator class already has some core business logic related to products. The factory method helps to decouple this logic from the concrete product classes. Here is an analogy: a large software development company can have a training department for programmers. However, the primary function of the company as a whole is still writing code, not producing programmers.

4. Concrete Creators: override the base factory method so it returns a different type of product.
   
   Note that the factory method doesn’t have to create new instances all the time. It can also return existing objects from a cache, an object pool, or another source.

# Example:
- [example.py](conceptual_example.py)

## Other Examples
- example1
  - problem code: [problem.py](problem.py)
    - Adding Database Information violates SRP(single responsibility principle), Add Factory
  - solution: [factory.py](factory.py) 
- example2: [example2.py](example2.py)

## Pseudo Example
- [pseudo code](pseudocode_example)

## Reference
1. https://refactoring.guru/design-patterns/factory-method
2. https://brownbears.tistory.com/491