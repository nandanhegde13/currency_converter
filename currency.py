from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dict import *

root = Tk()
root.geometry("500x500")
root.title("Currency Converter")
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

currency_frame = Frame(my_notebook, width=480, height=480)
conversion_frame = Frame(my_notebook, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(conversion_frame, text="Convert")

# disable second tab

my_notebook.tab(1, state="disabled")


##################
# currency
##################

def lock():
    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning("WARNING!", "you should fill all the fields")


    else:

        home_name = home_entry.get().lower()
        conversion_name = conversion_entry.get().lower()

        try:
            if not dic[home_name] or not dic[conversion_name]:
                my_notebook.tab(1, state="disabled")
                # my_notebook.tab(1, state="disabled")

        except KeyError:
            messagebox.showwarning("WARNING!", "Please enter correct currency name")
        else:
            my_notebook.tab(1, state="disabled")

            home_entry.config(state="disabled")
            conversion_entry.config(state="disabled")
            rate_entry.config(state="disabled")

            my_notebook.tab(1, state="normal")
            amount_label.config(text=f"amount of {home_entry.get()} To convert to {conversion_entry.get()}")
            converted_label.config(text=f'Equals This many {conversion_entry.get()}')
            convert_button.config(text=f"convert from {home_entry.get()}")


def unlock():
    home_entry.config(state="normal")
    conversion_entry.config(state="normal")
    rate_entry.config(state="normal")

    my_notebook.tab(1, state="disabled")


home = LabelFrame(currency_frame, text="Your home currency")
home.pack(pady=20)

home_entry = Entry(home, font=("helvetica", 24))
home_entry.pack(padx=10, pady=10)

conversion = LabelFrame(currency_frame, text="Currency you want to convert")
conversion.pack(pady=20)

conversion_label = Label(conversion, text="Currency to  convert to")
conversion_label.pack(pady=10)

conversion_entry = Entry(conversion, font=("helvetica", 24))
conversion_entry.pack(pady=10, padx=10)

rate_label = Label(conversion, text="Conversion rate")
rate_label.pack(pady=10)

rate_entry = Entry(conversion, font=("helvetica", 24))
rate_entry.pack(pady=10, padx=10)

button_frame = Frame(currency_frame)
button_frame.pack(pady=20)

lock_button = Button(button_frame, text="Lock", command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="Unlock", command=unlock)
unlock_button.grid(row=0, column=1, padx=10)


#############
# conversion frame
#############


def convert():
    con_currency = conversion_entry.get().lower()
    symbol = dic[con_currency]

    # adding symbol to input
    home_currency = home_entry.get().lower()
    home_currency_symbol = dic[home_currency]



    converted_entry.delete(0, END)

    final = float(rate_entry.get()) * float(amount_entry.get())

    final = round(final, 2)

    final = '{:,}'.format(final)

    converted_entry.insert(0, f'{symbol} {final}')

    input_currency = str(amount_entry.get())
    amount_entry.delete(0, END)
    amount_entry.insert(0, f'{home_currency_symbol} {input_currency}')


def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)


amount_label = LabelFrame(conversion_frame, text="Amount of US ")
amount_label.pack(pady=20)

amount_entry = Entry(amount_label, font=("helvetica", 24))
amount_entry.pack(pady=10, padx=10)

convert_button = Button(amount_label, text="convert", command=convert)
convert_button.pack(pady=10)

converted_label = LabelFrame(conversion_frame, text="Converted Currency")
converted_label.pack(pady=20)

converted_entry = Entry(converted_label, font=("Helvetica", 24), bd=0, bg="systembuttonface")
converted_entry.pack(pady=10, padx=10)

clear = Button(conversion_frame, text="clear", command=clear)
clear.pack(pady=20)

spacer = Label(conversion_frame, text="", width=68)
spacer.pack()

root.mainloop()
