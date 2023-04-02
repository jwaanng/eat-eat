"""This module contains functions allowing graphical maps to be generated as widgets for the tkinter module"""

import tkinter
import tkintermapview as tkmap
from classes import Restaurant


def create_map_widget(labelframe: tkinter.LabelFrame, list_of_restaurant_paths: list[list[Restaurant]],
                      width: int, height: int) -> tkmap.TkinterMapView:
    """Create a map widget given a list of restaurant paths showing markers for each restaurant and the paths
    between each restaurant.

    Preconditions:
        - width < labelframe.width and height < labelframe.height
    """

    map_widget = tkmap.TkinterMapView(labelframe, width=width, height=height)
    map_widget.pack()
    map_widget.set_tile_server("http://a.tile.stamen.com/toner/{z}/{x}/{y}.png")
    map_widget.set_position(deg_x=43.6658971, deg_y=-79.3906104)
    map_widget.set_zoom(15)

    for path in list_of_restaurant_paths:
        list_of_restaurant_positions = []
        for restaurant in path:
            marker = map_widget.set_marker(
                deg_x=restaurant.coordinates[0],
                deg_y=restaurant.coordinates[1],
                text=restaurant.name
            )
            list_of_restaurant_positions.append(marker.position)

        if len(path) > 1:
            map_widget.set_path(list_of_restaurant_positions)

    return map_widget


if __name__ == '__main__':

    test = tkinter.Tk()
    test.title('Test')
    test.geometry('900x700')

    labelframe_test = tkinter.LabelFrame(test)
    labelframe_test.pack(pady=20)

    example_restaurant_paths = [[Restaurant(identifier=1, coordinates=(43.6684, -79.38924),
                                            name='Deli Shop', price=1, restaurant_type='Fast Food', address='Toronto'),
                                 Restaurant(identifier=1, coordinates=(43.670420, -79.386450),
                                            name='Starbucks', price=1, restaurant_type='Cafe', address='Toronto')]]

    map_widget_example = create_map_widget(labelframe_test, example_restaurant_paths, 800, 600)
    test.mainloop()
