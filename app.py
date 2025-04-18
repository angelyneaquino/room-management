from tkinter import *

# Create a window
window = Tk()
# Set window properties
window.title("Resistor Color Code")
window.minsize(1000, 800)

# Main container to hold all the panels for each resistor band
main_container = Frame(window, bg="lightgray", width=1000, height=800)
main_container.place(relx=0.5, rely=0.5, anchor="center")



########## Header panel ##########
header_panel = Frame(main_container, bg="blue", width=1000, height=200)
header_panel.place(x=0, y=0, anchor="nw")

# Title Label
title_label = Label(header_panel, text="Resistor Color Code", font=("Arial bold", 24), bg="blue", fg="white") 
title_label.place(relx=0.5, y=50, anchor="center")
########## Header panel ##########



# Resistor band panels
band4_panel = Frame(main_container, bg="red", width=1000, height=600)
band4_panel.place(x=0, y=200, anchor="nw")
band5_panel = Frame(main_container, bg="yellow", width=1000, height=600)
band6_panel = Frame(main_container, bg="orange", width=1000, height=600)
abount_panel = Frame(main_container, bg="violet", width=1000, height=600)



############ Buttons ############
def show_band4_panel():
    band4_panel.place(x=0, y=200, anchor="nw")
    band5_panel.place_forget()
    band6_panel.place_forget()
    abount_panel.place_forget()
show_band4_panel_button = Button(header_panel, text="4-Band Resistor", command=show_band4_panel, font=("Arial", 12), bg="red", height=1, width=16)
show_band4_panel_button.place(x=10, y=168, anchor="nw")


def show_band5_panel():
    band5_panel.place(x=0, y=200, anchor="nw")
    band4_panel.place_forget()
    band6_panel.place_forget()
    abount_panel.place_forget()
show_band5_panel_button = Button(header_panel, text="5-Band Resistor", command=show_band5_panel, font=("Arial", 12), bg="yellow", height=1, width=16)
show_band5_panel_button.place(x=170, y=168, anchor="nw")

def show_band6_panel():
    band6_panel.place(x=0, y=200, anchor="nw")
    band5_panel.place_forget()
    band4_panel.place_forget()
    abount_panel.place_forget()
show_band6_panel_button = Button(header_panel, text="6-Band Resistor", command=show_band6_panel, font=("Arial", 12), bg="orange", height=1, width=16)
show_band6_panel_button.place(x=330, y=168, anchor="nw")

def show_about_panel():
    abount_panel.place(x=0, y=200, anchor="nw")
    band5_panel.place_forget()
    band4_panel.place_forget()
    band6_panel.place_forget()
show_about_panel_button = Button(header_panel, text="About", command=show_about_panel, font=("Arial", 12), bg="violet", height=1, width=16)
show_about_panel_button.place(x=836, y=168, anchor="nw")


window.mainloop()
