import tkinter as tk

gui_window=tk.Tk()

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

button1=tk.Button(gui_window,text='Veiw All Books',width=12,activebackground='khaki2',activeforeground='red')
button1.grid(row=3,column=1)

button2=tk.Button(gui_window,text='Add Book',width=12,activebackground='pale green')
button2.grid(row=3,column=3)

button3=tk.Button(gui_window,text='Search a Book',width=12,activebackground='SkyBlue')
button3.grid(row=4,column=1)

button4=tk.Button(gui_window,text='Update a Book',width=12,activebackground='MediumPurple1')
button4.grid(row=4,column=3)

button5=tk.Button(gui_window,text='Delete Book',width=12,activebackground='dark orange')
button5.grid(row=5,column=1)

button6=tk.Button(gui_window,text='Close',width=12,activebackground='firebrick1')
button6.grid(row=5,column=3)

scroll=tk.Scrollbar(gui_window)
scroll.grid(row=6,column=4,rowspan=6)

lst=tk.Listbox(gui_window,height=6,width=55)
lst.grid(row=6,column=0,rowspan=6,columnspan=4)

lst.config(yscrollcommand=scroll.set)
scroll.config(command=lst.yview)

gui_window.mainloop()