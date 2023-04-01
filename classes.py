from __future__ import annotations
from typing import Union
from python_ta.contracts import check_contracts


@check_contracts
class _Node:
    """An abstract class that represents a location.

    Instance Attributes
    - identifier:
        The id is an integer value that uniquely identifies each node
    - coordinates:
        For the restaurant: A tuple representing longitutde and latitude of the restaurant's address
        For the person: A person's
    - neighbors:
        A mapping containing the neighbor nodes where the key is the unique neighbor id and
        the value is the corresponding neighbor node.
    """
    identifier: int
    coordinates: tuple[float, float]
    neighbors: dict[int, _Node]

    def __init__(self, identifier: int, coordinates: tuple[float, float]) -> None:
        """Initialize this node with the unique identifier and coordinate location"""
        self.identifier = identifier
        self.coordinates = coordinates
        self.neighbors = {}

    def __repr__(self) -> str:
        """Return a string representing this node."""
        return f'Node({self.identifier})'


@check_contracts
class Restaurant(_Node):
    """A child class of Node, representing a restaurant

    Instance Attributes:
    - name: The name of this restaurant
    - price: An integer from 1 to 4 representing the price range of this restaurant.
    - type: The type of restaurant this is.
    - address: The street address of this restaurant

    Representation Invariants:
    - self.type in ("Drinks", "Cafe", "Dessert", "Fast Food", "Dinner")
    - ...
    """
    name: str
    price: int
    r_type: str  # r short for restaurant
    address: str

    def __init__(self, identifier: int, coordinates: tuple[float, float],
                 name: str, price: int, restaurant_type: str, address: str):
        super().__init__(identifier, coordinates)

        self.name = name
        self.price = price
        self.r_type = restaurant_type
        self.address = address

    def __str__(self):
        return f"Restaurant: {self.name}, price: {'$' * self.price}, type: {self.r_type}, address: {self.address}"


@check_contracts
class Person(_Node):
    """ A child class of Node, representing one user

    Instance Attributes:
        - max_price_range: A person's maximum price range willing to take
        - preferences: ... # TODO
    """

    route_plan: list[tuple[str, int]]                        # [(restaurant type, price range)]
    preference: dict[tuple[str, int], list[Restaurant]]      # {restaurant type: Restaurant}
    possible_options: list[Restaurant]                       # [restaurant name]

    def __init__(self, identifier: int, coordinates: tuple[float, float],
                 route_plan: list[tuple[str, int]], restaurant_data: list[Restaurant]) -> None:
        super().__init__(identifier, coordinates)

        self.route_plan = route_plan.copy()
        self.possible_options = restaurant_data.copy()
        self.preference = self._update_preferences(route_plan)

    def update_preferences(self, new_route_plan: list[tuple[str, int]]) -> None:
        """Update the person's preferences"""

        self.preference = self._update_preferences(new_route_plan)

    def _update_preferences(self, new_route_plan: list[tuple[str, int]]) -> dict[tuple[str, int], list[Restaurant]]:
        """Update the person's preferences"""

        new_preference: dict[tuple[str, int], list[Restaurant]] = {}

        for k in new_route_plan:
            if k not in new_preference:
                new_preference[k] = list(filter(lambda x: x.r_type == k[0] and x.price <= k[1], self.possible_options))

        return new_preference


@check_contracts
class Network:
    """A class that represents the network.

    Instance Attributes:
        - _nodes: The collection of the existing nodes in the network, where the key is the node's unique
                  identifier and the value is the corresponding node

    Representation Invariants:
        - all(identifier == self._nodes[identifier].identifier for identifier in self._nodes)
    """

    _nodes: dict[int, Union[Person, Restaurant]]

    def __init__(self):
        self._nodes = {}

    def add_node(self, node: Union[Restaurant, Person]) -> None:
        """Add node to the network.

        Preconditions:
            - id not in self._nodes
        """

        self._nodes[node.identifier] = node

    def add_edge(self, node1: Union[Restaurant, Person], node2: Union[Restaurant, Person]) -> None:
        """Connect the edge that leads node1 to node2.
        Note that the edge is not a bi-direction.

        Preconditions:
            - node1 in self._nodes
            - node2 not in self._nodes[node1].neighbors
        """

        if node1.identifier not in self._nodes:
            self.add_node(node1)

        if node2.identifier not in self._nodes:
            self.add_node(node2)

        self._nodes[node1.identifier].neighbors[node2.identifier] = self._nodes[node2.identifier]

    def get_distance(self, cuurent_location: _Node, destination: _Node) -> float:
        """Returns the distance between self and a target location"""
        # googlemaps api probabaly need to figure how to do that
        ...
