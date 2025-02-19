# foundational_design_principles
Notes of Python code of foundational design principles.

Four design principles are described:

1. Encapsulate what varies.
    This principle means aislate the parts of yout code with more probability to change and encapsulate. The techniques are to follow this principle are:
    1. [Polymorphism](https://github.com/MemoOlv/foundational_design_principles/blob/develop/src/polymorphism.py)
    1. [Getters](https://github.com/MemoOlv/foundational_design_principles/blob/develop/src/polymorphism.py#L25) and [setters](https://github.com/MemoOlv/foundational_design_principles/blob/develop/src/polymorphism.py#L29)

1. Favor Composition Over Inheritance.
    This principle talks abput prefer composition of simple parts over inherit functionalities of a base class. _To create complex objects combine simple objects_. The technique to follow this principle is:
    1. [Composition](https://github.com/MemoOlv/foundational_design_principles/blob/develop/src/composition.py)

1. Program to Interfaces, not Implementations.
    This pincniple talks abour how specify implementation makes the coupling stronger. This makes the code hard to modify. This principle talks about create interfaces (contracts) for the classes to follow. The thechniques to apply this principle are:
    1. [Abstract Base Clases (ABC's)](https://github.com/MemoOlv/foundational_design_principles/blob/develop/src/interfaces.py)
    1. [Protocols](https://github.com/MemoOlv/foundational_design_principles/blob/develop/src/protocols.py)

1. Loose Coupling principle.
    This principle states that create loose coupling between elements of the systems, allows to grow in complexity. In a loose coupling system the components are independent and interact in a well defined interfaces. The techniques to follow this principle are:
    1. [Dependency injection](https://github.com/MemoOlv/foundational_design_principles/blob/develop/src/dependency_injection.py)
    1. Observer pattern



## References

This notes are based in:

- Book [Mastering Python Design Patterns](https://learning.oreilly.com/library/view/mastering-python-design/9781837639618/B21896_01.xhtml). ISBN 978-1-83763-961-8
