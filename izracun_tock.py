__author__ = 'Gregor'
from tkinter import *
import os
import webbrowser

class Pretvori():
    def __init__(self, master):
        #kako dobiti self.d izven definicije poklicna oz.splosna??
        #division by zero
        self.master = master
        master.title("Izračun točk za sprejem v študetnski dom") #Naslov programa

        menu = Menu(master)
        master.config(menu=menu)

        file_menu=Menu(menu)
        file_menu1 = Menu(menu)
        menu.add_cascade(label="Datoteke", menu=file_menu)
        menu.add_cascade(label = 'Pomoč', menu = file_menu1)
        file_menu.add_command(label= 'Novo',command = self.novo)
        file_menu.add_command(label="Shrani", command = self.shrani)
        file_menu.add_separator() # To doda separator v menu
        file_menu.add_command(label="Izhod", command =master.destroy)
        file_menu1.add_command(label = "Pomoč", command = self.pomoc)


        #glavni gumb
        Button(master, text="Izračunaj", command = self.izracunaj).grid(row=26, column=3)


        self.ime = StringVar()
        Label(master, text="Ime:  ", ).grid(row=0, column=0)              #nepomembno
        Entry(master,value= None, textvariable = self.ime).grid(row=0, column=1)

        self.priimek = StringVar()
        Label(master, text="Priimek:  ").grid(row=1, column=0)          #nepomembno
        Entry(master, value= None, textvariable = self.priimek).grid(row=1, column=1)

        self.starost = IntVar(master, value=0)
        Label(master, text="Starsot:  ").grid(row=2, column=0)          #nepomembno
        Entry(master, textvariable=self.starost).grid(row=2, column=1)

        self.button11= IntVar()
        self.button12 = IntVar()
        Label(master, text="Vrsta mature:  ").grid(row=3, column=0)
        self.button1 = Checkbutton(master, text="Poklicna matura", onvalue=1, offvalue=0, variable=self.button11, command=self.poklicna).grid(row=3, column=1, sticky= S)
        self.button2 = Checkbutton(master, text="Splošna matura",onvalue=1, offvalue=0, variable=self.button12, command= self.splosna).grid(row=4, column=1, sticky=S)



        Label(master, text="Uspeh v zadnjem letniku (s številko): ").grid(row=6,column=0)
        self.e = IntVar(master, value=0)
        uspeh= Entry(master, textvariable=self.e)
        uspeh.grid(row=6,column=1)

        Label(master, text="Izjemen uspeh in obštudijske dejavnosti: ").grid(row=7,column=0)
        Label(master, text="(Izberite največ eno možnost)").grid(row=8,column=0, sticky=S)
        self.h1 = IntVar()
        self.h11 = Radiobutton(master, text="Maturitetno spričevalo s pohvalo",variable=self.h1,value=1, justify = LEFT).grid(row=7, column=1, sticky=W)
        self.h22 = Radiobutton(master, text="Status kategoriziranega vrhunskega športnika \n"
                                 "in uvrstitev do osmega mesta na evropskem ali svetovnem prvenstvu,\n"
                                 " univerziadi ali olimpiadi - velja če študent ni starejši od 25 let,\n"
                                 " ko prvič vloži prošnjo za sprejem v študentski dom", variable=self.h1, value = 2,justify = LEFT).grid(row=8,column=1, sticky=W)
        self.h33 = Radiobutton(master, text='Pohvala ali medalja na mednarodni olimpiadi znanja',variable=self.h1, value = 3,justify = LEFT).grid(row=9,column=1, sticky=W)
        self.g11 = Radiobutton(master, text='Državna nagrada za umetniške dosežke', variable=self.h1,value = 4, justify = LEFT).grid(row=10,column=1, sticky=W)
        self.g22 = Radiobutton(master, text='Status kategoriziranega vrhunskega športnika \n'
                                 ' in uvrstitev do tretjega mesta na državnem prvenstvu \n'
                                 ' in ni starejši od 25 let - velja če študent ni starejši od 25 let, \n'
                                 ' ko prvič vloži prošnjo za sprejem v študentski dom',variable=self.h1, height=5,value = 5, justify = LEFT).grid(row=11,column=1, sticky=W)
        self.g33 = Radiobutton(master, text='Zlato priznanje na državnem tekmovanju iz znanja', variable=self.h1,value = 6, justify = LEFT).grid(row=12,column=1, sticky=W)

        Button(master,text='Izbriši izbiro', command = self.pocisti).grid(row= 12, column = 3)

        Label(master, text="Materialni položaj: ").grid(row=13, column=0)

        Label(master, text='Število družinskih članov:').grid(row=14,column=0)
        self.f=IntVar(master,value=1)
        Entry(master, textvariable=self.f).grid(row=14, column=1)

        Label(master, text='Letni dohodek v družini:').grid(row=15,column=0)
        self.i = IntVar(master,value=0)
        material = Entry(master, textvariable=self.i)
        material.grid(row=15, column=1)

        Label(master, text='Oddaljenost stalnega bivališča do kraja študija (v kilometrih):  ').grid(row=17, column=0)
        self.k = IntVar(master, value=0)
        pot = Entry(master, textvariable= self.k).grid(row=17, column=1)

        Label(master, text='Posebne socialne in zdravstvene razmere in druge izjeme:').grid(row = 18, column = 0)
        self.m = IntVar()
        Radiobutton(master, text = "Težak socialni in/ali zdravstveni položaj ",variable= self.m, value=1, justify = LEFT,).grid (row =19, column=1, sticky=W)
        Radiobutton(master, text = 'Študent starš, ki bo imel tekom študija pri sebi \n'
                                 'svojega otroka, kateri je mlajši od 6 let ali šoloobvezen', variable= self.m, value=2, justify = LEFT).grid (row =20, column=1, sticky=W)
        Radiobutton(master, text = 'Študent, ki je otrok padlih v vojni za Slovenijo ali \n'
                                 'je žrtev naravnih nesreč in ni starejši od 27 let, ko \n'
                                 ' prvič vloži prošnjo za sprejem v študentski dom', variable= self.m, value=3, justify = LEFT).grid(row = 21, column=1,sticky=W)
        Button(master, text='Izbriši izbiro', command = self.pocisti1).grid(row=21, column = 3)
    #----------------------------------------------------------------------------------------------------------------------------------------------------
        Label(master, text = '------------------------------------------------------------').grid(row = 22)
        Label(master, text = '------------------------------------------------------------').grid(row = 22, column=1)

        Label(master, text = 'Skupno število točk za študntski dom: ').grid(row =23)

        self.sum = DoubleVar(master, value=None)
        sum = Label(master, textvariable=self.sum)
        sum.grid(row = 23, column = 1)

