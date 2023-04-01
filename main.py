from classes import Restaurant, Person, Network
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

    return list_of_restuarants


def generate_new_network(restaurants: list[Restaurant], user: Person) -> Network:
    """Generate the network based on the person's prefernce"""
    restuarants: list[Restaurant] = _filter_restaurants(restaurants, user)
    new_network: Network = Network()

    return new_network


def _filter_restaurants(restaurants: list[Restaurant], user: Person) -> list[Restaurant]:
    """Return the new list of restaurants, which is filterd by the user's preference"""

    return list(filter(lambda x: x.price == user.price_range and x.restaurant_type, restaurants))


if __name__ == "__main__":
    restaurant_data: list[Restaurant] = load_restuarant_data(...)
    person: Person = Person(0, ..., )      # idk how exactly the list of perference will be
    network: Network = generate_new_network(restaurant_data, person)
