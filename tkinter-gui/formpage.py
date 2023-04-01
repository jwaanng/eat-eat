from tkinter import *
from python_ta.contracts import check_contracts

#######################################################################################################################################
# Help Funcs
#######################################################################################################################################


@check_contracts
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


def places_select(num_places: int, window: str) -> None:
    """This function takes in the input number of places and returns that number of radio selections"""
    options = ['Cafe', 'Dessert', 'Dinner', 'Drinks',
               'Fast Food', 'Lunch', 'Doesn\'t Matter']
    selected_places = []

    def get_selections():
        """Gives a list of the strings of each place chosen by user in the"""
        nonlocal selected_places
        selected_places = [place.get() for place in selected_places]
        print(selected_places)

    for i in range(num_places):
        selected_place = StringVar()
        radio_frame = Frame(window, bg="#f2f2f2", padx=20, pady=20)
        group_label = "Place Number" + str(i+1) + ":"
        label = Label(radio_frame, text=group_label, font=(
            "Didact Gothic", 15), bg="#f2f2f2", fg="#26547c")
        label.pack(side=LEFT)

        for option in options:
            button = Radiobutton(radio_frame, text=option, variable=selected_place, value=option, font=(
                "Didact Gothic", 15), bg="#f2f2f2", activebackground="#f2f2f2", fg="#26547c", activeforeground="#26547c")
            button.pack(side=LEFT, padx=20)
        radio_frame.pack()

        selected_places.append(selected_place)

    button = Button(window, text="Submit selections", command=get_selections, font=("Didact Gothic", 10), bg="#26547c", fg="#ffffff",
                    padx=5, pady=5, activebackground="#f2f2f2", activeforeground="#26547c")
    button.pack()


def create_new_window() -> None:
    """Window of the form where users can input their preferences"""
    window = Tk()
    window.title("EAT EAT FORM")
    window.geometry("1200x800")

    #######################################################################################################################################
    # BUDGET QUESTION
    #######################################################################################################################################
    selected_budget = StringVar()

    budget_label = Label(window, text="What is your budget?", font=(
        "Didact Gothic", 18), fg="#26547c", padx=10, pady=10)
    budget_label.pack()

    radio_frame = Frame(window, bg="#f2f2f2", padx=20, pady=20)
    radio_frame.pack()

    option_1 = Radiobutton(radio_frame, text="$", variable=selected_budget, value="$", font=(
        "Didact Gothic", 15), bg="#f2f2f2", activebackground="#f2f2f2", fg="#26547c", activeforeground="#26547c")
    option_1.pack(side=LEFT, padx=20)

    option_2 = Radiobutton(radio_frame, text="$$", variable=selected_budget, value="$$", font=(
        "Didact Gothic", 15), bg="#f2f2f2", activebackground="#f2f2f2", fg="#26547c", activeforeground="#26547c")
    option_2.pack(side=LEFT, padx=20)

    option_3 = Radiobutton(radio_frame, text="$$$", variable=selected_budget, value="$$$", font=(
        "Didact Gothic", 15), bg="#f2f2f2", activebackground="#f2f2f2", fg="#26547c", activeforeground="#26547c")
    option_3.pack(side=LEFT, padx=20)

    option_4 = Radiobutton(radio_frame, text="$$$$", variable=selected_budget, value="$$$$", font=(
        "Didact Gothic", 15), bg="#f2f2f2", activebackground="#f2f2f2", fg="#26547c", activeforeground="#26547c")
    option_4.pack(side=LEFT, padx=20)

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

    # Run the main loop for the new window
    window.mainloop()


create_new_window()
# window = Tk()
# window.title("EAT EAT FORM")
# window.geometry("1200x800")

# places_select(2, window)
# window.mainloop()
