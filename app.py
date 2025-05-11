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
        self.ohms = -1
        self.tolerance = -1
        self.ppm = -1
        self.panel = Frame(container, bg="white", width=500, height=600)
        self.band_values = [-1,-1,-1,-1,-1,-1]

        self.band_colors_dict = {
            0: "black",
            1: "brown",
            2: "red",
            3: "orange",
            4: "yellow",
            5: "green",
            6: "blue",
            7: "violet",
            8: "gray",
            9: "white"
        }

        self.band_multipliers_dict = {
            1: "black",
            10: "brown",
            100: "red",
            1000: "orange",
            10000: "yellow",
            100000: "green",
            1000000: "blue",
            10000000: "violet",
            100000000: "gray",
            1000000000: "white",
            0.1: "gold",
            0.01: "silver"
        }

        self.band_tolerance_dict = {
            0.01: "brown",
            0.02: "red",
            0.005: "green",
            0.0025: "blue",
            0.001: "violet",
            0.0005: "gray",
            0.05: "gold",
            0.1: "silver"
        }

        self.band_ppm_dict = {
            100: "brown",
            50: "red",
            15: "orange",
            25: "yellow",
            10: "blue",
            5: "violet"
        }

        self.band_value_prefix_dict = {
            1000: "K",
            1000000: "M", 
            1000000000: "G",
        }


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


        # Resistor color bands
        self.band1 = Frame(self.resistor_head, bg="PeachPuff1", width=20, height=120)
        self.band1.place(x=30, y=0, anchor="nw")
        self.band2 = Frame(self.resistor_body, bg="PeachPuff1", width=20, height=120)
        self.band2.place(x=10, y=0, anchor="nw")
        self.band5 = Frame(self.resistor_body, bg="PeachPuff1", width=20, height=120)
        self.band5.place(x=70, y=0, anchor="nw")
        self.band3 = Frame(self.resistor_body, bg="PeachPuff1", width=20, height=120)
        self.band3.place(x=130, y=0, anchor="nw")
        self.band6 = Frame(self.resistor_body, bg="PeachPuff1", width=20, height=120)
        self.band6.place(x=190, y=0, anchor="nw")
        self.band4 = Frame(self.resistor_foot, bg="PeachPuff1", width=20, height=120)
        self.band4.place(x=30, y=0, anchor="nw")
        
    



        

    def update(self, mode):

        if mode == 'values':
            digit_arr = str(self.ohms).strip('0')
            c = len(digit_arr)
            mult = len(str(self.ohms))-len(digit_arr)

            if c > 3 or c == 0:
                raise ValueError("Invalid resistor value")
            if self.band == 4 and c > 2:
                raise ValueError("Invalid resistor value for 4-band resistor")

            if c == 1 and self.band == 4:
                mult -= 1
            if c == 1 and not self.band == 4:
                mult -= 2
            if c == 2 and not self.band == 4:
                mult -= 1

            # Helper function to safely get digit or 0 if out of bounds
            def safe_get(arr, index):
                return arr[index] if index < len(arr) else 0

            if self.band == 4:
                self.band_values = [
                    int(safe_get(digit_arr, 0)),
                    int(safe_get(digit_arr, 1)),
                    10**mult,
                    self.tolerance,
                    -1,
                    -1
                ]
            else:
                self.band_values = [
                    int(safe_get(digit_arr, 0)),
                    int(safe_get(digit_arr, 1)),
                    int(safe_get(digit_arr, 2)),
                    10**mult,
                    self.tolerance,
                    self.ppm
                ]



            print(self.band_values, self.band, mult)
            # if self.band == 4:
            #     if c == 1:


     

        
        
        if self.band == 4:
            self.band1.config(bg=self.band_colors_dict[self.band_values[0]] if self.band_values[0] != -1 else "PeachPuff1")
            self.band2.config(bg=self.band_colors_dict[self.band_values[1]] if self.band_values[1] != -1 else "PeachPuff1")
            self.band3.config(bg=self.band_multipliers_dict[self.band_values[2]] if self.band_values[2] != -1 else "PeachPuff1")
            self.band4.config(bg=self.band_tolerance_dict[self.band_values[3]] if self.band_values[3] != -1 else "PeachPuff1")
            self.band5.place_forget()
            self.band6.place_forget()

            self.ohms_temp = (self.band_values[0] * 10 + self.band_values[1]) * self.band_values[2]
            self.tolerance_temp = self.band_values[3]
            self.ppm_temp = -1

        if self.band == 5:
            self.band1.config(bg=self.band_colors_dict[self.band_values[0]] if self.band_values[0] != -1 else "PeachPuff1")
            self.band2.config(bg=self.band_colors_dict[self.band_values[1]] if self.band_values[1] != -1 else "PeachPuff1")
            self.band5.config(bg=self.band_colors_dict[self.band_values[2]] if self.band_values[2] != -1 else "PeachPuff1")
            self.band3.config(bg=self.band_multipliers_dict[self.band_values[3]] if self.band_values[3] != -1 else "PeachPuff1")
            self.band4.config(bg=self.band_tolerance_dict[self.band_values[4]] if self.band_values[4] != -1 else "PeachPuff1")
            self.band5.place(x=70, y=0, anchor="nw")
            self.band6.place_forget()

            self.ohms_temp = (self.band_values[0] * 100 + self.band_values[1] * 10 + self.band_values[2]) * self.band_values[3]
            self.tolerance_temp = self.band_values[4]
            self.ppm_temp = -1

        if self.band == 6:
            self.band1.config(bg=self.band_colors_dict[self.band_values[0]] if self.band_values[0] != -1 else "PeachPuff1")
            self.band2.config(bg=self.band_colors_dict[self.band_values[1]] if self.band_values[1] != -1 else "PeachPuff1")
            self.band5.config(bg=self.band_colors_dict[self.band_values[2]] if self.band_values[2] != -1 else "PeachPuff1")
            self.band3.config(bg=self.band_multipliers_dict[self.band_values[3]] if self.band_values[3] != -1 else "PeachPuff1")
            self.band6.config(bg=self.band_tolerance_dict[self.band_values[4]] if self.band_values[4] != -1 else "PeachPuff1")
            self.band4.config(bg=self.band_ppm_dict[self.band_values[5]] if self.band_values[5] != -1 else "PeachPuff1")
            self.band5.place(x=70, y=0, anchor="nw")
            self.band6.place(x=190, y=0, anchor="nw")

            self.ohms_temp = (self.band_values[0] * 100 + self.band_values[1] * 10 + self.band_values[2]) * self.band_values[3]
            self.tolerance_temp = self.band_values[4]
            self.ppm_temp = self.band_values[5]

        self.ohms_simplified = str(self.ohms_temp)
        for k in self.band_value_prefix_dict.keys():
            if self.ohms_temp/k > 1 and self.ohms/k < 1000:
                self.ohms_simplified = str(self.ohms_temp/k) + ' ' + self.band_value_prefix_dict[k]

        self.resistor_value.config(text=f"{self.ohms_simplified} Ohms {self.tolerance_temp*100}% Tolerance {'' if self.ppm_temp == -1 else (str(self.ppm_temp)+' PPM')}")

            


    def show(self):
        self.panel.place(x=500, y=200, anchor="nw")
        
        
    def hide(self):
        self.panel.place_forget()
            



