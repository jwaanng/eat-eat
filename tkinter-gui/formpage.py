from tkinter import *
from python_ta.contracts import check_contracts

#######################################################################################################################################
# Help Funcs
#######################################################################################################################################


def validate_input(select_places):
    """This function takes in the input from user and verifies if the input is valid.
    Valid: is an integer and 0 <= select_places <= 10

    Preconditions:
        - select_places.type() == StringVar
        - select_places >= 0 and select_places <= 10
    """
    if select_places == "":
        return None
    elif select_places.isdigit() and int(select_places) >= 1 and int(select_places) <= 10:
        return True
    else:
        return False


@check_contracts
def get_selections(selected_places: list, selected_budgets: list) -> list[tuple[str, str]]:
    """Gives a list of the strings of each place chosen by user in the

    Preconditions:
        - len(selected_places) == len(selected_budgets)
        - len(selected_places) >= 1
    """
    selected_budgets = [budget.get() for budget in selected_budgets]
    selected_places = [place.get() for place in selected_places]

    selections = [(str(selected_places[i]), str(selected_budgets[i]))
                  for i in range(len(selected_places))]

    # print(selected_budgets)
    # print(selections)
    return selections


def places_select(num_places: int, window: str) -> None:
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
        radio_frame = Frame(window, bg="#f2f2f2", padx=20, pady=20)
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
        radio_frame = Frame(window, bg="#f2f2f2", padx=20, pady=20)
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

    button = Button(window, text="Submit selections", command=lambda: get_selections(selected_places=selected_places, selected_budgets=selected_budgets), font=(
        "Didact Gothic", 10), bg="#26547c", fg="#ffffff", padx=5, pady=5, activebackground="#f2f2f2", activeforeground="#26547c")
    button.pack()


def create_new_window() -> None:
    """Window of the form where users can input their preferences"""
    window = Tk()
    window.title("EAT EAT FORM")
    window.geometry("1200x800")

    #######################################################################################################################################
    # Places Question
    #######################################################################################################################################
    num_places = IntVar()

    slider_label = Label(window, text="How many places would you like to visit?", font=(
        "Didact Gothic", 18), fg="#26547c", padx=10, pady=10)
    slider_label.pack()

    slider_frame = Frame(window, bg="#f2f2f2", padx=20, pady=20)
    slider_frame.pack()

    slider = Scale(slider_frame, from_=1, to=10, variable=num_places, orient=HORIZONTAL, length=300, width=20,
                   sliderlength=20, highlightthickness=0, bg="#f2f2f2", activebackground="#26547c", troughcolor="#d9d9d9")
    slider.pack()

    submit_button = Button(window, text="Submit", font=("Didact Gothic", 10), bg="#26547c", fg="#ffffff",
                           padx=5, pady=5, activebackground="#f2f2f2", activeforeground="#26547c", command=lambda: places_select(num_places.get(), window))
    submit_button.pack()

    # TODO: SOME IMPLEMENTATION OF THE MAP HERE

    # Run the main loop for the new window
    window.mainloop()


create_new_window()
