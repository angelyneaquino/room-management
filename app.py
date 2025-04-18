from tkinter import *

# Create a window
window = Tk()
# Set window properties
window.title("Resistor Color Code")
window.minsize(1000, 800)

# Main container to hold all the panels for each resistor band
main_container = Frame(window, bg="lightgray", width=1000, height=800)
main_container.place(relx=0.5, rely=0.5, anchor="center")

# Header panel
header_panel = Frame(main_container, bg="blue", width=1000, height=200)
header_panel.place(x=0, y=0, anchor="nw")

# Resistor band panels
band4_panel = Frame(main_container, bg="red", width=1000, height=600)
band4_panel.place(x=0, y=200, anchor="nw")
band5_panel = Frame(main_container, bg="red", width=1000, height=600)
band5_panel.place(x=0, y=200, anchor="nw")
band6_panel = Frame(main_container, bg="red", width=1000, height=600)
band6_panel.place(x=0, y=200, anchor="nw")




window.mainloop()
