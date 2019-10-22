from tkinter import *
from back import Database

database=Database()

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple = list1.get(index)
        t1.delete(0,END)
        t1.insert(END,selected_tuple[1])
        t2.delete(0,END)
        t2.insert(END,selected_tuple[3])
        t3.delete(0,END)
        t3.insert(END,selected_tuple[2])
        t4.delete(0,END)
        t4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END,row)

def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

window=Tk()
window.wm_title("Book Store")

#Labels
l1=Label(window,text="Title",font=("Helvetica", 12), anchor=W, justify=LEFT)
l1.grid(row=0,column=0)

l2=Label(window,text="Year",font=("Helvetica", 12), anchor=W, justify=LEFT)
l2.grid(row=1,column=0)

l3=Label(window,text="Author",font=("Helvetica", 12), anchor=W, justify=LEFT)
l3.grid(row=0,column=2)

l4=Label(window,text="ISBN",font=("Helvetica", 12), anchor=W, justify=LEFT)
l4.grid(row=1,column=2)

#Entry texts
title_text=StringVar()
t1=Entry(window,textvariable=title_text, highlightthickness=1, highlightbackground="#111")
t1.grid(row=0,column=1)

year_text=StringVar()
t2=Entry(window,textvariable=year_text, highlightthickness=1, highlightbackground="#111")
t2.grid(row=1,column=1)

author_text=StringVar()
t3=Entry(window,textvariable=author_text, highlightthickness=1, highlightbackground="#111")
t3.grid(row=0,column=3)

isbn_text=StringVar()
t4=Entry(window,textvariable=isbn_text, highlightthickness=1, highlightbackground="#111")
t4.grid(row=1,column=3)

#Listbox and scrollbar
list1=Listbox(window, height=6, width=35, highlightthickness=2, highlightbackground="#dfddc7")
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

#Buttons
b1=Button(window,text="View All",bg="#51dacf", highlightthickness=2, highlightbackground="#111", width=12, command=view_command)
b1.grid(row=3, column=3)

b2=Button(window,text="Search",bg="#76dbd1", highlightthickness=2, highlightbackground="#111", width=12, command=search_command)
b2.grid(row=4, column=3)

b3=Button(window,text="Add",bg="#51dacf", highlightthickness=2, highlightbackground="#111", width=12, command=add_command)
b3.grid(row=5, column=3)

b4=Button(window,text="Update",bg="#76dbd1", highlightthickness=2, highlightbackground="#111", width=12, command=update_command)
b4.grid(row=6, column=3)

b5=Button(window,text="Delete",bg="#51dacf", highlightthickness=2, highlightbackground="#111", width=12, command=delete_command)
b5.grid(row=7, column=3)

b6=Button(window,text="Close",bg="#76dbd1", highlightthickness=2, highlightbackground="#111", width=12, command=window.destroy)
b6.grid(row=8, column=3)

window.mainloop()
