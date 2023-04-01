from __future__ import annotations
from typing import Optional, Union
from python_ta.contracts import check_contracts


@check_contracts
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


@check_contracts
class Restaurant(Node):
    """A child class of Node, representing a restaurant

    Instance Attributes:
    - name:
        The name of this restaurant
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


@check_contracts
class Person(Node):
    """ A child class of Node, representing one user

    Instance Attributes:
    - price_range:
        An integer from 1 to 4 representing the price range preference of the person
    # TODO : should we make a instance attribute for every preference of the person (and make it T/F) or just have a list?
             I feel like the list might be kind of hard to evaluate later on - jw
    """
    price_range: int
    preferences: list

    def __init__(self, identifier: int, coordinates: tuple[float, float],
                 price_range: int, current_restaurant_type: str, preferences: list) -> None:
        super().__init__(identifier, coordinates)

        self.price_range = price_range
        self.current_restaurant_type = current_restaurant_type
        self.preferences = preferences.copy()

    def update_preferences(self, new_preferences: list) -> None:
        """Update the person's preferences"""
        self.preferences = new_preferences.copy()


class Network:
    """A class that represents the network.

    Instance Attributes:
    - _nodes: The collection of the existing nodes in the network, where the key is the id of the node
              and the value is the corresponding node

    Representation Invariants:
    - ...
    """

    _nodes: dict[int, Node]

    def __init__(self):
        self._nodes = {}

    def add_restaurant(self, id: int, coordinates: tuple[float, float],
                       name: str, cuisine: str, price: int, r_type: str, address: str) -> None:
        """Add node to the network
        Raise ValueError if the given id is not unique"""

        if id in self._nodes:
            raise ValueError('Given id exists in the network')

        new_restaurant: Restaurant = Restaurant(
            id, coordinates, name, cuisine, price, r_type, address)

    def add_edge(self, node1: Union[Restaurant, Person], node2: Union[Restaurant, Person]) -> None:
        """"""

    def get_distance(self, cuurent_location: Node, destination: Node) -> float:
        """Returns the distance between self and a target location"""
        # googlemaps api probabaly need to figure how to do that
        ...
