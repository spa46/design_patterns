# Facade Pattern

## Definition
Facade pattern hides the complexities of the system and provides an interface to the client using which the client can access the system. This type of design pattern comes under structural pattern as this pattern adds an interface to existing system to hide its complexities.
This pattern involves a single class which provides simplified methods required by client and delegates calls to methods of existing system classes.

## Diagram
![alt text](concept/structure.png)

1. The Facade provides convenient access to a particular part of the subsystem’s functionality. It knows where to direct the client’s request and how to operate all the moving parts.

2. An Additional Facade class can be created to prevent polluting a single facade with unrelated features that might make it yet another complex structure. Additional facades can be used by both clients and other facades.

3. The Complex Subsystem consists of dozens of various objects. To make them all do something meaningful, you have to dive deep into the subsystem’s implementation details, such as initializing objects in the correct order and supplying them with data in the proper format.
   
   Subsystem classes aren’t aware of the facade’s existence. They operate within the system and work with each other directly.

4. The Client uses the facade instead of calling the subsystem objects directly.

- - [Click Code](concept/example.py)

## Pseudo Example
- [example](pseudocode)

## Other Examples
- [facade.py](facade.py)

## reference
1. https://www.tutorialspoint.com/design_pattern/facade_pattern.htm
2. https://www.geeksforgeeks.org/facade-method-python-design-patterns/
