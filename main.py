"""main"""

from homepage import *
from mapview import *

import csv


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
    homepage = HomePage()
    homepage.run()

    restaurant_data: list[Restaurant] = load_restuarant_data('./Data/Restaurants.csv')
    person: Person = Person(identifier=0, coordinate=homepage.form_page.coordinates,
                            route_plan=homepage.form_page.selections, restaurant_data=restaurant_data)
    network: Network = generate_new_network(person)
    shortest_path: list[Node] = network.get_shortest_route(person)
    result_page: LocationPage = LocationPage()

    result_page.create_new_window(shortest_path)
    result_page.run()
