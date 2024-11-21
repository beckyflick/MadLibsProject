import tkinter as tk
window= tk.Tk()
window.title("Mad Libs")

def hidden_story(widget):
    widget.pack_forget()
def show_story(widget):
    widget.pack()

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

noun1_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

noun1_entry.insert(0,"Noun:")
noun1_entry.pack()

verb1_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

verb1_entry.insert(0, "Verb ending in -ing:")
verb1_entry.pack()

adjective1_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

adjective1_entry.insert(0, "Adjective:")
adjective1_entry.pack()

fam_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

fam_entry.insert(0, "Family Member:")
fam_entry.pack()

verb2_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

verb2_entry.insert(0, "Verb:")
verb2_entry.pack()

ing_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

ing_entry.insert(0, "Ingredient:")
ing_entry.pack()

noun2_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

noun2_entry.insert(0, "Noun:")
noun2_entry.pack()

noun3_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

noun3_entry.insert(0, "Noun:")
noun3_entry.pack()

noun4_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")
noun4_entry.insert(0, "Noun:")
noun4_entry.pack()


noun5_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

noun5_entry.insert(0, "Noun:")
noun5_entry.pack()


noun6_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

noun6_entry.insert(0, "Noun:")
noun6_entry.pack()

verb3_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

verb3_entry.insert(0, "Verb:")
verb3_entry.pack()

noun7_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

noun7_entry.insert(0, "Noun:")
noun7_entry.pack()

num1_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

num1_entry.insert(0, "Number:")
num1_entry.pack()

num2_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

num2_entry.insert(0, "Number:")
num2_entry.pack()

noun8_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

noun8_entry.insert(0, "Noun:")
noun8_entry.pack()

def hide_label():
   label1.pack_forget()
   noun1_entry.pack_forget()
   noun2_entry.pack_forget()
   noun3_entry.pack_forget()
   noun4_entry.pack_forget()
   noun5_entry.pack_forget()
   noun6_entry.pack_forget()
   noun7_entry.pack_forget()
   noun8_entry.pack_forget()
   verb1_entry.pack_forget()
   verb2_entry.pack_forget()
   verb3_entry.pack_forget()
   adjective1_entry.pack_forget()
   ing_entry.pack_forget()
   num1_entry.pack_forget()
   num2_entry.pack_forget()
   fam_entry.pack_forget()

def storytime():
    print(f"Every year, {noun1_entry} we make at Christmas time.\n{verb1_entry} has been a tradition since I was a/an {adjective1_entry} kid!\n{fam_entry} used to make most of the recipe back then, but I would always help {verb2_entry} {ing_entry}.\n Now that I'm older, I make the entire batch of {noun2_entry} from scratch.\n All you have to do is mix {noun3_entry} and {noun4_entry} in a bowl until fluffy, and add {noun5_entry}.\n Don't forget the {noun6_entry}! {verb3_entry} them on a {noun7_entry} and bake them at a {num1_entry} degrees.\n After {num2_entry} minutes, you will have the perfect {noun8_entry}!")  

story= tk.Label(window, bg="white", width= 50, height=50, text=storytime())
hidden_story(story)

button=tk.Button(
    window,
    text = "Submit",
    fg="white",
    bg= "purple",
    width = 10,
    height = 2, 
    command=hide_label()
    )
button.pack()

show_story(story)


window.mainloop()