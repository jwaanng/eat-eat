"""main"""

from formpage import *
from homepage import *
from mapview import *
from classes import *

import csv


def load_restuarant_data(file: str) -> list[Restaurant]:
    """Reads a given restaurants csv file and outputs a list of restaurants"""
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


def generate_new_network_test() -> None:
    """test generate network"""
    # dinner
    restaurant1: Restaurant = Restaurant(1, (123.0, 31.0), 'dinner1', 3, 'Dinner', 'asdf')
    restaurant2: Restaurant = Restaurant(2, (546.0, 413.0), 'dinner2', 1, 'Dinner', 'asdf')
    restaurant3: Restaurant = Restaurant(3, (35.0, 2.0), 'dinner3', 2, 'Dinner', 'asdf')
    restaurant4: Restaurant = Restaurant(4, (54.0, 123.0), 'dinner4', 4, 'Dinner', 'asdf')
    restaurant5: Restaurant = Restaurant(5, (531.0, 647.0), 'dinner5', 3, 'Dinner', 'asdf')
    restaurant6: Restaurant = Restaurant(6, (15.0, 375.0), 'dinner6', 4, 'Dinner', 'asdf')

    # drinks
    restaurant11: Restaurant = Restaurant(11, (151.0, 245.0), 'drink1', 2, 'Drinks', 'asdf')
    restaurant12: Restaurant = Restaurant(12, (23.0, 234.0), 'drink2', 1, 'Drinks', 'asdf')
    restaurant13: Restaurant = Restaurant(13, (14.0, 246.0), 'drink3', 3, 'Drinks', 'asdf')
    restaurant14: Restaurant = Restaurant(14, (432.0, 736.0), 'drink4', 2, 'Drinks', 'asdf')
    restaurant15: Restaurant = Restaurant(15, (56.0, 23.0), 'drink5', 4, 'Drinks', 'asdf')
    restaurant16: Restaurant = Restaurant(16, (1245.0, 54.0), 'drink6', 2, 'Drinks', 'asdf')

    # cafe
    restaurant111: Restaurant = Restaurant(111, (75.0, 142.0), 'cafe1', 2, 'Cafe', 'asdf')
    restaurant112: Restaurant = Restaurant(112, (765.0, 153.0), 'cafe1', 3, 'Cafe', 'asdf')
    restaurant113: Restaurant = Restaurant(113, (354.0, 634.0), 'cafe1', 1, 'Cafe', 'asdf')
    restaurant114: Restaurant = Restaurant(114, (643.0, 643.0), 'cafe1', 1, 'Cafe', 'asdf')
    restaurant115: Restaurant = Restaurant(115, (153.0, 124.2), 'cafe1', 4, 'Cafe', 'asdf')
    restaurant116: Restaurant = Restaurant(116, (235.6, 546.23), 'cafe1', 4, 'Cafe', 'asdf')

    restaurants: list[Restaurant] = [
        restaurant1, restaurant2, restaurant3, restaurant4, restaurant5, restaurant6,
        restaurant11, restaurant12, restaurant13, restaurant14, restaurant15, restaurant16,
        restaurant111, restaurant112, restaurant113, restaurant114, restaurant115, restaurant116
    ]
    person1: Person = Person(0, (123, 324), [('Dinner', 3), ('Drinks', 2), ('Cafe', 2)], restaurants)

    # filtered restaurent data ids:
    #   dinner: 1, 2, 3, 5
    #   drinks: 11, 12, 14, 16
    #   cafe: 111, 113, 114
    test_network: Network = generate_new_network(person1)
    routes: list[tuple[list[Node], float]] = test_network.paths_recommandations(person1)

    print(len(routes))
    print(len(routes) == 48)

    for route in routes:
        print(route)


if __name__ == "__main__":
    home_page = HomePage()
    home_page.run()

    restaurant_data: list[Restaurant] = load_restuarant_data('./Data/Restaurants.csv')
    person: Person = Person(identifier=0, coordinate=home_page.form_page.coordinates,
                            route_plan=home_page.form_page.selections, restaurant_data=restaurant_data)
    network: Network = generate_new_network(person)
    recommanded_paths: list[tuple[list[Node], float]] = network.paths_recommandations(person)[:5]
    print(recommanded_paths)

    # generate_new_network_test()
