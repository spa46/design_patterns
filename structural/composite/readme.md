# Composite Pattern

## Definition
partitioning design pattern. 
It describes a group of objects that is treated the same way as a single instance of the same type of object. 
The intent of a composite is to “compose” objects into tree structures to represent part-whole hierarchies. 
It allows you to have a tree structure and ask each node in the tree structure to perform a task.

## Diagram
![alt text](concept/structure.png)

1. Component interface: operations that are common to both simple and complex elements of the tree.

2. Leaf: a basic element of a tree that doesn’t have sub-elements.
   
   Usually, leaf components end up doing most of the real work, since they don’t have anyone to delegate the work to.
   
3. The Container (aka composite) is an element that has sub-elements: leaves or other containers. A container doesn’t know the concrete classes of its children. It works with all sub-elements only via the component interface.
   
   Upon receiving a request, a container delegates the work to its sub-elements, processes intermediate results and then returns the final result to the client.

4. The Client works with all elements through the component interface. As a result, the client can work in the same way with both simple or complex elements of the tree.

- - [Click Code](concept/example.py)

## Pseudo Example
- [example](pseudocode)

## Other Examples
- [composite.py](other_examples/composite.py) (python)
- [composite.java](other_examples/composite.java) (java)

## Reference
1. https://www.geeksforgeeks.org/composite-design-pattern/
2. https://brownbears.tistory.com/499 (examples in Korean)
