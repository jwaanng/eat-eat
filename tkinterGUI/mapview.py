"""This module contains functions allowing graphical maps to be generated as widgets for the tkinter module"""

import tkinter
import tkintermapview as tkmap
from classes import Restaurant


def create_user_location_select_map(labelframe: tkinter.LabelFrame, width: int, height: int) -> tkmap.TkinterMapView:
    map_widget = tkmap.TkinterMapView(labelframe, width=width, height=height)
    map_widget.grid(row=0, column=0)  # i changed this to grid - JW
    map_widget.set_tile_server("http://a.tile.stamen.com/toner/{z}/{x}/{y}.png")
    map_widget.set_position(deg_x=43.6658971, deg_y=-79.3906104)
    map_widget.set_zoom(15)

    return map_widget


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

    user_position = []

    def confirm_selection():
        if user_position:
            print(user_position[0])
        else:
            return

    labelframe_test = tkinter.LabelFrame(test)
    labelframe_test.pack(pady=20)
    button = tkinter.Button(test, width=15, text='Confirm Selection', command=confirm_selection)
    button.pack()

    # example_restaurant_paths = [[Restaurant(identifier=1, coordinates=(43.6684, -79.38924),
    #                                         name='Deli Shop', price=1, restaurant_type='Fast Food', address='Toronto'),
    #                              Restaurant(identifier=1, coordinates=(43.670420, -79.386450),
    #                                         name='Starbucks', price=1, restaurant_type='Cafe', address='Toronto')]]

    # map_widget_example = create_map_widget(labelframe_test, example_restaurant_paths, 800, 600)
    map_widget_example_2 = create_user_location_select_map(labelframe_test, 800, 600)

    def add_marker_event(coords):
        map_widget_example_2.delete_all_marker()
        new_marker = map_widget_example_2.set_marker(coords[0], coords[1], text="You are here")
        user_position.clear()
        user_position.append(new_marker.position)


    map_widget_example_2.add_right_click_menu_command(label="Select location",
                                            command=add_marker_event,
                                            pass_coords=True)

    test.mainloop()
