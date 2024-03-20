from tkinter import *
def FromEntryToLabel(event):
    tekst=e.get()
    l.configure(text=tekst)
def valik():
    arv=var.get()
    e.delete(0,END)
    e.insert(END,arv)
showflag=False
def naitatarnid(event):
    global showflag
    if showflag:
        e.configure(show="")
        showflag=False
    else:
        e.configure(show="*")
        showflag=True
def chekbutton_select(event):
    v1=var1.get()
    v2=var2.get()
    jarjend=[v1,v2]
    lb.delete(0,1)
    for item in jarjend:
        lb.insert(END,item)

aken=Tk()
aken.geometry("740x700")
aken.title("Tkinteri kasutamine. See on pealkiri")
aken.iconbitmap("icon.ico")
f=Frame(aken,bg="#346089",border=50,height=50,width=600)
f_all=Frame(aken,bg="#5596d0",border=10,height=200,width=600)

l=Label(f,text="x**2",bg="#38761d",fg="#e7efe3",font="Castellar 16",height=3,width=4)
a=Entry(f,bg="#38761d",width=4,font="Arial 20")
e=Entry(f_all,bg="#e7efe3",fg="#38761d",font="Arial 20",width=30,justify=CENTER)#,show="*"
e.bind("<Return>",naitatarnid) #Enteri peale vajutamine
b=Button(f_all,text="Vajuta siia",bg="lightblue",font="Arial 20",relief=RAISED)#SUNKEN#GROOVE)
b.bind("<Button-1>",FromEntryToLabel) #LKM
b.bind("<Button-3>",chekbutton_select) #PKM
var=IntVar() #StringVar()
r1=Radiobutton(f_all,text="Esimene",font="Arial 20",bg="#5596d0",variable=var,value=1,command=valik)
r2=Radiobutton(f_all,text="Teine",font="Arial 20",bg="#5596d0",variable=var,value=2,command=valik)
r3=Radiobutton(f_all,text="Kolmas",font="Arial 20",bg="#5596d0",variable=var,value=3,command=valik)
img1=PhotoImage(file="paike.png")
img2=PhotoImage(file="vihm.png")
var1=StringVar()
var2=StringVar()
c1=Checkbutton(f_all,image=img1,variable=var1,bg="#5596d0",onvalue="Päike paistab",offvalue="Päike ei paista")
c2=Checkbutton(f_all,image=img2,variable=var2,bg="#5596d0",onvalue="Sajab vihn",offvalue="Vihma ei ole")
c1.deselect()
c2.deselect()
lb=Listbox(f_all,height=2,width=30,font="Arial 20")

f.grid(row=0,column=0) #place()-koordinaadid, pack()-nii nägu nimekirjas
a.grid(row=0,column=0)
l.grid(row=0,column=1)


f_all.grid(row=1,column=0)
e.grid(row=0,column=0,columnspan=6)
obj=[b,r1,r2,r3,c1,c2]
i=0
for o in obj:
    o.grid(row=1,column=i)
    i+=1
lb.grid(row=2,column=0,columnspan=6)
aken.mainloop()
