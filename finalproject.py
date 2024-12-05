#to do:
    #make sure have something from every week (logic week)
    #finish f string piece
    #text to speech
    #solidify what 3 we are presenting on/who will present what 

import tkinter as tk
window= tk.Tk()
window.title("Mad Libs")

# def hidden_story(widget):
#     widget.pack_forget()
# def show_story(widget):
#     widget.pack()
    

def main():
    for x in list:
        x.pack_forget()
    
    full_line=noun1_entry.get()
    global noun1
    noun1=full_line[5:]

    line_v1=verb1_entry.get()
    global verb1
    verb1=line_v1[20:]

    line_adj1=adjective1_entry.get()
    global adjective1
    adjective1=line_adj1[10:]

    line_fam=fam_entry.get()
    global fam
    fam=line_fam[14:]

    line_v2=verb2_entry.get()
    global verb2
    verb2=line_v2[5:]   
    
    line_ing=ing_entry.get()
    global ing
    ing=line_ing[11:]

    line_n2=noun2_entry.get()
    global noun2
    noun2=line_n2[5:]

    line_n3=noun3_entry.get()
    global noun3
    noun3=line_n3[5:]

    line_n4=noun4_entry.get()
    global noun4
    noun4=line_n4[5:]

    line_n5=noun5_entry.get()
    global noun5
    noun5=line_n5[5:]

    line_n6=noun6_entry.get()
    global noun6
    noun6=line_n6[5:]

    line_v3=verb3_entry.get()
    global verb3
    verb3=line_v3[5:]

    line_n7=noun7_entry.get()
    global noun7
    noun7=line_n7[5:]

    line_num1=num1_entry.get()
    global num1
    num1=line_num1[7:]

    line_num2=num2_entry.get()
    global num2
    num2=line_num2[7:]

    line_n8=noun8_entry.get()
    global noun8
    noun8=line_n8[5:]

    # storytext=text_box.get()


    
#repeat what is above for every entry and have it print in f string below

    storytime()
    # show_story()



label1= tk.Label(
    window, 
    text= "Enter words below:",
    foreground= "white",
    background= "red",
    width= 20, 
    height= 2
)
label1.pack()

frame1= tk.Frame(window, bg="white", relief=tk.RAISED, borderwidth=25)
frame1.pack()

noun1_entry=tk.Entry(
    window,
    fg = "green",
    bg = "white")

noun1_entry.insert(0,"Noun:")
noun1_entry.pack()


#figure out how to grab the text that is put in but not list the Noun: label

verb1_entry=tk.Entry(
    window,
    fg = "green",
    bg = "white")

verb1_entry.insert(0, "Verb ending in -ing:")
verb1_entry.pack()
verb1= verb1_entry.get()

adjective1_entry=tk.Entry(
    window,
    fg = "green",
    bg = "white")

adjective1_entry.insert(0, "Adjective:")
adjective1_entry.pack()
adjective1= adjective1_entry.get()

fam_entry=tk.Entry(
    window,
    fg = "green",
    bg = "white")

fam_entry.insert(0, "Family Member:")
fam_entry.pack()
fam=fam_entry.get()

verb2_entry=tk.Entry(
    window,
    fg = "green",
    bg = "white")

verb2_entry.insert(0, "Verb:")
verb2_entry.pack()
verb2= verb2_entry.get()

ing_entry=tk.Entry(
    window,
    fg = "green",
    bg = "white")

ing_entry.insert(0, "Ingredient:")
ing_entry.pack()
ing=ing_entry.get()

noun2_entry=tk.Entry(
    window,
    fg = "green",
    bg = "white")

noun2_entry.insert(0, "Noun:")
noun2_entry.pack()
noun2= noun2_entry.get()

noun3_entry=tk.Entry(
    window,
    fg = "green",
    bg = "white")

noun3_entry.insert(0, "Noun:")
noun3_entry.pack()
noun3= noun3_entry.get()

noun4_entry=tk.Entry(
    window,
    fg = "green",
    bg = "white")
noun4_entry.insert(0, "Noun:")
noun4_entry.pack()
noun4= noun4_entry.get()

noun5_entry=tk.Entry(
    window,
    fg = "green",
    bg = "white")

noun5_entry.insert(0, "Noun:")
noun5_entry.pack()
noun5= noun5_entry.get()

noun6_entry=tk.Entry(
    window,
    fg = "green",
    bg = "white")

noun6_entry.insert(0, "Noun:")
noun6_entry.pack()
noun6= noun6_entry.get()

verb3_entry=tk.Entry(
    window,
    fg = "green",
    bg = "white")

verb3_entry.insert(0, "Verb:")
verb3_entry.pack()
verb3= verb3_entry.get()

noun7_entry=tk.Entry(
    window,
    fg = "green",
    bg = "white")

noun7_entry.insert(0, "Noun:")
noun7_entry.pack()
noun7= noun7_entry.get()

num1_entry=tk.Entry(
    window,
    fg = "green",
    bg = "white")

num1_entry.insert(0, "Number:")
num1_entry.pack()
num1= num1_entry.get()

num2_entry=tk.Entry(
    window,
    fg = "green",
    bg = "white")

num2_entry.insert(0, "Number:")
num2_entry.pack()
num2= num2_entry.get()

noun8_entry=tk.Entry(
    window,
    fg = "green",
    bg = "white")

noun8_entry.insert(0, "Noun:")
noun8_entry.pack()
noun8= noun8_entry.get()

def storytime():
    global text_box
    text_box = tk.Text(width=100)
    text_box.pack()
    text_box.insert("1.0", string())

def string():
    return (f"Every year, {noun1} we make at Christmas time.\n{verb1} has been a tradition since I was a/an {adjective1} kid!\n{fam} used to make most of the recipe back then, but I would always help {verb2} {ing}.\nNow that I'm older, I make the entire batch of {noun2} from scratch.\nAll you have to do is mix {noun3} and {noun4} in a bowl until fluffy, and add {noun5}.\nDon't forget the {noun6}! {verb3} them on a {noun7} and bake them at a {num1} degrees.\nAfter {num2} minutes, you will have the perfect {noun8}!")
   

# story=tk.Label(window, bg="white", width= 50, height=50, text= storytime)
# hidden_story(story)

button=tk.Button(
    window,
    text = "Submit",
    fg="white",
    bg= "red",
    width = 10,
    height = 2, 
    command= main
    )
button.pack()

list=[label1, button, noun1_entry, noun2_entry, noun3_entry, noun4_entry, noun5_entry, noun6_entry, noun7_entry, noun8_entry, verb1_entry, verb2_entry, verb3_entry, adjective1_entry, ing_entry, num1_entry, num2_entry, fam_entry]


# #FOR THE TEXT TO SPEECH
# from gtts import gTTS
# mytext = 'Welcome to geeksforgeeks Joe!'
# # Language in which you want to convert
# language = 'en'
# # Passing the text and language to the engine, 
# # here we have marked slow=False. Which tells 
# # the module that the converted audio should 
# # have a high speed
# myobj = gTTS(text=storytext, lang=language, slow=False)
# # Saving the converted audio in a mp3 file named
# # welcome
# myobj.save("welcome.mp3")
# # Playing the converted file
# os.system("start welcome.mp3")

window.mainloop()