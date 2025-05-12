from tkinter import *
from tkinter import ttk as TTK

# Create a window
window = Tk()
# Set window properties
window.title("Resistor Color Code")
window.minsize(1000, 800)

# Main container to hold all the panels for each resistor band
main_container = Frame(window, bg="SteelBlue2", width=1000, height=800)
main_container.place(relx=0.5, rely=0.5, anchor="center")



########## Header panel ##########
header_panel = Frame(main_container, bg="SteelBlue1", width=1000, height=200)
header_panel.place(x=0, y=0, anchor="nw")

# Title Label
title_label = Label(header_panel, text="Resistor Color Code", font=("Arial bold", 24), bg="SteelBlue1", fg="white") 
title_label.place(relx=0.5, y=50, anchor="center")
########## Header panel ##########



# Resistor band panels
band4 = Frame(main_container, bg="RoyalBlue3", width=500, height=600)
band4.place(x=0, y=200, anchor="nw")
# about_panel = Frame(main_container, bg="SteelBlue", width=1000, height=600)



############# Resistor ############

# band library

class Resistor:

    def __init__(self, container):
        self.band = 4
        self.ohms = -1
        self.tolerance = -1
        self.ppm = -1
        self.panel = Frame(container, bg="DodgerBlue3", width=500, height=600)
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


        self.resistor_container = Frame(self.panel, bg="DodgerBlue3", width=400, height=120)
        self.resistor_label = Label(self.panel, text="Resistor Value:", font=("Arial bold", 16), bg="DodgerBlue3", fg="white")
        self.resistor_value = Label(self.panel, text=f"-", font=("Arial bold", 16), bg="DodgerBlue3", fg="white")
    
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
        
    def update(self, mode = "band"):
        try:
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
            
            if self.band_values[0] == -1:
                raise ValueError("Error")


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
                if (self.ohms_temp/k > 1 and self.ohms_temp/k < 1000) or self.ohms_temp/k == 1:
                    self.ohms_simplified = str(self.ohms_temp/k) + ' ' + self.band_value_prefix_dict[k]
            self.resistor_value.config(text=f"{self.ohms_simplified} Ohms {self.tolerance_temp*100}% Tolerance {'' if self.ppm_temp == -1 else (str(self.ppm_temp)+' PPM')}")
        except Exception as e:
            if str(e) == "Invalid resistor value for 4-band resistor" or str(e) == "Invalid resistor value":
                self.resistor_value.config(text="Error: "+str(e))
            else:
                self.resistor_value.config(text="-")
    
    def show(self):
        self.panel.place(x=500, y=200, anchor="nw")
        
    def hide(self):
        self.panel.place_forget()
            



# Create Resistor Object
resistor = Resistor(main_container)
resistor.show()

