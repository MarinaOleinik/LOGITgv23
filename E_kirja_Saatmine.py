import email
from tkinter import *
import smtplib,ssl 
from email.message import EmailMessage
import imghdr
from tkinter import messagebox, filedialog
file="vihm.png"
def vali_pilt():
    global file
    file=filedialog.askopenfilename()

    return file
def saada_kiri():
    kellele=email_box.get()
    kiri=kiri_box.get("1.0",END)
    smtp_server="smtp.gmail.com"
    port=587
    sender_email="oleinik.marina@gmail.com"
    password="sdas fssd dfsf ghgh" #InputBox()
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri)
    msg['Subject']="E-kiri saatmine" #from Entry
    msg['From']="Marina Oleinik"
    msg['To']=kellele
    with open(file,'rb') as fpilt:
        pilt=fpilt.read()
    msg.add_attachment(pilt,maintype='image',subtype=imghdr.what(None,pilt))
    try:
        server=smtplib.SMTP(smtp_server,port)
        server.starttls(context=context)
        server.login(sender_email,password)
        server.send_message(msg)
        messagebox.showinfo("Informatsioon","Kiri oli saadetud")  
    except Exception as e:
        messagebox.showerror("Tekkis viga!",e)
    finally:
        server.quit()

aken=Tk()
aken.geometry("420x300")
aken.title("E-kirja saatmine")
aken.iconbitmap("mail.ico")
l_mail=Label(aken,text="Email:",bg="#38761d",fg="#e7efe3",font="Castellar 16",height=1,width=8)
l_kiri=Label(aken,text="Kiri:",bg="#38761d",fg="#e7efe3",font="Castellar 16",height=1,width=8)
l_teema=Label(aken,text="Teema:",bg="#38761d",fg="#e7efe3",font="Castellar 16",height=1,width=8)
teema_box=Entry(aken,bg="#e7efe3",fg="#38761d",font="Arial 18",width=20,justify=LEFT)
l_lisa=Label(aken,text="Lisa:",bg="#38761d",fg="#e7efe3",font="Castellar 16",height=1,width=8)
l_lisatud=Label(aken,text="...",bg="#e7efe3",fg="#38761d",font="Castellar 16",height=1,width=20)
email_box=Entry(aken,bg="#e7efe3",fg="#38761d",font="Arial 18",width=20,justify=LEFT)
kiri_box=Text(aken,bg="#e7efe3",fg="#38761d",font="Arial 18",height=6,width=20)
saada_btn=Button(aken,text="Saada",bg="#38761d",fg="#e7efe3",font="Castellar 16",relief=RAISED,command=saada_kiri)

pilt_btn=Button(aken,text="Lisa pilt",bg="#38761d",fg="#e7efe3",font="Castellar 16",relief=RAISED,command=vali_pilt)

l_mail.grid(row=0,column=0)
email_box.grid(row=0,column=1,columnspan=2)
l_teema.grid(row=1,column=0)
teema_box.grid(row=1,column=1,columnspan=2)
l_lisa.grid(row=2,column=0)
l_lisatud.grid(row=2,column=1,columnspan=2)
l_kiri.grid(row=3,column=0)
kiri_box.grid(row=3,column=1,columnspan=2)




saada_btn.grid(row=4,column=2)

pilt_btn.grid(row=4,column=1)
aken.mainloop()