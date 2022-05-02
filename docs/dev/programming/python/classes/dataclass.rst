Data Class
==========

The material of this topic is from `stack overflow <https://stackoverflow.com/questions/47955263/what-are-data-classes-and-how-are-they-different-from-common-classes>`_ .

Data classes are just regular classes that are geared towards storing state,
rather than containing a lot of logic. Every time you create a class that
mostly consists of attributes, you make a data class.

What the ``dataclasses`` module does is to make it **easier** to create data
classes. It takes care of a lot of boilerplate for you.

This is especially useful when your data class must be hashable; because
this requires a ``__hash__`` method as well as an ``__eq__`` method. If you
add a custom ``__repr__`` method for ease of debugging, that can become
quite verbose:

.. code-block:: python
    :linenos:

    class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def __init__(
            self, 
            name: str, 
            unit_price: float,
            quantity_on_hand: int = 0
        ) -> None:
        self.name = name
        self.unit_price = unit_price
        self.quantity_on_hand = quantity_on_hand

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
    
    def __repr__(self) -> str:
        return (
            'InventoryItem('
            f'name={self.name!r}, unit_price={self.unit_price!r}, '
            f'quantity_on_hand={self.quantity_on_hand!r})'

    def __hash__(self) -> int:
        return hash((self.name, self.unit_price, self.quantity_on_hand))

    def __eq__(self, other) -> bool:
        if not isinstance(other, InventoryItem):
            return NotImplemented
        return (
            (self.name, self.unit_price, self.quantity_on_hand) == 
            (other.name, other.unit_price, other.quantity_on_hand))

With dataclasses you can reduce it to:

.. code-block:: python
    :linenos:

    from dataclasses import dataclass
    
    @dataclass(unsafe_hash=True)
    class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

The same class decorator can also generate comparison methods (``__lt__``,
``__gt__``, etc.) and handle immutability.

``namedtuple`` classes are also data classes, but are immutable by default
(as well as being sequences). dataclasses are much more flexible in this
regard, and can easily be structured such that they can fill the same role
as a ``namedtuple`` class.

The `PEP` was inspired by the `attrs` project, which can do even more (including
slots, validators, converters, metadata, etc.).

If you want to use dataclasses module in Python versions < 3.7, then you
could install the ``backported`` module (requires 3.6) or use the `attrs`
project mentioned above.
