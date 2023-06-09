"""Necessary classes for the backend operation for the CSC111 project"""

from __future__ import annotations
from typing import Union
from python_ta.contracts import check_contracts

import csv


@check_contracts
class Node:
    """An abstract class that represents a location.

    Instance Attributes
        - identifier:
            The id is an integer value that uniquely identifies each node
        - coordinate:
            For the restaurant: A tuple representing longitutde and latitude of the restaurant's address
            For the person: A tuple representing longitutde and latitude of the person's current location
        - neighbors:
            A mapping containing the neighbor nodes where the key is the unique neighbor id and
            the value is the corresponding neighbor node.

     Representation Invariants:
         - self.identifier not in self.neighbours
         - self.name != ''
         - all(neighbour == self.neighbour[neighbour].identifier for neighbour in self.neighbours)
    """
    identifier: int
    name: str
    coordinate: tuple[float, float]
    neighbours: dict[int, Node]

    def __init__(self, identifier: int, coordinate: tuple[float, float], name: str) -> None:
        """Initialize this node with the unique identifier and coordinate location"""
        self.identifier = identifier
        self.coordinate = coordinate
        self.name = name
        self.neighbours = {}

    def find_all_routes(self, route_length: int, visited: set[Node]) -> list[list[Node]]:
        """Return all possible routes that matches user route plan preference"""

        if len(visited) == route_length:
            return [[self]]

        routes: list[list[Node]] = []

        visited.add(self)

        for neighbour in self.neighbours.values():
            if neighbour not in visited:
                for route in neighbour.find_all_routes(route_length, visited):
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
        - self.name != ''
        - 0 < self.price < 5
        - self.r_type in {"Drinks", "Cafe", "Dessert", "Fast Food", "Lunch", "Dinner"}
        - self.address != ''
    """

    price: int
    r_type: str  # r short for restaurant
    address: str

    def __init__(self, identifier: int, coordinate: tuple[float, float],
                 name: str, price: int, r_type: str, address: str) -> None:
        """Initialize the restaurant with the given arguments."""

        super().__init__(identifier, coordinate, name)

        self.price = price
        self.r_type = r_type
        self.address = address

    def __repr__(self) -> str:
        """Return a string representing this restaurant"""

        return f"Restaurant: {self.name}, coordinate: {self.coordinate}, " \
               f"price: {'$' * self.price}, type: {self.r_type}, address: {self.address}"


@check_contracts
class Person(Node):
    """ A child class of Node, representing one user

    Instance Attributes:
        - route_plan: The order of restaurants types and the corresponding maximum price range
                      that the person is planning to visit.
        - preferences: The dictionary mapping where the key is a tuple of restaurant's type and
                       the maximum price range for that restaurant, and the key is the corresponding restaurants that
                       satisfies the key.
        - _possible_options: All possible restaurants for the person can visit

    Representation Invariants:
        - len(self.route_plan) > 0 and all(plan != () for plan in self.route_plan)
        - len(self.preference) > 0 and len(self.preference.values()) > 0
        - self._possible_options != []
    """

    route_plan: list[tuple[str, int]]  # [(restaurant type, price range)]
    preference: dict[tuple[str, int], list[Restaurant]]  # {restaurant type: corresponding POSSIBLE restaurants}
    _possible_options: list[Restaurant]  # [ALL possible restaurants]

    def __init__(self, identifier: int, coordinate: tuple[float, float],
                 route_plan: list[tuple[str, int]], restaurant_data: list[Restaurant]) -> None:
        """Initialize the person with the given arguments."""

        super().__init__(identifier, coordinate, 'YOU')

        self.route_plan = route_plan.copy()
        self._possible_options = restaurant_data.copy()
        self.preference = self._update_preferences(route_plan)

    def update_preferences(self, new_route_plan: list[tuple[str, int]]) -> None:
        """Update the person's preferences"""

        self.route_plan = new_route_plan.copy()
        self.preference = self._update_preferences(new_route_plan)

    def _update_preferences(self, new_route_plan: list[tuple[str, int]]) -> dict[tuple[str, int], list[Restaurant]]:
        """Private helper method for updating the person's preferences with the
        filtered restaurents based on the given route plan.
        """

        new_preference: dict[tuple[str, int], list[Restaurant]] = {}

        for k in new_route_plan:
            if k not in new_preference:
                new_preference[k] = list(filter(lambda x: x.r_type == k[0] and x.price <= k[1], self._possible_options))

        return new_preference

    def __repr__(self):
        return f"Person's location: {self.coordinate}"


