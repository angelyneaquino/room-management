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
band4 = Frame(main_container, bg="red", width=500, height=600)
band4.place(x=0, y=200, anchor="nw")
about_panel = Frame(main_container, bg="violet", width=1000, height=600)



############# Resistor ############

# band library

class Resistor:

    def __init__(self, container):
        self.band = 4
        self.ohms = 1000
        self.tolerance = 0.05
        self.ppm = 10
        self.panel = Frame(container, bg="white", width=500, height=600)

        band_values = [0,0,0,0,0,0]

        self.resistor_container = Frame(self.panel, bg="white", width=400, height=120)
        self.resistor_label = Label(self.panel, text="Resistor Value:", font=("Arial bold", 16), bg="white", fg="black")
        self.resistor_value = Label(self.panel, text=f"{self.ohms} Ohms {self.tolerance*100}% {'' if self.ppm == 0 else (str(self.ppm)+' PPM')}", font=("Arial bold", 16), bg="white", fg="black")
    
        self.resistor_container.place(relx=0.5, y=200, anchor="center")
        self.resistor_label.place(relx=0.5, y=350, anchor="center")
        self.resistor_value.place(relx=0.5, y=380, anchor="center")

        # Initial resistor
        self.resistor_head = Frame(self.resistor_container, bg="PeachPuff2", width=80, height=120)
        self.resistor_head.place(x=0, y=0, anchor="nw")
        self.resistor_body = Frame(self.resistor_container, bg="PeachPuff2", width=240, height=80)
        self.resistor_body.place(x=80, y=20, anchor="nw")
        self.resistor_foot = Frame(self.resistor_container, bg="PeachPuff2", width=80, height=120)
        self.resistor_foot.place(x=320, y=0, anchor="nw")



        

    def update(self):
        self.resistor_value.config(text=f"{self.ohms} Ohms {self.tolerance*100}% {'' if self.ppm == 0 else (str(self.ppm)+' PPM')}")

    def show(self):
        self.panel.place(x=500, y=200, anchor="nw")
        
    def hide(self):
        self.panel.place_forget()
            



# Create Resistor Object
resistor = Resistor(main_container)
resistor.show()


############ Buttons ############
def show_band4():
    band4.place(x=0, y=200, anchor="nw")
    resistor.ohms = 100
    resistor.update()
    resistor.show()
    about_panel.place_forget()
show_band4_button = Button(header_panel, text="4-Band Resistor", command=show_band4, font=("Arial", 12), bg="red", height=1, width=16)
show_band4_button.place(x=10, y=168, anchor="nw")

def show_band5():
    band4.place(x=0, y=200, anchor="nw")
    resistor.ohms = 200
    resistor.update()
    resistor.show()
    about_panel.place_forget()
show_band5_button = Button(header_panel, text="5-Band Resistor", command=show_band5, font=("Arial", 12), bg="yellow", height=1, width=16)
show_band5_button.place(x=170, y=168, anchor="nw")

def show_band6():
    band4.place(x=0, y=200, anchor="nw")
    resistor.ohms = 300
    resistor.update()
    resistor.show()
    about_panel.place_forget()
show_band6_button = Button(header_panel, text="6-Band Resistor", command=show_band6, font=("Arial", 12), bg="orange", height=1, width=16)
show_band6_button.place(x=330, y=168, anchor="nw")

def show_about_panel():
    about_panel.place(x=0, y=200, anchor="nw")
    resistor.hide()
    band4.place_forget()
show_about_panel_button = Button(header_panel, text="About", command=show_about_panel, font=("Arial", 12), bg="violet", height=1, width=16)
show_about_panel_button.place(x=836, y=168, anchor="nw")









window.mainloop()