#-------------------------------------------------------------------


    def poklicna(self):
        Label( master = self.master, text="Število točk:  ").grid(row=5, column=0)
        self.b = IntVar(master=None, value=0)
        matura = Entry(master=None, textvariable=self.b)
        matura.grid(row=5, column=1)
        self.d = IntVar(master= None, value= self.izracun_poklicna())
        return self.d.get()

    def splosna (self):
        Label(master=None, text="Število točk:  ").grid(row=5, column=0)
        self.b = IntVar(master=None, value=0)
        matura = Entry(master=None, textvariable=self.b)
        matura.grid(row=5, column=1)
        self.d = IntVar(master =None, value=self.izracun_splosna())
        return self.d.get()

    def izracun_poklicna (self):            #izračuna stevilo točk iz mature
        if 24 >= self.b.get() >= 18:
            return 5
        elif 17>= self.b.get() >=14:
            return 4
        elif 13>= self.b.get() >=10:
            return 3
        elif 9>= self.b.get() >=8:
            return 2
        elif 7>= self.b.get() or self.b.get() >=25:
            return 0
    def izracun_splosna(self):

        if 34>= self.b.get()>=24:
            return 5
        elif 23>= self.b.get()>=17:
            return 4
        elif 16>= self.b.get()>=12:
            return 3
        elif 11>= self.b.get()>=9:
            return 2
        elif 8>= self.b.get() or self.b.get() >=35:
            return 0        #izračuna stevilo točk iz mature

    def sola(self):
        if self.button11.get() ==0:
            return ((self.izracun_splosna() + self.e.get())*18)
        else:
            return ((self.izracun_poklicna()  + self.e.get())*18)

    def dohodek(self):
        self.f1 = self.f.get()*12
        self.j1 =  self.i.get()/self.f1
        self.j2 = (self.j1*100 ) /989.91
        self.j = (100- self.j2)*3
        return self.j

    def kilometri(self):
        if self.k.get() >= 100:
            return 100
        else:
            return self.k.get()
    def posebni_dosezki(self):
        if self.h1.get() == 1 or self.h1.get() == 2 or self.h1.get() == 3:
            return 50
        elif self.h1.get() == 4 or self.h1.get() == 5 or self.h1.get() == 6:
            return 30
        else:
            return 0
    def socialne_razmere(self):
        if self.m.get() == 1 or self.m.get() == 2 :
            return 100
        elif self.m.get() == 3:
            return 50
        return 0
    def izracunaj (self):
        a =( self.socialne_razmere() + self.dohodek() + self.sola()  + self.kilometri() + self.posebni_dosezki() )
        self.sum.set(a)

    def shrani(self):
        if os.path.exists(os.getcwd() + '\Rezultati.txt'):
            with open(os.getcwd() + '\Rezultati.txt', 'a') as f:
                print('Ime: {0} \nPriimek: {1}\nStarost: {2} \nTocke za ucni uspeh:{3} \nTocke za uspehe in obštudijske dejavnosti: {4} '
                      '\nTocke za materialni polozaj: {5} \nPosebne socialne in zdravstvene razmere in druge izjemne okoliščine: {6} '
                          '\nTocke za oddaljenost stalnega prebivališča od kraja študija: {7} '
                          '\nSkupno število tock: {8} '.format(self.ime.get(), self.priimek.get(),self.starost.get(),self.sola(),
                                                             self.posebni_dosezki(),self.dohodek(),self.socialne_razmere(),self.kilometri(), self.sum.get()), file=f)
        else:
            with open(os.getcwd() + '\Rezultati.txt', 'w') as f:
                print('Ime: {0} \nPriimek: {1}\nStarost: {2} \nTocke za ucni uspeh:{3} \nTocke za uspehe in obštudijske dejavnosti: {4} '
                      '\nTocke za materialni polozaj: {5} \nPosebne socialne in zdravstvene razmere in druge izjemne okoliščine: {6} '
                          '\nTocke za oddaljenost stalnega prebivališča od kraja študija: {7} '
                          '\nSkupno število tock: {8} '.format(self.ime.get(), self.priimek.get(),self.starost.get(),self.sola(),
                                                             self.posebni_dosezki(),self.dohodek(),self.socialne_razmere(),self.kilometri(), self.sum.get()), file=f)

    def pomoc (self):
         webbrowser.open("http://studentski.net/bivanje/sprejem-v-studentski-dom-tockovalni-sistem.html")
    def novo (self):
        self.ime.set('')
        self.priimek.set('')
        self.starost.set(0)
        self.e.set(0)
        self.i.set(0)
        self.b.set(0)
        self.d.set(0)
        self.button11.set(0)
        self.button12.set(0)
        self.h1.set(0)
        self.f.set(1)
        self.k.set(0)
        self.m.set(0)
        self.sum.set(0)
    def pocisti(self):
        self.h1.set(0)

    def pocisti1(self):
        self.m.set(0)
# Naredimo glavno okno
root = Tk()

aplikacija = Pretvori(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
