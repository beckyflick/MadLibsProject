import tkinter as tk
window= tk.Tk()
window.title("Mad Libs")
label1= tk.Label(
    window, 
    text= "Enter words below:",
    foreground= "white",
    background= "purple",
    width= 20, 
    height= 2
)
label1.pack()

frame1= tk.Frame(window, bg="white", relief=tk.RAISED, borderwidth=25)
frame1.pack()

window.mainloop()