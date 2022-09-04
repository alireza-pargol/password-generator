import string, random
from tkinter import *

x = {"Lowercase letters" : string.ascii_lowercase,
    "Capital letters" : string.ascii_uppercase,
    "Character" : "!@#$%^&*()",
    "Numbers" : string.digits}

def generate():
    if resualt.get():
        resualt.delete(0,END)

    items = ''
    all_items = list.curselection()
    for i in all_items:
        option = list.get(i)
        items += x[option]
    password = ''.join(random.choice(items)
                       for i in range(int(count.get())))

    resualt.insert(END, password)

window = Tk()
window.title('Generate Password')
window.geometry("300x350")

label = Label(window,
              text="Chose the number of characters",
              font=("Times New Roman", 10),
              padx=10, bg='lightyellow')
label.pack(fill='both')

count = Scale(window, from_=1, to_=20, orient=HORIZONTAL)
count.pack(pady=5)

label_list = Label(window,
              text="Select the options used in the password :",
              font=("Times New Roman", 10), padx=10, bg='lightyellow')
label_list.pack(fill='both')

list = Listbox(window, selectmode="multiple", justify="center")
list.pack(padx=10, pady=10, fill="both")
for each_item in x.keys():
    list.insert(END, each_item)

btn = Button(window, text="Generate password",
             font=("Arial", 10), command=generate)
btn.pack(padx=10, pady=5)

resualt = Entry(window,font=("Arial", 15) ,
               justify=CENTER , bd=0 , bg = "systembuttonface")
resualt.pack(fill="both",pady=5)

window.mainloop()