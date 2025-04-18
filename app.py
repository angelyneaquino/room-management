from tkinter import *

# Create a window
window = Tk()
# Set window properties
window.title("Resistor Color Code")
window.minsize(1000, 800)

main_panel = Frame(window, bg="lightgray", width=1000, height=800)
main_panel.place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()