class InputField:

    def __init__(self, container):
        self.panel = Frame(container, bg="DodgerBlue3", width=500, height=600)
        self.input_container = Frame(self.panel, bg="DodgerBlue4", width=420, height=570)
        self.input_container.place(relx=0.5,rely=0.5, anchor="center")

        resistance_label = Label(self.input_container, text="Resistance", font=("Arial bold", 12), fg="black") 
        resistance_label.place(x=10,y=20,anchor='nw')

        self.res=StringVar()
        self.resistance_entry = Entry(self.input_container,textvariable = self.res, font=('calibre',16, 'bold'), width=12)
        self.resistance_entry.place(x=10,y=50,anchor='nw')

        tolerance_label = Label(self.input_container, text="Tolerance (%)", font=("Arial bold", 12), fg="black") 
        tolerance_label.place(x=180,y=20,anchor='nw')

        self.tol=StringVar()
        self.tolerance_entry = Entry(self.input_container,textvariable = self.tol, font=('calibre',16, 'bold'), width=10)
        self.tolerance_entry.place(x=180,y=50,anchor='nw')

        ppm_label = Label(self.input_container, text="PPM", font=("Arial bold", 12), fg="black") 
        ppm_label.place(x=325,y=20,anchor='nw')

        self.p=StringVar()
        self.ppm_entry = Entry(self.input_container,textvariable = self.p, font=('calibre',16, 'bold'), width=6)
        self.ppm_entry.place(x=325,y=50,anchor='nw')

        self.value_list =  ("0 - Black",
            "1 - Brown",
            "2 - Red",
            "3 - Orange",
            "4 - Yellow",
            "5 - Green",
            "6 - Blue",
            "7 - Violet",
            "8 - Gray",
            "9 - White")
        
        self.multiplier_list = ("1 - Black",
            "10 - Brown",
            "100 - Red",
            "1000 - Orange",
            "10000 - Yellow",
            "100000 - Green",
            "1000000 - Blue",
            "10000000 - Violet",
            "100000000 - Gray",
            "1000000000 - White",
            "0.1 - Gold",
            "0.01 - Silver")
        
        self.tolerance_list = ("0.01 - Brown",
            "0.02 - Red",
            "0.005 - Green",
            "0.0025 - Blue",
            "0.001 - Violet",
            "0.0005 - Gray",
            "0.05 - Gold",
            "0.1 - Silver")
        
        self.ppm_list = ("100 - brown",
            "50 - red",
            "15 - orange",
            "25 - yellow",
            "10 - blue",
            "5 - violet")

        self.label1 = Label(self.input_container, text="Band 1 Color", font=("Arial bold", 12), fg="black") 
        self.label1.place(x=10,y=90,anchor='nw')
        self.e1=StringVar()
        self.entry1 = TTK.Combobox(self.input_container,textvariable = self.e1, font=('calibre',16, 'bold'), width=31)
        self.entry1.place(x=10,y=120,anchor='nw')
        self.entry1['values'] = self.value_list
        
        self.label2 = Label(self.input_container, text="Band 2 Color", font=("Arial bold", 12), fg="black") 
        self.label2.place(x=10,y=160,anchor='nw')
        self.e2=StringVar()
        self.entry2 = TTK.Combobox(self.input_container,textvariable = self.e2, font=('calibre',16, 'bold'), width=31)
        self.entry2.place(x=10,y=190,anchor='nw')
        self.entry2['values'] = self.value_list
        
        self.label3 = Label(self.input_container, text="Band 3 Color", font=("Arial bold", 12), fg="black") 
        self.label3.place(x=10,y=230,anchor='nw')
        self.e3=StringVar()
        self.entry3 = TTK.Combobox(self.input_container,textvariable = self.e3, font=('calibre',16, 'bold'), width=31)
        self.entry3.place(x=10,y=260,anchor='nw')
        self.entry3['values'] = self.multiplier_list 
        
        self.label4 = Label(self.input_container, text="Band 4 Color", font=("Arial bold", 12), fg="black") 
        self.label4.place(x=10,y=300,anchor='nw')
        self.e4=StringVar()
        self.entry4 = TTK.Combobox(self.input_container,textvariable = self.e4, font=('calibre',16, 'bold'), width=31)
        self.entry4.place(x=10,y=330,anchor='nw')
        self.entry4['values'] =  self.tolerance_list
        
        self.label5 = Label(self.input_container, text="Band 5 Color", font=("Arial bold", 12), fg="black") 
        # label5.place(x=10,y=370,anchor='nw')
        self.e5=StringVar()
        self.entry5 = TTK.Combobox(self.input_container,textvariable = self.e5, font=('calibre',16, 'bold'), width=31)
        # self.entry5.place(x=10,y=400,anchor='nw')
        # self.entry5['values'] = ("0 - black",
        #     "1 - Brown",
        #     "2 - Red",
        #     "3 - Orange",
        #     "4 - Yellow",
        #     "5 - Green",
        #     "6 - Blue",
        #     "7 - Violet",
        #     "8 - Gray",
        #     "9 - White") 
        
        self.label6 = Label(self.input_container, text="Band 6 Color", font=("Arial bold", 12), fg="black") 
        # label6.place(x=10,y=440,anchor='nw')
        self.e6=StringVar()
        self.entry6 = TTK.Combobox(self.input_container,textvariable = self.e6, font=('calibre',16, 'bold'), width=31)
        # self.entry6.place(x=10,y=470,anchor='nw')
        # self.entry6['values'] = ("100 - Brown",
        #     "50 - Red",
        #     "15 - Orange",
        #     "25 - Yellow",
        #     "10 - Blue",
        #     "5 - Violet") 
        

        
        self.clear_button = Button(self.input_container, text="Clear", command=self.clear_all, font=("Arial", 12), bg="white", height=1, width=16)
        self.clear_button.place(relx=0.25, y=540, anchor="center")

        self.submit_button = Button(self.input_container, text="Enter", command=self.submit, font=("Arial", 12), bg="white", height=1, width=16)
        self.submit_button.place(relx=0.75, y=540, anchor="center")

    def clear_dropdown(self):
        self.e1.set("")
        self.e2.set("")
        self.e3.set("")
        self.e4.set("")
        self.e5.set("")
        self.e6.set("")

    def clear_all(self):
        self.e1.set("")
        self.e2.set("")
        self.e3.set("")
        self.e4.set("")
        self.e5.set("")
        self.e6.set("")
        self.res.set("")
        self.tol.set("")
        self.p.set("")
        
    
    def submit(self):
        m = 'values'
        
        try:
            if not self.res.get() == "":
                resistor.ohms = int(self.res.get())
                resistor.tolerance = float(self.tol.get())/100

                self.clear_dropdown()
            else:
                def safe_number(value):
                    try:
                        part = value.split('-')[0].strip()
                        if not part:
                            return -1
                        number = float(part)
                        return int(number) if number.is_integer() else number
                    except (ValueError, AttributeError):
                        return -1
                v1 = safe_number(self.e1.get().split('-')[0].strip())
                v2 = safe_number(self.e2.get().split('-')[0].strip())
                v3 = safe_number(self.e3.get().split('-')[0].strip())
                v4 = safe_number(self.e4.get().split('-')[0].strip())
                v5 = safe_number(self.e5.get().split('-')[0].strip())
                v6 = safe_number(self.e6.get().split('-')[0].strip())
                # print(v1,v2,v3,v4,v5,v6)
                resistor.band_values = [v1,v2,v3,v4,v5,v6]
                m = 'band'
            
        except Exception as e:
            resistor.ohms = 0
            resistor.tolerance = 0
        try:
            resistor.ppm = float(self.p.get())
        except Exception as e:
            resistor.ppm = -1
        resistor.update(m)
        resistor.show()

    


    def show(self, band):
        self.panel.place(x=0, y=200, anchor="nw")

        if band == 4:
            self.entry1.place(x=10,y=120,anchor='nw')
            self.entry1['values'] = self.value_list

            self.entry2.place(x=10,y=190,anchor='nw')
            self.entry2['values'] = self.value_list
            
            self.entry3.place(x=10,y=260,anchor='nw')
            self.entry3['values'] = self.multiplier_list 

            self.entry4.place(x=10,y=330,anchor='nw')
            self.entry4['values'] =  self.tolerance_list

            self.label5.place_forget()
            self.entry5.place_forget()
            self.label6.place_forget()
            self.entry6.place_forget()
        elif band == 5:
            self.entry1.place(x=10,y=120,anchor='nw')
            self.entry1['values'] = self.value_list

            self.entry2.place(x=10,y=190,anchor='nw')
            self.entry2['values'] = self.value_list
            
            self.entry3.place(x=10,y=260,anchor='nw')
            self.entry3['values'] = self.value_list 

            self.entry4.place(x=10,y=330,anchor='nw')
            self.entry4['values'] =  self.multiplier_list

            self.label5.place(x=10,y=370,anchor='nw')
            self.entry5.place(x=10,y=400,anchor='nw')
            self.entry5['values'] =  self.tolerance_list

            self.label6.place_forget()
            self.entry6.place_forget()
        elif band == 6:
            self.entry1.place(x=10,y=120,anchor='nw')
            self.entry1['values'] = self.value_list

            self.entry2.place(x=10,y=190,anchor='nw')
            self.entry2['values'] = self.value_list
            
            self.entry3.place(x=10,y=260,anchor='nw')
            self.entry3['values'] = self.value_list 

            self.entry4.place(x=10,y=330,anchor='nw')
            self.entry4['values'] =  self.multiplier_list

            self.entry5.place(x=10,y=400,anchor='nw')
            self.entry5['values'] =  self.tolerance_list

            self.label6.place(x=10,y=440,anchor='nw')
            self.entry6.place(x=10,y=470,anchor='nw')
            self.entry6['values'] =  self.ppm_list
    


        
    def hide(self):
        self.panel.place_forget()


