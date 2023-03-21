import tkinter as tk
import random


 
def kiri_vasak():
    num1 = random.randint(1,2)
    #print(num1)
    if num1 == 1:
        print("läksid vasakule ja kohtusid Üllariga")
        ullar2 = random.randint(1,4)
        if ullar2 == 1:
            print("Üllar astus sinuga võitlusesse, millest ta ennast päästa ei suutnud, sa jätkad")
        if ullar2 == 2:
            print("Üllar solvas sinu ema ja sa surid, sa ei jätka")
            exit()
        if ullar2 == 3:
            print("Üllar andis sulle peksa ja soovis sulle edu teel, sa jätkad")
        if ullar2 == 4:
            print("Üllar tegi sulle noomituse, sa jätkad oma teed ")
        
    if num1 ==2:
        print("läksid vasakule ja jätkad oma teed")
def kiri_parem():
    num2 = random.randint(1,2)
    #print (num2)
    if num2 == 1:
        print("läksid paremale ja kohtusid Siimuga")
        siim2 = random.randint(1,4)
        if siim2 == 1:
            print("Siim astus sinuga võitlusesse, millest ta ennast välja ei vaielnud, sa jätkad")
        if siim2 == 2:
            print("Siim solvas sinu bashi skille ja sa surid, sa ei jätka")
            exit()
        if siim2 == 3:
            print("Siim andis sulle mälupulga ja soovis sulle edu teel, sa jätkad")
        if siim2 == 4:
            print("Siim tegi sulle psüühilise noomituse, sa jätkad oma teed ")
    if num2 ==2:
        print("läksid paremale ja jätkad oma teed")
def kiri_tagasi():
    num3 = random.randint(1,2)
    #print(num3)
    if num3 == 1:
        print("läksid tagasi ja kohtusid Uudoga")
        uudo2 = random.randint(1,4)
        if uudo2 == 1:
            print("Uudo astus sinuga võitlusesse, millest ta ennast välja ei laulnud, sa jätkad")
        if uudo2 == 2:
            print("Sa sattusid peale Uudole ja ta laulis su surnuks, sa ei jätka")
            exit()
        if uudo2 == 3:
            print("Uudo andis sulle 10euki ja soovis sulle edu teel, sa jätkad")
        if uudo2 == 4:
            print("Uudo ei soovinud tegemist teha, sa jätkad")
        
    if num3 ==2:
        print("läksid tagasi ja jätkad oma teed")
def kiri_otse():
    num4 = random.randint(1,2)
    #print(num4)
    if num4 == 1:
        print("läksid otse ja kohtusid Mart Helmega")
        mart2 = random.randint(1,4)
        if mart2 == 1:
            print("Mart viskas sulle 5s ja lubas sul jätkata")
        if mart2 == 2:
            print("Mart keelas sul edasi minna ja tegi sulle füüsilise noomituse, sa ei jätka")
            exit()
        if mart2 == 3:
            print("Mart astus sinuga võitlusesse, mille sa võitsid, jätkad oma teed")
        if mart2 == 4:
            print("Mart ei soovinud tegemist teha ja sa jätkad")
            
            
            
    if num4 ==2:
        print("läksid otse ja jätkad oma teed")
        


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.geometry("300x300")


button = tk.Button(frame, 
                   text="lõpp", 
                   fg="red",
                   command=quit)


button.pack(side=tk.LEFT)
vasak = tk.Button(frame,
                   text="Vasak",
                   fg="blue",
                   command=kiri_vasak)



parem = tk.Button(frame,
                   text="Parem",
                   fg="blue",
                   command=kiri_parem)


otse = tk.Button(frame,
                   text="Otse",
                   fg="blue",
                   command=kiri_otse)


tagasi = tk.Button(frame,
                   text="Tagasi",
                   fg="blue",
                   command=kiri_tagasi)


vasak.pack(side=tk.LEFT)
parem.pack(side=tk.LEFT)
otse.pack(side=tk.LEFT)
tagasi.pack(side=tk.LEFT)

    

root.mainloop()