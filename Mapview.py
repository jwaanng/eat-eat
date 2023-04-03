"""This module contains functions allowing graphical maps to be generated as widgets for the tkinter module"""

import tkinter as tk
import tkintermapview as tkmap
from typing import Union
from Classes_and_Functions import Restaurant, Person


class LocationPage:
    """Class for the interface page which generates a graphical visualization of the map"""
    coordinates: tuple[float, float]

    def __init__(self):
        """Initiate a LocationPage with a tkinter window"""
        self.window = tk.Tk()
        self.window.title("EAT EAT FORM")
        self.window.geometry("1200x800")

    def create_new_window(self, route: list[Restaurant]):
        """Create a new window containing a map widget displaying the restaurants on the map"""
        frame = tk.Frame(self.window)
        self.main_frame = frame
        frame.pack()

        final_map_frame = tk.LabelFrame(frame)
        final_map_frame.pack()

        map_widget = create_map_widget(final_map_frame, [route], 800, 600)
        map_widget.pack()

    def run(self):
        """Opens up the window"""
        self.window.mainloop()


def create_user_location_select_map(labelframe: tk.LabelFrame, width: int, height: int) -> tkmap.TkinterMapView:
    """Creates a new map for the purposes of letting the user select their current location.

    Preconditions:
        - width < labelframe.width and height < labelframe.height
    """
    map_widget = tkmap.TkinterMapView(labelframe, width=width, height=height)
    map_widget.grid(row=0, column=0)
    map_widget.set_tile_server("http://a.tile.stamen.com/toner/{z}/{x}/{y}.png")
    map_widget.set_position(deg_x=43.6658971, deg_y=-79.3906104)
    map_widget.set_zoom(15)

    return map_widget


def create_map_widget(labelframe: tk.LabelFrame,
                      list_of_restaurant_routes: tuple[list[Union[Person, Restaurant]], float],
                      width: int, height: int) -> tkmap.TkinterMapView:
    """Create a map widget given a list of node paths showing markers for each node and the paths
    between each node.

    Preconditions:
        - width < labelframe.width and height < labelframe.height
    """

    map_widget = tkmap.TkinterMapView(labelframe, width=width, height=height)
    map_widget.pack()
    map_widget.set_tile_server("http://a.tile.stamen.com/toner/{z}/{x}/{y}.png")
    map_widget.set_position(deg_x=43.6658971, deg_y=-79.3906104)
    map_widget.set_zoom(15)

    for route, distance in list_of_restaurant_routes:
        list_of_restaurant_positions = []

        for node in route:
            if type(node) == Person:
                marker = map_widget.set_marker(
                    deg_x=node.coordinate[0],
                    deg_y=node.coordinate[1],
                    text=f'{node.name} |' + f'Total Distance: {distance}'
                )
            else:
                marker = map_widget.set_marker(
                        deg_x=node.coordinate[0],
                        deg_y=node.coordinate[1],
                        text=f'{node.name}' + '(' + '$' * node.price + ')'
                    )
            list_of_restaurant_positions.append(marker.position)

        map_widget.set_path(list_of_restaurant_positions)

    return map_widget


if __name__ == '__main__':
    test = tk.Tk()
    test.title('Test')
    test.geometry('900x700')

    user_position = []

    def confirm_selection():
        if user_position:
            print(user_position[0])
        else:
            return

    labelframe_test = tk.LabelFrame(test)
    labelframe_test.pack(pady=20)
    button = tk.Button(test, width=15, text='Confirm Selection', command=confirm_selection)
    button.pack()

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
