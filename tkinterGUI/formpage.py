import tkinter as tk
from tkinter import ttk
import tkintermapview_gui as tkmap
import mapview


class Form:
    """A class of representing the Tkinter window for the user info form.

    Instance Attributes
    - selections: list of user suggestions
    - slider_submitted: whether user submitted slider or not
    - selections: list of user suggestions
    """
    slider_submitted: bool
    main_frame: None
    selections: list[tuple[str, str]]
    coordinates: tuple[float, float]

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("EAT EAT FORM")
        self.window.geometry("1200x800")

        self.main_frame = None
        self.slider_submitted = False

    def submit_slider(self, num_places) -> None:
        """A function that lets user only submit the slider once."""
        if not self.slider_submitted:
            self.slider_submitted = True
            self.places_select(num_places)

    def get_selections(self, selected_places: list, selected_budgets: list) -> list[tuple[str, str]]:
        """Gives a list of the strings of each place chosen by user in the

        Preconditions:
            - len(selected_places) == len(selected_budgets)
            - len(selected_places) >= 1
        """
        selected_budgets = [budget.get() for budget in selected_budgets]
        selected_places = [place.get() for place in selected_places]

        selections = [(str(selected_places[i]), str(selected_budgets[i]))
                      for i in range(len(selected_places))]

        # print(selections)
        self.selections = selections
        return selections

    def places_select(self, num_places):
        """Creates a widget that lets user select num_places amount of restaurants and """
        options = ['Cafe', 'Dessert', 'Dinner', 'Drinks',
                   'Fast Food', 'Lunch']
        budget_options = ['$', '$$', '$$$', '$$$$']

        selected_places = []
        selected_budgets = []

        budget_frame = tk.LabelFrame(self.main_frame)
        budget_frame.grid(row=1, column=0, ipadx=114)

        for i in range(int(num_places)):
            # Variables for holding current selection
            selected_place = tk.StringVar()
            selected_budget = tk.StringVar()

            # Combobox for type of place
            group_label = "Place #" + str(i + 1) + ":"
            selections_label = tk.Label(budget_frame, text=group_label, font=(
                "Didact Gothic", 10), bg="#f2f2f2", fg="#26547c")
            selections_label.grid(row=i + 1, column=0)

            selection_combobox = tk.ttk.Combobox(budget_frame, values=options, textvariable=selected_place)
            selection_combobox.grid(row=i + 1, column=1)

            # Combobox for price
            budget_group_label = "Budget #" + str(i + 1) + ":"
            budget_label = tk.Label(budget_frame, text=budget_group_label, font=(
                "Didact Gothic", 10), bg="#f2f2f2", fg="#26547c")
            budget_label.grid(row=i + 1, column=2)
            budget_combobox = ttk.Combobox(budget_frame, values=budget_options, textvariable=selected_budget)
            budget_combobox.grid(row=i + 1, column=3)

            selected_places.append(selected_place)
            selected_budgets.append(selected_budget)

        submit_button = tk.Button(budget_frame, text="Submit selections",
                                  command=lambda: self.get_selections(selected_places, selected_budgets),
                                  font=("Didact Gothic", 10), bg="#26547c", fg="#ffffff", padx=5, pady=5,
                                  activebackground="#f2f2f2", activeforeground="#26547c")
        submit_button.grid(row=5, column=2)

        self.create_map()

    def create_map(self):
        places_visit_frame = tk.LabelFrame(self.main_frame)
        places_visit_frame.grid(row=2, column=0)

        user_position = []

        def confirm_selection():
            if user_position:
                print(user_position[0])
            else:
                return

        button = tk.Button(places_visit_frame, text="Submit selections",
                           command=lambda: confirm_selection(),
                           font=("Didact Gothic", 10), bg="#26547c", fg="#ffffff", padx=5, pady=5,
                           activebackground="#f2f2f2", activeforeground="#26547c")
        button.grid(row=1, column=0)

        map_widget_example_2 = tkmap.create_user_location_select_map(places_visit_frame, 700, 500)

        def add_marker_event(coords):
            map_widget_example_2.delete_all_marker()
            new_marker = map_widget_example_2.set_marker(coords[0], coords[1], text="You are here")
            user_position.clear()
            user_position.append(new_marker.position)
            self.coordinates = coords

        map_widget_example_2.add_right_click_menu_command(label="Select location",
                                                          command=add_marker_event,
                                                          pass_coords=True)

    def create_new_window(self):
        frame = tk.Frame(self.window)
        self.main_frame = frame
        frame.pack()

        places_visit_frame = tk.LabelFrame(frame)
        places_visit_frame.grid(row=0, column=0, ipadx=138)

        num_places = tk.IntVar()
        slider_label = tk.Label(places_visit_frame, text="How many places would you like to visit?", font=(
            "Didact Gothic", 15), fg="#26547c", padx=10, pady=10)
        slider_label.grid(row=0, column=0)

        slider = tk.Scale(places_visit_frame, from_=1, to=4, variable=num_places, length=300,
                          width=20,
                          sliderlength=20, highlightthickness=0, bg="#f2f2f2",
                          activebackground="#26547c", troughcolor="#d9d9d9", orient=tk.HORIZONTAL)
        slider.grid(row=1, column=0)

        submit_button = tk.Button(places_visit_frame, text="OK!", font=("Didact Gothic", 10), bg="#26547c",
                                  fg="#ffffff",
                                  padx=5, pady=5, activebackground="#f2f2f2", activeforeground="#26547c",
                                  command=lambda: self.submit_slider(int(num_places.get())))
        submit_button.grid(row=1, column=1)

    def run(self):
        self.window.mainloop()

# hi = Form()
# hi.create_new_window()
# hi.run()
