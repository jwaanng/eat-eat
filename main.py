"""main"""

from Classes_and_Functions import *
from Homepage import *
from Mapview import *


homepage = HomePage()
homepage.run()

restaurant_data: list[Restaurant] = load_restuarant_data('./Data/Restaurants.csv')
person: Person = Person(identifier=0, coordinate=homepage.form_page.coordinates,
                        route_plan=homepage.form_page.selections, restaurant_data=restaurant_data)
network: Network = generate_new_network(person)
shortest_path: tuple[list[Union[Person, Restaurant]], float] = network.get_shortest_route(person)
result_page: LocationPage = LocationPage()

result_page.create_new_window(shortest_path)
result_page.run()