input_field = InputField(main_container)
input_field.show(4)


############ Buttons ############
def show_band4():
    band4.place(x=0, y=200, anchor="nw")
    
    resistor.band_values = [-1,-1,-1,-1,-1,-1]
    resistor.band = 4

    input_field.show(4)
    input_field.clear_dropdown()
    resistor.update('values')
    resistor.show()
    # about_panel.place_forget()
show_band4_button = Button(header_panel, text="4-Band Resistor", command=show_band4, font=("Arial", 12), bg="SteelBlue2", fg= "white" , height=1, width=16)
show_band4_button.place(x=10, y=168, anchor="nw")

def show_band5():
    band4.place(x=0, y=200, anchor="nw")
    
    resistor.band_values = [-1,-1,-1,-1,-1,-1]
    resistor.band = 5

    input_field.show(5)
    input_field.clear_dropdown()
    resistor.update('values')
    resistor.show()
    # about_panel.place_forget()
show_band5_button = Button(header_panel, text="5-Band Resistor", command=show_band5, font=("Arial", 12), bg="SteelBlue3", fg= "white", height=1, width=16)
show_band5_button.place(x=170, y=168, anchor="nw")

def show_band6():
    band4.place(x=0, y=200, anchor="nw")

    resistor.band_values = [-1,-1,-1,-1,-1,-1]
    resistor.band = 6

    input_field.show(6)
    input_field.clear_dropdown()
    resistor.update('values')
    resistor.show()
    # about_panel.place_forget()
