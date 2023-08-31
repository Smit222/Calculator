from tkinter import *
root=Tk()

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)

    if text == '=':

            if scvalue.get().isdigit():
                value=float(scvalue.get())

            else:
                value= eval(frame.get())

            scvalue.set(value)
            frame.update()

    elif text == 'C':
        scvalue.set("")
        frame.update()
    else:
        scvalue.set(scvalue.get() + text)
        frame.update()

root.geometry('400x500')
root.resizable(False,False)
root.title("Calculator created by Smit")

scvalue=StringVar()
scvalue.set("")

add_button=Button(root,text="+",font="arial 15",width=2,height=1,background="#CDC9A5",foreground="Black",bd=5)
add_button.place(x=290,y=43)
add_button.bind("<Button-1>", click)
add_button=Button(root,text="-",font="arial 15",width=2,height=1,background="#CDC9A5",foreground="Black",bd=5)
add_button.place(x=290,y=108)
add_button.bind("<Button-1>", click)
add_button=Button(root,text="*",font="arial 15",width=2,height=1,background="#CDC9A5",foreground="Black",bd=5)
add_button.place(x=290,y=167)
add_button.bind("<Button-1>", click)
add_button=Button(root,text="/",font="arial 15",width=2,height=1,background="#CDC9A5",foreground="Black",bd=5)
add_button.place(x=290,y=228)
add_button.bind("<Button-1>", click)

frame=Entry(root,textvariable=scvalue, font="arail 20 bold")
frame.pack()

frame1= Frame(root, background="#CDC9A5")
button1=Button(frame1,text="9",padx=5,pady=5,font="arail 15 bold")
button1.pack(side=LEFT,padx=5,pady=5 )
button1.bind("<Button-1>", click)

button1=Button(frame1,text="8",padx=5,pady=5,font="arail 15 bold")
button1.pack(side=LEFT,padx=5,pady=5 )
button1.bind("<Button-1>", click)

button1=Button(frame1,text="7", padx=5,pady=5 ,font="arail 15 bold")
button1.pack(side=LEFT,padx=5,pady=5 )
button1.bind("<Button-1>", click)
frame1.pack()


frame1= Frame(root, background="#CDC9A5")
button1=Button(frame1,text="6",padx=5,pady=5 , font="arail 15 bold")
button1.pack(side=LEFT,padx=5,pady=5 )
button1.bind("<Button-1>", click)

button1=Button(frame1,text="5", padx=5,pady=5 ,font="arail 15 bold")
button1.pack(side=LEFT,padx=5,pady=5 )
button1.bind("<Button-1>", click)

button1=Button(frame1,text="4",padx=5,pady=5 , font="arail 15 bold")
button1.pack(side=LEFT,padx=5,pady=5 )
button1.bind("<Button-1>", click)
frame1.pack()

frame1= Frame(root, background="#CDC9A5")
button1=Button(frame1,text="3",padx=5,pady=5 , font="arail 15 bold")
button1.pack(side=LEFT,padx=5,pady=5 )
button1.bind("<Button-1>", click)

button1=Button(frame1,text="2", padx=5,pady=5 ,font="arail 15 bold")
button1.pack(side=LEFT,padx=5,pady=5)
button1.bind("<Button-1>", click)

button1=Button(frame1,text="1", padx=5,pady=5 ,font="arail 15 bold")
button1.pack(side=LEFT,padx=5,pady=5 )
button1.bind("<Button-1>", click)
frame1.pack()

frame1= Frame(root, background="#CDC9A5")
button1=Button(frame1,text="0",padx=5,pady=5 , font="arail 15 bold")
button1.pack(side=LEFT,padx=5,pady=5 )
button1.bind("<Button-1>", click)

button1=Button(frame1,text="C", padx=5,pady=5 ,font="arail 15 bold")
button1.pack(side=LEFT,padx=5,pady=5 )
button1.bind("<Button-1>", click)

button1=Button(frame1,text="=",padx=5,pady=5 , font="arail 15 bold")
button1.pack(side=LEFT,padx=5,pady=5 )
button1.bind("<Button-1>", click)
frame1.pack()


root.mainloop()