# Create Resistor Object
resistor = Resistor(main_container)
resistor.show()

resistor.ohms = 11000
resistor.tolerance = 0.05
resistor.ppm = 10







############ Buttons ############
def show_band4():
    band4.place(x=0, y=200, anchor="nw")
    
    # resistor.band_values = [1,1,1000000000,0.05,-1,-1]
    resistor.band = 4

    resistor.update('values')
    resistor.show()
    about_panel.place_forget()
show_band4_button = Button(header_panel, text="4-Band Resistor", command=show_band4, font=("Arial", 12), bg="red", height=1, width=16)
show_band4_button.place(x=10, y=168, anchor="nw")

def show_band5():
    band4.place(x=0, y=200, anchor="nw")
    
    # resistor.band_values = [1,2,3,100000,0.05,-1]
    resistor.band = 5
    
    resistor.update('values')
    resistor.show()
    about_panel.place_forget()
show_band5_button = Button(header_panel, text="5-Band Resistor", command=show_band5, font=("Arial", 12), bg="yellow", height=1, width=16)
show_band5_button.place(x=170, y=168, anchor="nw")

def show_band6():
    band4.place(x=0, y=200, anchor="nw")

    # resistor.band_values = [1,2,3,100000,0.05,10]
    resistor.band = 6

    resistor.update('values')
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
