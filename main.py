"""main"""

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

    _generate_new_network(new_network, user, user, 0, len(user.route_plan))

    return new_network


def _generate_new_network(new_network: Network,
                            node: Union[Restaurant, Person], user: Person, i: int, d: int) -> None:
    """Generate the network using recursion"""

    for neighbour in user.preference[user.route_plan[i]]:
        new_network.add_edge(node, neighbour)

        if i + 1 < d:
            _generate_new_network(new_network, neighbour, user, i + 1, d)


def update_user_preference(user: Person, new_preference: list[tuple[str, int]]) -> Network:
    """Return the new network when the user's preference is updated"""

    user.update_preferences(new_preference)

    return generate_new_network(user)


def generate_new_network_test() -> None:
    # dinner
    restaurant1: Restaurant = Restaurant(1, (0, 0), 'dinner1', 3, 'dinner', 'asdf')
    restaurant2: Restaurant = Restaurant(2, (0, 0), 'dinner2', 1, 'dinner', 'asdf')
    restaurant3: Restaurant = Restaurant(3, (0, 0), 'dinner3', 2, 'dinner', 'asdf')
    restaurant4: Restaurant = Restaurant(4, (0, 0), 'dinner4', 4, 'dinner', 'asdf')
    restaurant5: Restaurant = Restaurant(5, (0, 0), 'dinner5', 3, 'dinner', 'asdf')
    restaurant6: Restaurant = Restaurant(6, (0, 0), 'dinner6', 4, 'dinner', 'asdf')

    # drinks
    restaurant11: Restaurant = Restaurant(11, (0, 0), 'drink1', 2, 'drinks', 'asdf')
    restaurant12: Restaurant = Restaurant(12, (0, 0), 'drink2', 1, 'drinks', 'asdf')
    restaurant13: Restaurant = Restaurant(13, (0, 0), 'drink3', 3, 'drinks', 'asdf')
    restaurant14: Restaurant = Restaurant(14, (0, 0), 'drink4', 2, 'drinks', 'asdf')
    restaurant15: Restaurant = Restaurant(15, (0, 0), 'drink5', 4, 'drinks', 'asdf')
    restaurant16: Restaurant = Restaurant(16, (0, 0), 'drink6', 2, 'drinks', 'asdf')

    # cafe
    restaurant111: Restaurant = Restaurant(111, (0, 0), 'cafe1', 2, 'cafe', 'asdf')
    restaurant112: Restaurant = Restaurant(112, (0, 0), 'cafe1', 3, 'cafe', 'asdf')
    restaurant113: Restaurant = Restaurant(113, (0, 0), 'cafe1', 1, 'cafe', 'asdf')
    restaurant114: Restaurant = Restaurant(114, (0, 0), 'cafe1', 1, 'cafe', 'asdf')
    restaurant115: Restaurant = Restaurant(115, (0, 0), 'cafe1', 4, 'cafe', 'asdf')
    restaurant116: Restaurant = Restaurant(116, (0, 0), 'cafe1', 4, 'cafe', 'asdf')

    restaurants: list[Restaurant] = [
        restaurant1, restaurant2, restaurant3, restaurant4, restaurant5, restaurant6,
        restaurant11, restaurant12, restaurant13, restaurant14, restaurant15, restaurant16,
        restaurant111, restaurant112, restaurant113, restaurant114, restaurant115, restaurant116
    ]
    person1: Person = Person(0, (0, 0), [('dinner', 3), ('drinks', 2), ('cafe', 2)], restaurants)

    # filtered restaurent data ids:
    #   dinner: 1, 2, 3, 5
    #   drinks: 11, 12, 14, 16
    #   cafe: 111, 113, 114
    test_network: Network = generate_new_network(person1)
    routes: list[list[Node]] = test_network.find_all_routes(person1)

    print(len(routes))
    print(len(routes) == 48)
    new_line = routes[0][0]

    for route in routes:
        if route[0] != new_line:
            new_line = route[0]
            print()

        print(route)


if __name__ == "__main__":
    # restaurant_data: list[Restaurant] = load_restuarant_data(...)
    # person: Person = Person(0, ..., )      # idk how exactly the list of perference will be inputted
    # network: Network = generate_new_network(person)

    generate_new_network_test()
