"""main"""

from classes import *
import csv


def load_restuarant_data(file: str) -> list[Restaurant]:
    """Reads a given restaurants csv file and outputs a list of restaurants"""
    with open(file) as restaurants_file:
        reader = csv.reader(restaurants_file)
        list_of_restuarants = []

        next(reader)

        i = 0

        for row in reader:
            restuarant_node = Restaurant(
                identifier=i,
                coordinates=(float(row[2]), float(row[3])),
                name=row[0],
                price=int(row[4]),
                r_type=row[5],
                address=row[1]
            )

            list_of_restuarants.append(restuarant_node)
            i += 1

    return list_of_restuarants


def generate_new_network(user: Person) -> Network:
    """Generate the network based on the person's prefernce"""
    new_network: Network = Network()

    _gegenerate_new_network(new_network,
                            user, user, 0, len(user.route_plan))

    return new_network


def _gegenerate_new_network(new_network: Network,
                            node: Union[Restaurant, Person], user: Person, i: int, d: int) -> None:
    """Generate the network using recursion"""

    for neighbour in user.preference[user.route_plan[i]]:
        new_network.add_edge(node, neighbour)

        if i + 1 < d:
            _gegenerate_new_network(new_network, neighbour, user, i + 1, d)


if __name__ == "__main__":
    restaurant_data: list[Restaurant] = load_restuarant_data(...)
    person: Person = Person(0, ..., )      # idk how exactly the list of perference will be inputted
    network: Network = generate_new_network(person)
