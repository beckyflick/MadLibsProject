import tkinter as tk
window= tk.Tk()
window.title("Mad Libs")

def hidden_story(widget):
    widget.pack_forget()
def show_story(widget):
    widget.pack()
    

def main():
    hide_label()
    #add a loop here to call each function grabbing the text here so taht we put the text in after we close the window
    #loop thru and find() the ":" and then grab that text [#:] so that it goes until the end
    storytime()
    show_story()



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
noun1= noun1_entry.get()
full_noun= noun1[5:]
#figure out how to grab the text that is put in but not list the Noun: label

verb1_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

verb1_entry.insert(0, "Verb ending in -ing:")
verb1_entry.pack()
verb1= verb1_entry.get()

adjective1_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

adjective1_entry.insert(0, "Adjective:")
adjective1_entry.pack()
adjective1= adjective1_entry.get()

fam_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

fam_entry.insert(0, "Family Member:")
fam_entry.pack()
fam=fam_entry.get()

verb2_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

verb2_entry.insert(0, "Verb:")
verb2_entry.pack()
verb2= verb2_entry.get()

ing_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

ing_entry.insert(0, "Ingredient:")
ing_entry.pack()
ing=ing_entry.get()

noun2_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

noun2_entry.insert(0, "Noun:")
noun2_entry.pack()
noun2= noun2_entry.get()

noun3_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

noun3_entry.insert(0, "Noun:")
noun3_entry.pack()
noun3= noun3_entry.get()

noun4_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")
noun4_entry.insert(0, "Noun:")
noun4_entry.pack()
noun4= noun4_entry.get()

noun5_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

noun5_entry.insert(0, "Noun:")
noun5_entry.pack()
noun5= noun5_entry.get()

noun6_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

noun6_entry.insert(0, "Noun:")
noun6_entry.pack()
noun6= noun6_entry.get()

verb3_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

verb3_entry.insert(0, "Verb:")
verb3_entry.pack()
verb3= verb3_entry.get()

noun7_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

noun7_entry.insert(0, "Noun:")
noun7_entry.pack()
noun7= noun7_entry.get()

num1_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

num1_entry.insert(0, "Number:")
num1_entry.pack()
num1= num1_entry.get()

num2_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

num2_entry.insert(0, "Number:")
num2_entry.pack()
num2= num2_entry.get()

noun8_entry=tk.Entry(
    window,
    fg = "purple",
    bg = "white")

noun8_entry.insert(0, "Noun:")
noun8_entry.pack()
noun8= noun8_entry.get()

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
    text_box = tk.Text()
    text_box.pack()
    text_box.insert("1.0", string())

def string():
    return (f"Every year, {full_noun} we make at Christmas time.\n{verb1} has been a tradition since I was a/an {adjective1} kid!\n{fam} used to make most of the recipe back then, but I would always help {verb2} {ing}.\n Now that I'm older, I make the entire batch of {noun2} from scratch.\n All you have to do is mix {noun3} and {noun4} in a bowl until fluffy, and add {noun5}.\n Don't forget the {noun6}! {verb3} them on a {noun7} and bake them at a {num1} degrees.\n After {num2} minutes, you will have the perfect {noun8}!")
   

# story=tk.Label(window, bg="white", width= 50, height=50, text= storytime)
# hidden_story(story)

button=tk.Button(
    window,
    text = "Submit",
    fg="white",
    bg= "purple",
    width = 10,
    height = 2, 
    command= main
    )
button.pack()





window.mainloop()