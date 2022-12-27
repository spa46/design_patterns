# Adapter Pattern

## Definition
The adapter pattern convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn’t otherwise because of incompatible interfaces.

## Diagram
![alt text](concept/structure.png)

1. Client:contains the existing business logic of the program.

2. Client Interface: a protocol that other classes must follow to be able to collaborate with the client code.

3. Service (usually 3rd-party or legacy): The client can’t use this class directly because it has an incompatible interface.

4. Adapter: able to work with both the client and the service: it implements the client interface, while wrapping the service object. The adapter receives calls from the client via the adapter interface and translates them into calls to the wrapped service object in a format it can understand.

5. The client code doesn’t get coupled to the concrete adapter class as long as it works with the adapter via the client interface. Thanks to this, you can introduce new types of adapters into the program without breaking the existing client code. This can be useful when the interface of the service class gets changed or replaced: you can just create a new adapter class without changing the client code.

- - [Click Code](concept/example.py)

## Pseudo Example
- [example](pseudocode)

## Other Examples
- adapter.py