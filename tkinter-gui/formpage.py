from tkinter import *

#######################################################################################################################################
# Help Funcs
#######################################################################################################################################


def validate_input(select_places: StringVar) -> bool:
    """This function takes in the input from user and verifies if the input is valid.
    Valid: is an integer and 0 <= select_places <= 10 
    """
    if select_places == "":
        return None
    elif select_places.isdigit() and int(select_places) >= 1 and int(select_places) <= 10:
        return True
    else:
        return False


def places_select(num_places: StringVar) -> None:
    """This function takes in the input number of places and returns that number of radio selections"""
    options = ['Cafe', 'Dessert', 'Dinner', 'Drinks',
               'Fast Food', 'Lunch', 'Doesn\'t Matter']

    for i in range(num_places):
        group_label = "Place Number:  " + str(i+1)
        button_group = []
        for option in options:
            button = Radiobutton(window, text=option, variable=selected_budget, value="$$", font=(
                "Didact Gothic", 15), bg="#f2f2f2", activebackground="#f2f2f2", fg="#26547c", activeforeground="#26547c")
            button_group.append(button)
            button.pack(side=LEFT, padx=20)
        label = Label(window, text=group_label, font=(
            "Didact Gothic", 15), bg="#f2f2f2", fg="#26547c")
        label.pack()

        # TODO: fix this function !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


window = Tk()
window.title("EAT EAT FORM")
window.geometry("1200x800")

#######################################################################################################################################
# BUDGET QUESTION
#######################################################################################################################################

budget_label = Label(window, text="What is your budget?", font=(
    "Didact Gothic", 18), fg="#26547c", padx=10, pady=10)
budget_label.pack()

selected_budget = StringVar()

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

# Create a label for the number of places question
places_label = Label(window, text="How many places would you like to visit?", font=(
    "Didact Gothic", 18), fg="#26547c", padx=10, pady=10)
places_label.pack()

# Create a frame to hold the entry widget
entry_frame = Frame(window, bg="#f2f2f2", padx=20, pady=20)
entry_frame.pack()

num_places = 0

places_entry = Entry(window, validate="key", validatecommand=(
    window.register(validate_input), '%P'), textvariable=num_places)
places_entry.pack()

submit_button = Button(window, text="Submit", font=("Didact Gothic", 10), bg="#26547c", fg="#ffffff",
                       padx=5, pady=5, activebackground="#f2f2f2", activeforeground="#26547c", command=places_select(num_places))
submit_button.pack(pady=20)

# Run the main loop for the new window
window.mainloop()
