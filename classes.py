from __future__ import annotations
from typing import Optional
from python_ta.contracts import check_contracts


class Node:
    """An abstract class that represents a location.

    Instance Attributes
    - identifier:
        The id is an integer value that uniquely identifies each node
    - coordinates:
        A tuple representing longitutde and latitude of the node
    - neighbors:
        A mapping containing the neighbor nodes where the key is the unique neighbor id and
        the value is the corresponding neighbor node.
    """
    identifier: int
    coordinates: tuple[float, float]
    neighbors: dict[int, Node]

    def __init__(self, identifier: int, coordinates: tuple[float, float]) -> None:
        """Initialize this node with the unique identifier and coordinate location"""
        self.identifier = identifier
        self.coordinates = coordinates
        self.neighbors = {}

    def __repr__(self) -> str:
        """Return a string representing this node."""
        return f'Node({self.identifier})'

    def get_distance(self, target_location: Node) -> float:
        """Returns the distance between self and a target location"""
        # googlemaps api probabaly need to figure how to do that
        ...


class Restaurant(Node):
    """A child class of Node, representing a restaurant

    Instance Attributes:
    - name:
        The name of this restaurant
    - cuisine:
        The type of cuisine this restaurant offers
    - price:
        An integer from 1 to 4 representing the price range of this restaurant.
    - type:
        The type of restaurant this is.
    - address:
        The street address of this restaurant

    Representation Invariants:
    - self.type in ("Drinks", "Cafe", "Dessert", "Fast Food", "Dinner")
    - ...
    """
    name: str
    cuisine: str
    price: int
    r_type: str  # r short for restaurant
    address: str

    def __init__(self, identifier: int, coordinates: tuple[float, float],
                 name: str, cuisine: str, price: int, r_type: str, address: str):
        super().__init__(identifier, coordinates)
        self.name = name
        self.cuisine = cuisine
        self.price = price
        self.r_type = r_type
        self.address = address


class Person(Node):
    """ A child class of Node, representing one user

    Instance Attributes:
    - price_range:
        An integer from 1 to 4 representing the price range preference of the person
    - current_restaurant_type:
        The current type of restaurant this person is in
    # TODO : should we make a instance attribute for every preference of the person (and make it T/F) or just have a list?
             I feel like the list might be kind of hard to evaluate later on - jw
    """
    price_range: int
    current_restaurant_type: str

    def __init__(self, identifier: int, coordinates: tuple[float, float],
                 price_range: int, current_restaurant_type: str):
        super().__init__(identifier, coordinates)

        self.price_range = price_range
        self.current_restaurant_type = current_restaurant_type


class Network:
    pass
