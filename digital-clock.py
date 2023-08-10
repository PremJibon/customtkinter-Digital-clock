import customtkinter
from time import strftime

root = customtkinter.CTk()
root.title("Digital Clock")

def time():
    string = strftime("%H:%M:%S %p")
    clock_lbl.configure(text=string)
    clock_lbl.after(1000,time)


clock_lbl = customtkinter.CTkLabel(root,font=("ds-digital",80),
                                   fg_color='purple',
                                   text_color='white')
clock_lbl.grid(padx=10,pady=10)

time()

root.mainloop()