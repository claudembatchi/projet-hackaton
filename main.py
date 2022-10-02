
from tkinter import *
global fenetre1, fenetre2
import webbrowser
def test():
    global fenetre1, fenetre2
    fenetre1.destroy()
    acceuil()

def fenetre():
    global fenetre1
    fenetre1 = Tk()
    fenetre1.title("cleanet")
    fenetre1.geometry("1080x720")
    fenetre1.minsize(480, 360)
    fenetre1.iconbitmap("")
    # une boite

    can = Canvas(fenetre1, width="1600", height="1600")

    img = PhotoImage(file="C:\\Users\\Cedric\\PycharmProjects\\projet ackton\\image.gif")
    frame = Frame(fenetre1, bg="white")
    frame = Frame(fenetre1, bg="white")
    label1 = Label(frame, text=" bienvenue sur cleanet", bg="white", fg="#086c0a", font=("areal", 40))
    label1.pack()
    label1 = Label(frame, text="l'application de detection des especes menacées", bg="white", fg="#086c0a",
                   font=("curriel", 20))
    label1.pack()
    bouton = Button(frame, text="ENTRER", fg="white" ,bg="#086c0a", command=test)
    bouton.pack(pady=25 ,fill=X)

    frame.pack(expand=YES)

    can.create_image(50, 50, anchor=NW, image=img)
    frame.pack(expand=YES)

    can.place(x=0, y=0)

    fenetre1.mainloop()

