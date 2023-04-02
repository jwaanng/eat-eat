"""Necessary classes for the project"""

from __future__ import annotations
from typing import Union
from python_ta.contracts import check_contracts


@check_contracts
class Node:
    """An abstract class that represents a location.

    Instance Attributes
    - identifier:
        The id is an integer value that uniquely identifies each node
    - coordinates:
        For the restaurant: A tuple representing longitutde and latitude of the restaurant's address
        For the person: A tuple representing longitutde and latitude of the the person's current location
    - neighbors:
        A mapping containing the neighbor nodes where the key is the unique neighbor id and
        the value is the corresponding neighbor node.

     Representation Invariants:
     - self.identifier not in self.neighbours
     - all(neighbour == self.neighbour[neighbour].identifier for neighbour in self.neighbours)
    """
    identifier: int
    coordinates: tuple[float, float]
    neighbours: dict[int, Node]

    def __init__(self, identifier: int, coordinates: tuple[float, float]) -> None:
        """Initialize this node with the unique identifier and coordinate location"""
        self.identifier = identifier
        self.coordinates = coordinates
        self.neighbours = {}

    def find_all_routes(self, path_length: int, visited: set[Node]) -> list[list[Node]]:
        """Return all possible routes that matches user route plan preference"""

        if len(visited) == path_length - 1:
            return [[self]]

        routes: list[list[Node]] = []

        visited.add(self)

        for neighbour in self.neighbours.values():
            if neighbour not in visited:
                for route in neighbour.find_all_routes(path_length, visited):
                    routes.append([self] + route)

        visited.remove(self)

        return routes

    def __repr__(self) -> str:
        """Return a string representing this node."""
        return f'Node({self.identifier})'


@check_contracts
class Restaurant(Node):
    """A class which represents the restaurant node in the network

    Instance Attributes:
    - name: The name of this restaurant.
    - price: An integer from 1 to 4 representing the price range of this restaurant.
    - r_type: The type of restaurant this is.
    - address: The street address of this restaurant.

    Representation Invariants:
    - self.r_type in ("Drinks", "Cafe", "Dessert", "Fast Food", "Dinner")
    - ...   # TODO
    """
    name: str
    price: int
    r_type: str  # r short for restaurant
    address: str

    def __init__(self, identifier: int, coordinates: tuple[float, float],
                 name: str, price: int, restaurant_type: str, address: str) -> None:
        """Initialize this restaurant with the given arguments."""

        super().__init__(identifier, coordinates)

        self.name = name
        self.price = price
        self.r_type = restaurant_type
        self.address = address

    def __repr__(self) -> str:
        """Return a string representing this restaurant"""

        # return f"Restaurant: {self.name}, price: {'$' * self.price}, type: {self.r_type}, address: {self.address}"
        return f"Restaurant: {self.identifier}"     # TODO this is simplified str representation for testing purpose


@check_contracts
class Person(Node):
    """ A child class of Node, representing one user

    Instance Attributes:
        - route_plan: It represents person's
        - preferences: ... # TODO
    """

    route_plan: list[tuple[Union[str, None], int]]                         # [(restaurant type, price range)]
    preference: dict[tuple[str, int], list[Restaurant]]       # {restaurant type: corresponding possible restaurants}
    _possible_options: list[Restaurant]                       # [All possible restaurants]

    def __init__(self, identifier: int, coordinates: tuple[float, float],
                 route_plan: list[tuple[str, int]], restaurant_data: list[Restaurant]) -> None:
        super().__init__(identifier, coordinates)

        self.route_plan = route_plan.copy()
        self._possible_options = restaurant_data.copy()
        self.preference = self._update_preferences(route_plan)

    def update_preferences(self, new_route_plan: list[tuple[str, int]]) -> None:
        """Update the person's preferences"""

        self.route_plan = new_route_plan.copy()
        self.preference = self._update_preferences(new_route_plan)

    def _update_preferences(self, new_route_plan: list[tuple[str, int]]) -> dict[tuple[str, int], list[Restaurant]]:
        """Update the person's preferences"""

        new_preference: dict[tuple[str, int], list[Restaurant]] = {}

        for k in new_route_plan:
            if k not in new_preference:
                new_preference[k] = list(filter(lambda x: x.r_type == k[0] and x.price <= k[1], self._possible_options))

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
            - node.identifier not in self._nodes
        """

        self._nodes[node.identifier] = node

    def add_edge(self, node1: Union[Restaurant, Person], node2: Union[Restaurant, Person]) -> None:
        """Connect the edge that leads node1 to node2.
        Note that the edge is not a bi-direction.

        Preconditions:
            - node2 not in self._nodes[node1].neighbors
        """

        if node1.identifier != node2.identifier:
            if node1.identifier not in self._nodes:
                self.add_node(node1)

            if node2.identifier not in self._nodes:
                self.add_node(node2)

            self._nodes[node1.identifier].neighbours[node2.identifier] = self._nodes[node2.identifier]

    def _find_all_routes(self, user: Person) -> list[list[Node]]:
        """Return a list of all possible paths in this network which satifies the person's prefernce"""

        routes: list[list[Node]] = []
        route_length = len(user.route_plan)

        for neighbour in user.neighbours.values():
            routes.extend(neighbour.find_all_routes(route_length, set()))

        return routes

    def get_distance(self, departure: Node, destination: Node) -> float:
        """Returns the straight distance between the departure and destination location"""

        x_dist: float = (destination.coordinates[0] - departure.coordinates[0]) ** 2
        y_dist: float = (destination.coordinates[1] - departure.coordinates[1]) ** 2

        return (x_dist + y_dist) ** 0.5

    def paths_recommandation(self, user: Person) -> list[tuple[list[Node], float]]:
        """Return a sorted list of all possible paths in this network which satifies the person's prefernce by
        ascending distance order"""

        routes: list[tuple[list[Node], float]] = []

        for route in self._find_all_routes(user):
            routes.append((route, sum(self.get_distance(route[i], route[i + 1]) for i in range(len(route) - 1))))

        routes.sort(key=lambda x: x[1])

        return routes