show_band6_button = Button(header_panel, text="6-Band Resistor", command=show_band6, font=("Arial", 12), bg="SteelBlue4", fg= "white", height=1, width=16)
show_band6_button.place(x=330, y=168, anchor="nw")

def show_about_panel():
    # about_panel.place(x=0, y=200, anchor="nw")
    # resistor.hide()
    # band4.place_forget()

    about_win = Toplevel(window)
    about_win.title("About")
    about_win.geometry("300x280")
    about_win.resizable(False, False)

    # Optional: make sure it stays on top
    about_win.transient(window)
    about_win.grab_set()

    # Content
    Label(about_win, text="Resistor Color Code", font=("Arial", 16, "bold")).pack(pady=10)
    Label(about_win, text="Version 1.0.0").pack(pady=5)
    Label(about_win, text="Developed by A. Aquino, G.R. Demate, N. Jacinto,").pack(pady=5)
    Label(about_win, text="J. Manlapaz, R. Postrero, C.M. Amora").pack(pady=5)
    Label(about_win, text="").pack(pady=5)
    Label(about_win, text="© 2025 All rights reserved").pack(pady=5)

    Button(about_win, text="OK", command=about_win.destroy).pack(pady=15)

show_about_panel_button = Button(header_panel, text="About", command=show_about_panel, font=("Arial", 12), bg="DodgerBlue3", fg = "white", height=1, width=16)
show_about_panel_button.place(x=836, y=168, anchor="nw")




window.mainloop()