@check_contracts
class Network:
    """A class that represents the network.

    Instance Attributes:
        - _nodes: The collection of the nodes existing in the network, where the key is the node's unique
                  identifier and the value is the corresponding node

    Representation Invariants:
        - all(node == self._nodes[node].identifier for node in self._nodes)
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
        """Connect the edge that leads node1 to node2. Note that the edge has a direction.
         However, it's still possible to establish the non-direction relationship..

        Preconditions:
            - node2 not in self._nodes[node1].neighbors
        """

        if node1.identifier != node2.identifier:
            if node1.identifier not in self._nodes:
                self.add_node(node1)

            if node2.identifier not in self._nodes:
                self.add_node(node2)

            self._nodes[node1.identifier].neighbours[node2.identifier] = self._nodes[node2.identifier]

    def get_distance(self, departure: Node, destination: Node) -> float:
        """Returns the straight distance between the departure and destination location

        Preconditions:
            - departure.identifier != destination.identifier
        """

        x_dist: float = (destination.coordinate[0] - departure.coordinate[0]) ** 2
        y_dist: float = (destination.coordinate[1] - departure.coordinate[1]) ** 2

        return (x_dist + y_dist) ** 0.5

    def get_shortest_route(self, user: Person) -> tuple[list[Union[Person, Restaurant]], float]:
        """Return the shortest route from all possible routes in this network which satifies the person's
        prefernce by ascending distance order.

        Preconditions:
            - len(user.neighbours) > 0
        """

        routes: list[tuple[list[Union[Person, Restaurant]], float]] = []

        for route in user.find_all_routes(len(user.route_plan), set()):
            restaurants = [self._nodes[node.identifier] for node in route]

            routes.append((restaurants, sum(self.get_distance(route[i], route[i + 1]) for i in range(len(route) - 1))))

        routes.sort(key=lambda x: x[1])

        return routes[0]


def load_restuarant_data(file: str) -> list[Restaurant]:
    """Reads a given restaurants csv file and outputs a list of restaurants

    Preconditions:
        - file != ''
    """
    with open(file) as restaurants_file:
        reader = csv.reader(restaurants_file)
        list_of_restuarants = []

        next(reader)

        i = 1

        for row in reader:
            restuarant_node = Restaurant(identifier=i, coordinate=(float(row[2]), float(row[3])), name=row[0],
                                         price=int(row[4]), r_type=row[5], address=row[1])

            list_of_restuarants.append(restuarant_node)
            i += 1

    return list_of_restuarants


def generate_new_network(user: Person) -> Network:
    """Generate the network based on the person's prefernce"""
    new_network: Network = Network()

    _connect_nodes(new_network=new_network, node=user, user=user, i=0, d=len(user.route_plan))

    return new_network


def _connect_nodes(new_network: Network, node: Union[Restaurant, Person], user: Person, i: int, d: int) -> None:
    """Private helper function for connecting the nodes and generate the network."""

    for neighbour in user.preference[user.route_plan[i]]:
        new_network.add_edge(node, neighbour)

        if i + 1 < d:
            _connect_nodes(new_network, neighbour, user, i + 1, d)


def update_user_preference(user: Person, new_preference: list[tuple[str, int]]) -> Network:
    """Return the new network when the user's preference is updated"""

    user.update_preferences(new_preference)

    return generate_new_network(user)


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['__future__', 'typing'],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120
    })
