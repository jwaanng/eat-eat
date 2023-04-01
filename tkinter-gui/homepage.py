from tkinter import *
from PIL import Image, ImageTk
import formpage

# Create the main window
window = Tk()
window.title("EAT EAT HOME")
window.geometry("1200x800")

# Open the image file using Pillow
image = Image.open('tkinter-gui/images/background.jpeg')

# Resize the image to fit the window
image = image.resize((1200, 800), Image.ANTIALIAS)

# Create a PhotoImage object from the resized image
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
label = Label(window, image=photo)
label.pack(fill=BOTH, expand=True)

# "Don't Know"
eat_label1 = Label(window, text="Don't Know",
                   font=("Didact Gothic", 45), fg="black",
                   highlightbackground="black", highlightthickness=0)
eat_label1.pack(side=RIGHT, padx=0, pady=0)
eat_label1.place(x=700, y=150)

# "What to Eat?"
eat_label1 = Label(window, text="What to Eat?",
                   font=("Didact Gothic", 45), fg="black",
                   highlightbackground="black", highlightthickness=0)
eat_label1.pack(side=RIGHT, padx=0, pady=0)
eat_label1.place(x=700, y=210)

# Create a label for the additional text
back_label = Label(window, text="We've got your back",
                   font=("Didact Gothic", 25), fg="#26547c", highlightthickness=0, padx=0, pady=0, borderwidth=0)
back_label.pack(side=RIGHT, padx=50, pady=0)
back_label.place(x=700, y=300)
back_label.lift()

# Create a button for the "Try Now" action
try_button = Button(window, text="Try Now", font=("Didact Gothic", "10", "bold"), bg="white", fg="black",
                    bd=0, cursor="hand2", width=15, height=3, )
try_button.pack(side=RIGHT, padx=50, pady=10)
try_button.place(x=700, y=350)
try_button.lift()

# Define a function for the button click action


def go_to_another_page():
    # Destroy the current window
    window.destroy()
    formpage.create_new_window()


# Set the button's command to the function that takes you to another page
try_button.configure(command=go_to_another_page)

# Run the main loop
window.mainloop()
