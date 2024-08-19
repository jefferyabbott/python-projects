from tkinter import *


def convert_miles_to_km():
    miles = text_input.get()
    if float(miles) > 0:
        output["text"] = f"{1.6 * float(miles):.2f}"


# window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# text input
text_input = Entry(width=10)
text_input.grid(column=1, row=0)
text_input.focus()

# text input label
text_input_label = Label(text="Miles")
text_input_label.grid(column=2, row=0)

# label is equal to
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

# label output
output = Label()
output.config(width=10)
output.grid(column=1, row=1)

# label Km
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# calculate button
calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)

# keep window alive
window.mainloop()