def acceuil():


    # Création de la barre des menu
    def chien():

        filewin = Toplevel(fenetre2)
        filewin.geometry("1080x720")
        button = Button(filewin, text="retour", fg="white" ,bg="#086c0a", command=test)
        button.pack()



    def chat():
        filewin = Toplevel(fenetre2)
        filewin.geometry("1080x720")
        button = Button(filewin, text="retour", fg="white", bg="#086c0a", command=test)
        button.pack()

    def souris():
        filewin = Toplevel(fenetre2)
        filewin.geometry("1080x720")
        button = Button(filewin, text="retour", fg="white", bg="#086c0a", command=test)
        button.pack()

    def lesard():
        filewin = Toplevel(fenetre2)
        filewin.geometry("1080x720")
        button = Button(filewin, text="retour", fg="white", bg="#086c0a", command=test)
        button.pack()

    def canard():
        filewin = Toplevel(fenetre2)
        filewin.geometry("1080x720")
        button = Button(filewin, text="retour", fg="white", bg="#086c0a", command=test)
        button.pack()

    def apropos():
        filewin = Toplevel(fenetre2)
        filewin.geometry("1080x720")
        button = Button(filewin, text="retour", fg="white", bg="#086c0a", command=test)
        button.pack()

    def contact():
        filewin = Toplevel(fenetre2)
        filewin.geometry("1080x720")
        button = Button(filewin, text="retour", fg="white", bg="#086c0a", command=test)
        button.pack()

    def ong():
        filewin = Toplevel(fenetre2)
        filewin.geometry("1080x720")
        button = Button(filewin, text="retour", fg="white", bg="#086c0a", command=test)
        button.pack()

    def alerte():
        filewin = Toplevel(fenetre2)
        filewin.geometry("1080x720")
        filewin.config(background="red")
        button = Button(filewin, text="retour", fg="white", bg="#086c0a", command=test)
        button.pack()

    def maps():
        filewin = Toplevel(fenetre2)
        filewin.geometry("1080x720")
        button = Button(filewin, text="retour", fg="#086c0a", bg="white", command=test)
        button.pack()
        label = Label(filewin, text="zone protegée", font=("areal", 30), fg="red")
        label.pack(pady=4)
        photo = PhotoImage(file="CC.png", )

        image_photo = Label(filewin, text="animaux protegés", font=("areal", 30, "bold"), fg="#086c0a", image=photo,
                            compound="bottom")
        image_photo.pack()

    def region():
        filewin = Toplevel(fenetre2)
        filewin.geometry("1080x720")
        button = Button(filewin, text="retour", fg="#086c0a", bg="white", command=test)
        button.pack()


    def donothing():
        filewin = Toplevel(fenetre2)
        filewin.geometry("1080x720")
        button = Button(filewin, text="AAA")
        button.pack()
    fenetre2 = Tk()
    fenetre2.title("cleanet")
    fenetre2.geometry("1080x720")
    fenetre2.minsize(480, 360)
    fenetre2.iconbitmap("")
    fenetre2.config(background="white")
    menubar = Menu(fenetre2)
    def sesar_am():
        webbrowser.open_sesar_am("https://youtu.be/5WJZqTlbgD8")
    filemenu = Menu(menubar, tearoff=0)


    filemenu.add_command(label="Tortues marine", command=chien)
    filemenu.add_command(label="Guorille", command=chat)
    filemenu.add_command(label="Elephant", command=souris)


    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=fenetre2.quit)
    menubar.add_cascade(label="annimaux ménacés", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)

    editmenu.add_separator()

    editmenu.add_command(label="Renatura", command=donothing)
    editmenu.add_command(label="Climate Education", command=donothing)
    editmenu.add_command(label="Couronne Verte", command=donothing)
    editmenu.add_command(label="FIve Enviro Communication", command=donothing)


    menubar.add_cascade(label="organisatiion", menu=editmenu)
    telemenu = Menu(menubar, tearoff=0)
    telemenu.add_command(label="ONG", command=ong)
    telemenu.add_command(label="Alerte", command=alerte)
    menubar.add_cascade(label="télédetection", menu=telemenu)
    regionmenu = Menu(menubar, tearoff=0)
    regionmenu.add_command(label="kouilou", command=region)
    regionmenu.add_command(label="pointe-noire", command=region)
    menubar.add_cascade(label="region", menu=regionmenu)

    mapsmenu = Menu(menubar, tearoff=0)

    menubar.add_cascade(label="maps", menu=mapsmenu)
    mapsmenu.add_command(label="maps", command=maps)


    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="contact", command=contact)
    helpmenu.add_command(label="Apropos", command=apropos)
    menubar.add_cascade(label="cleanet", menu=helpmenu)


    fenetre2.config(menu=menubar)


    # Création du cadre-conteneur pour les menus
    """
    label= Label(fenetre2, text="PROTECTION D'ANIMAUX" ,font=("areal",30) ,fg="#086c0a")
    label.pack(pady=4)
    photo = PhotoImage(file="CC.png",)

    image_photo = Label(fenetre2, text="animaux protegés", font=("areal", 30 ,"bold"), fg="#086c0a",image=photo,compound="bottom")
    image_photo.pack()

    fenetre2 = Canvas(fenetre2,width=200,height=200)
    fenetre2.pack()
    """
    # Création de l'onglet texte
    frame = Frame(fenetre2)
    label = Label(frame, text="CLEANET", font=("areal", 30), fg="black")
    label.pack(pady=4)
    label = Label(frame, text="est une application qui permet de repertorier et de cartographier", font=("areal", 10), fg="black")
    label.pack(pady=4)
    label = Label(frame, text="les especes ménacés, les regions ménacées et les organisation non gouvernementale", font=("areal", 10), fg="black")
    label.pack(pady=4)
    label = Label(frame, text="qui lutte pour un environement sain au Congo", font=("areal", 10),
                  fg="black")
    label.pack(pady=4)

    fb_lien = Button(frame, text="voir la video", font=("areal", 30), fg="white", bg="BLACK", command=sesar_am)
    fb_lien.pack(pady=25, fill=X)
    frame.pack(expand=YES)



    # image = PhotoImage(file="CC.png")
    # fenetre2.create_image(0, 0, anchor=NW, image=image)

    # fenetre2 = Canvas(fenetre2, width=200, height=200)
    # fenetre2.pack()
    # image = PhotoImage(file="CC.png")
    # fenetre2.create_image(0, 0, anchor=NW, image=image)

    fenetre2.mainloop()




if __name__ == '__main__':
    fenetre()
