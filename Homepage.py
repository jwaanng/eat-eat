from tkinter import *
from Formpage import *
from PIL import Image, ImageTk
from typing import Union


class HomePage:
    """Class representing the home page

    Instance Attributes:
    - form_page: representing the form object related to this homepage
    """
    form_page: Union[Form, None] = None

    def __init__(self):
        """Initialize the HomePage"""
        # Create the main window
        self.window = Tk()
        self.window.title("EAT EAT HOME")
        self.window.geometry("1200x800")

        # Open the image file using Pillow
        image = Image.open('./Images/background.jpeg')

        # Resize the image to fit the window
        image = image.resize((1200, 800), Image.LANCZOS)

        # Create a PhotoImage object from the resized image
        self.photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        self.label = Label(self.window, image=self.photo)
        self.label.pack(fill=BOTH, expand=True)

        # "Don't Know"
        self.eat_label1 = Label(self.window, text="Don't Know",
                                font=("Didact Gothic", 45), fg="black",
                                highlightbackground="black", highlightthickness=0)
        self.eat_label1.pack(side=RIGHT, padx=0, pady=0)
        self.eat_label1.place(x=700, y=150)

        # "What to Eat?"
        self.eat_label2 = Label(self.window, text="What to Eat?",
                                font=("Didact Gothic", 45), fg="black",
                                highlightbackground="black", highlightthickness=0)
        self.eat_label2.pack(side=RIGHT, padx=0, pady=0)
        self.eat_label2.place(x=700, y=230)

        # Create a label for the additional text
        self.back_label = Label(self.window, text="We've got your back",
                                font=("Didact Gothic", 25), fg="#26547c", highlightthickness=0,
                                padx=0, pady=0, borderwidth=0)
        self.back_label.pack(side=RIGHT, padx=50, pady=0)
        self.back_label.place(x=700, y=300)
        self.back_label.lift()

        # Create a button for the "Try Now" action
        self.try_button = Button(self.window, text="Try Now", font=("Didact Gothic", "10", "bold"),
                                 bg="white", fg="black", bd=0, cursor="hand2", width=15, height=3)
        self.try_button.pack(side=RIGHT, padx=50, pady=10)
        self.try_button.place(x=700, y=350)
        self.try_button.lift()

        # Set the button's command to the function that takes you to another page
        self.try_button.configure(command=self.go_to_form_page)

    def go_to_form_page(self) -> None:
        """Directs to the 'formpage' when button is pressed"""
        # Destroy the current window
        self.window.destroy()
        form = Form()
        form.create_new_window()
        self.form_page = form
        form.run()

    def run(self):
        """Runs the tkinker GUI window for the user input"""
        # Run the main loop
        self.window.mainloop()

