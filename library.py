import tkinter as tk
from tkinter.constants import END, VERTICAL
import button 

def view_cmd():
    lst.delete(0,END)
    for data in button.view_data():
        lst.insert(END,data)

def add_cmd():
    button.insert_in_database(title_val.get(),author_val.get(),year_val.get(),isbn_val.get())
    lst.delete(0,END)
    lst.insert(END,(title_val.get(),author_val.get(),year_val.get(),isbn_val.get()))

def search_cmd():
    lst.delete(0,END)
    for data in button.search_in_database(title_val.get(),author_val.get(),year_val.get(),isbn_val.get()):
        lst.insert(END,data)

def delete_cmd():
    button.delete_record(selection[0])

def update_cmd():
    button.update_record(selection[0],title_val.get(),author_val.get(),year_val.get(),isbn_val.get())

def get_selected_row(event):
    try:
        global selection
        index=lst.curselection()[0]
        selection=lst.get(index)
        entry1.delete(0,END)
        entry1.insert(END,selection[1])
        entry2.delete(0,END)
        entry2.insert(END,selection[2])
        entry3.delete(0,END)
        entry3.insert(END,selection[3])
        entry4.delete(0,END)
        entry4.insert(END,selection[4])
    except IndexError:
        pass
gui_window=tk.Tk()

gui_window.title('Library Management System')

gui_window.geometry("380x250")

label1=tk.Label(gui_window,text='Title')
label1.grid(row=0,column=0)

label2=tk.Label(gui_window,text='Author')
label2.grid(row=0,column=2)

label3=tk.Label(gui_window,text='Year')
label3.grid(row=1,column=0)

label4=tk.Label(gui_window,text='ISBN Code')
label4.grid(row=1,column=2)

title_val=tk.StringVar()
entry1=tk.Entry(gui_window,textvariable=title_val)
entry1.grid(row=0,column=1)

author_val=tk.StringVar()
entry2=tk.Entry(gui_window,textvariable=author_val)
entry2.grid(row=0,column=3)

year_val=tk.StringVar()
entry3=tk.Entry(gui_window,textvariable=year_val)
entry3.grid(row=1,column=1)

isbn_val=tk.StringVar()
entry4=tk.Entry(gui_window,textvariable=isbn_val)
entry4.grid(row=1,column=3)

button1=tk.Button(gui_window,text='Veiw All Books',width=12,activebackground='khaki2',activeforeground='red',command=view_cmd)
button1.grid(row=3,column=1)

button2=tk.Button(gui_window,text='Add Book',width=12,activebackground='pale green',command=add_cmd)
button2.grid(row=3,column=3)

button3=tk.Button(gui_window,text='Search a Book',width=12,activebackground='SkyBlue',command=search_cmd)
button3.grid(row=4,column=1)

button4=tk.Button(gui_window,text='Update a Book',width=12,activebackground='MediumPurple1',command=update_cmd)
button4.grid(row=4,column=3)

button5=tk.Button(gui_window,text='Delete Book',width=12,activebackground='dark orange',command=delete_cmd)
button5.grid(row=5,column=1)

button6=tk.Button(gui_window,text='Close',width=12,activebackground='firebrick1',command=gui_window.destroy)
button6.grid(row=5,column=3)

scroll=tk.Scrollbar(gui_window)
scroll.grid(row=6,column=4,rowspan=6)

lst=tk.Listbox(gui_window,height=6,width=55)
lst.grid(row=6,column=0,rowspan=6,columnspan=4)

lst.config(yscrollcommand=scroll.set)
scroll.config(command=lst.yview)

lst.bind('<<ListboxSelect>>',get_selected_row)

gui_window.mainloop()