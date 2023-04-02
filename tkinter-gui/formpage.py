from tkinter import *
from PIL import Image, ImageTk
from python_ta.contracts import check_contracts


@check_contracts
class FormWindow():
    """A class of representing the Tkinter window

    Instance Attributes:
    - title: title of the window

    """

    def __init__(self):
        self.window = Tk()
        self.window.title("EAT EAT FORM")
        self.window.geometry("1200x800")

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

        return selections

    def places_select(self, num_places) -> None:
        """This function takes in the input number of places and returns that number of radio selections"""
        options = ['Cafe', 'Dessert', 'Dinner', 'Drinks',
                   'Fast Food', 'Lunch', 'Doesn\'t Matter']
        budget_options = ['$', '$$', '$$$', '$$$$']

        # holding current selections in order
        selected_places = []
        selected_budgets = []

        for i in range(num_places):
            # Variables for holding current selection
            selected_place = StringVar()
            selected_budget = StringVar()

            # Radio Frame for type of place
            radio_frame = Frame(self.window, bg="#f2f2f2", padx=20, pady=20)
            group_label = "Place Number" + str(i+1) + ":"
            label = Label(radio_frame, text=group_label, font=(
                "Didact Gothic", 15), bg="#f2f2f2", fg="#26547c")
            label.pack()

            for option in options:
                button = Radiobutton(radio_frame, text=option, variable=selected_place, value=option, font=(
                    "Didact Gothic", 15), bg="#f2f2f2", activebackground="#f2f2f2", fg="#26547c", activeforeground="#26547c")
                button.pack(side=LEFT, padx=20)
            radio_frame.pack()

            selected_places.append(selected_place)

            # Radio Frame for budget
            radio_frame = Frame(self.window, bg="#f2f2f2", padx=20, pady=20)
            group_label = "Budget for place:" + str(i+1) + ":"
            label = Label(radio_frame, text=group_label, font=(
                "Didact Gothic", 15), bg="#f2f2f2", fg="#26547c")
            label.pack()

            for budget in budget_options:
                button = Radiobutton(radio_frame, text=budget, variable=selected_budget, value=budget, font=(
                    "Didact Gothic", 15), bg="#f2f2f2", activebackground="#f2f2f2", fg="#26547c", activeforeground="#26547c")
                button.pack(side=LEFT, padx=20)
            radio_frame.pack()

            selected_budgets.append(selected_budget)

        button = Button(self.window, text="Submit selections", command=lambda: self.get_selections(selected_places=selected_places, selected_budgets=selected_budgets), font=(
            "Didact Gothic", 10), bg="#26547c", fg="#ffffff", padx=5, pady=5, activebackground="#f2f2f2", activeforeground="#26547c")
        button.pack()

    def submit_slider(self, num_places):
        """A function that lets user only submit the slider once."""
        if not self.slider_submitted:  # check if slider has been submitted before
            self.slider_submitted = True
            self.places_select(num_places)

    def create_new_window(self):
        num_places = IntVar()
        self.slider_submitted = False  # initialize the attribute

        slider_label = Label(self.window, text="How many places would you like to visit?", font=(
            "Didact Gothic", 18), fg="#26547c", padx=10, pady=10)
        slider_label.pack()

        slider_frame = Frame(self.window, bg="#f2f2f2", padx=20, pady=20)
        slider_frame.pack()

        slider = Scale(slider_frame, from_=1, to=10, variable=num_places, orient=HORIZONTAL, length=300, width=20,
                       sliderlength=20, highlightthickness=0, bg="#f2f2f2", activebackground="#26547c", troughcolor="#d9d9d9")
        slider.pack()

        submit_button = Button(self.window, text="Submit", font=("Didact Gothic", 10), bg="#26547c", fg="#ffffff",
                               padx=5, pady=5, activebackground="#f2f2f2", activeforeground="#26547c", command=lambda: self.submit_slider(int(num_places.get())))
        submit_button.pack()

    def go_to_map_page(self) -> None:
        """Directs to the 'formpage' when button is pressed"""
        # Destroy the current window
        self.window.destroy()
        ...

    def run(self):
        # Run the main loop
        self.window.mainloop()
