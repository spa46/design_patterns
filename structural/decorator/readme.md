# Decorator Pattern

## Definition
It attaches a flexible additional responsibilities to an object dynamically. 
In other words, this uses composition instead of inheritance to extend the functionality of an object at runtime.

## Diagram
![alt text](concept/structure.png)

1. The Component declares the common interface for both wrappers and wrapped objects.

2. Concrete Component is a class of objects being wrapped. It defines the basic behavior, which can be altered by decorators.

3. The Base Decorator class has a field for referencing a wrapped object. The field’s type should be declared as the component interface so it can contain both concrete components and decorators. The base decorator delegates all operations to the wrapped object.

4. Concrete Decorators define extra behaviors that can be added to components dynamically. Concrete decorators override methods of the base decorator and execute their behavior either before or after calling the parent method.

5. The Client can wrap components in multiple layers of decorators, as long as it works with all objects via the component interface.

- - [Click Code](concept/example.png)

## Pseudo Example
- [example](pseudocode)

## Other Examples
- [problematic code](other_examples/problem.java) (java)
  - What if putting options are required when ordering a cup of coffee?
- [decorator.py](other_examples/decorator.py) (python)
- [decorator.java](other_examples/decorator.java) (java)

## Reference
1. https://refactoring.guru/design-patterns/decorator
2. https://brownbears.tistory.com/557 (examples, Korean)
