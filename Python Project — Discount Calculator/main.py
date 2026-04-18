import tkinter as tk

#calculation function
def run_calculation():
    try:
        # get values from the input boxes
        # .get() reads the current text as a string, float() converts to a number
        orig_price_raw = float(entry_price.get())
        disc_rate_raw = float(entry_discount.get())

        # perform the math
        final_amount = orig_price_raw * (1.0 - (disc_rate_raw / 100.0))

        # update the result label
        lbl_result.config(text=f"Final Price: Rp. {final_amount:.2f}")

    except ValueError:
        # error handling for non-numeric input
        lbl_result.config(text="Error: Please enter numbers only.")

# window setup
app_window = tk.Tk()
app_window.title("Discount Calculator")  
app_window.geometry("260x220")         

# original price input
lbl_price = tk.Label(app_window, text="Original Price:")
lbl_price.pack(pady=(20, 0))  
entry_price = tk.Entry(app_window)
entry_price.pack()

# discount input
lbl_discount = tk.Label(app_window, text="Discount (%):")
lbl_discount.pack(pady=(10, 0))
entry_discount = tk.Entry(app_window)  
entry_discount.pack()

# calculate button
btn_calculate = tk.Button(app_window, text="Calculate", command=run_calculation)
btn_calculate.pack(pady=15)

# final price result display
lbl_result = tk.Label(app_window, text="Final Price: ")
lbl_result.pack()

# start the application
app_window.mainloop()
