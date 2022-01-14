import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=50, height=20)
window.config(padx=10, pady=10)

def button_clicked():
     content = float(input.get())
     result.config(text=round(content * 1.660934))

#Entry
input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

#miles
miles_label = tkinter.Label(text="Miles ", font=("Arial", 10))
miles_label.grid(column=2, row=0)
miles_label.config(pady=10, padx=10)

#is equal to
miles_label = tkinter.Label(text="is equal to", font=("Arial", 10))
miles_label.grid(column=0, row=1)

#result
result = tkinter.Label(text="0", font=("Arial", 14, "bold"))
result.grid(column=1, row=1)

#Km
km = tkinter.Label(text="Km", font=("Arial", 10))
km.grid(column=2, row=1)

#Button
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
