from tkinter import *
PADX = 0
FONT = "Arial"

def convert_miles_to_km():
    miles = input_user.get()
    km = round((1.60934 * float(miles)), 2)
    label_4.config(text=km)


window = Tk()
window.title("Mile to km Converter")
window.minsize()
window.config(padx=70, pady=50)

# Label_1
label_1 = Label(text="miles", font=(FONT, 14))
label_1.grid(column=2, row=0)
label_1.config(padx=PADX, pady=PADX)

# Label_2
label_2 = Label(text="is equal to", font=(FONT, 14))
label_2.grid(column=0, row=1)
label_2.config(padx=PADX, pady=PADX)

# Label_3
label_3 = Label(text="km", font=(FONT, 14))
label_3.grid(column=2, row=1)
label_3.config(padx=PADX, pady=PADX)

# input miles
input_user = Entry(width=20, text="Enter miles")
input_user.get()
input_user.grid(column=1, row=0)


# label_4 = Output miles in km
label_4 = Label(text="", font=(FONT, 14))
label_4.grid(column=1, row=1)
label_4.config(padx=PADX, pady=PADX)

# Button Calculate
button_calculate = Button(text="Calculate", command=convert_miles_to_km)
button_calculate.grid(column=1, row=2)

window.mainloop()
