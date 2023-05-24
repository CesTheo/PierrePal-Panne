import os
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from PIL import ImageTk, Image
import random
import requests

class Chrono:
    def __init__(self, master):
        self.win_key = None;
        self.master = master
        width=1920
        height=1080
        screenwidth = self.master.winfo_screenwidth()
        screenheight = self.master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.master.geometry(alignstr)
        self.master.resizable(width=False, height=False)
        self.master.title("Sniffeur")
        self.master.overrideredirect(True)
        self.master.geometry('1920x1080')
        self.master["bg"] = "#d04927"
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)


        TKButton=tk.Button(self.master)
        TKButton["borderwidth"] = "0px"
        TKButton["cursor"] = "target"
        ft = tkFont.Font(family='Terminal',size=24)
        TKButton["font"] = ft
        TKButton["bg"] = "#e15a38"
        TKButton["fg"] = "#ffffff"
        TKButton["justify"] = "center"
        TKButton["text"] = "Cliquez ici pour soutenir PierrePasPanne"
        TKButton.place(x=460,y=300,width=1000,height=114)
        TKButton["borderwidth"] = 10
        TKButton["command"] = self.reset

        TKText1=tk.Label(self.master)
        TKText1["text"]= "Merci d'avoir soutenue Pierre\n il vient de sniffer une ligne, mais il en voudra encore\n attention un fichier avec de la c vien d'étre enlever\n sacré Pierre" 
        ft1 = tkFont.Font(family='Terminal',size=20)
        TKText1["font"]= ft1
        TKText1["bg"] = "#d04927"
        TKText1["fg"] = "#ffffff"
        TKText1.place(x=650,y=450,width=620,height=100)


        self.filename = ""
        self.TKText2=tk.Label(self.master)
        self.TKText2["text"]= self.filename
        self.TKText2["font"] = ft1
        self.TKText2["bg"] = "#d04927"
        self.TKText2.place(x=0,y=680,width=1920,height=100)


        
        self.seconds_left = 60000 # 2 minutes en millisecondes
        
        self.label = tk.Label(self.master, text="")
        self.label.pack()
        self.label.place(x=610,y=180,width=700,height=100)
        fontTime = tkFont.Font(family='Terminal',size=60, weight="bold")
        self.label["font"] = fontTime
        self.label["bg"] = "#d04927"
        self.label["fg"] = "#ffffff"
        
        Pixelart = Image.open("pixelart.png")
        photo = ImageTk.PhotoImage(Pixelart)

        for i in range(10):
            label_name = "self.label" + str(i+1)
            exec(label_name + " = Label(self.master, image=photo)")
            exec(label_name + ".pack()")
            exec(label_name + ".image = photo")
            exec(label_name + ".bg = '#d04927'")
            exec(label_name + ".place(x=200*i,y=740,width=200,height=390)")

        navbar = tk.Label(self.master, borderwidth=6, relief="groove")
        navbar["bg"] = "#0057E6"
        navbar["fg"] = "#0057E6"   
        navbar.place(x=191,y=107,width=1537,height=60)

        navbarTitre = tk.Label(self.master, text="Software PalPanne")
        navbarTitre["bg"] = "#0057E6"
        navbarTitre["fg"] = "#FFFFFF"
        Terminale = tkFont.Font(family='Terminal',size=14, weight="bold")
        navbarTitre["font"] = Terminale
        navbarTitre.place(x=201,y=121,width=237,height=30)

        navbarButton=tk.Button(self.master)
        navbarButton["borderwidth"] = "0px"
        navbarButton["cursor"] = "target"
        navbarButton["font"] = Terminale
        navbarButton["bg"] = "#B44533"
        navbarButton["fg"] = "#ffffff"
        navbarButton["justify"] = "center"
        navbarButton["text"] = "×"
        navbarButton.place(x=1680,y=121,width=30,height=30)
        navbarButton["borderwidth"] = 5
        navbarButton.bordercolor = "#ffffff"

        navbar1Button=tk.Button(self.master)
        navbar1Button["borderwidth"] = "0px"
        navbar1Button["cursor"] = "target"
        navbar1Button["font"] = Terminale
        navbar1Button["bg"] = "#4679CC"
        navbar1Button["fg"] = "#ffffff"
        navbar1Button["justify"] = "center"
        navbar1Button["text"] = "□"
        navbar1Button.place(x=1640,y=121,width=30,height=30)
        navbar1Button["borderwidth"] = 5
        navbar1Button.bordercolor = "#ffffff"

        navbar2Button=tk.Button(self.master)
        navbar2Button["borderwidth"] = "0px"
        navbar2Button["cursor"] = "target"
        navbar2Button["font"] = Terminale
        navbar2Button["bg"] = "#4679CC"
        navbar2Button["fg"] = "#ffffff"
        navbar2Button["justify"] = "center"
        navbar2Button["text"] = "_"
        navbar2Button.place(x=1600,y=121,width=30,height=30)
        navbar2Button["borderwidth"] = 5
        navbar2Button.bordercolor = "#ffffff"

        self.update_clock()

    def animate(self):
        self.y_pos += self.direction * 5
        self.canvas.coords(self.image_id, 50, self.y_pos)
        if self.y_pos > 200:
            self.direction = -1
        elif self.y_pos < 50:
            self.direction = 1
        self.canvas.after(50, self.animate)

        
    def update_clock(self):
        self.seconds_left -= 20 # mise à jour toutes les 10 millisecondes
        if self.seconds_left <= 0:
            # os.system("shutdown /s /t 1")
            self.master.destroy() # ferme la fenêtre Tkinter
        else:
            minutes, seconds = divmod(self.seconds_left // 1000, 60)
            milliseconds = self.seconds_left % 1000
            self.label.config(text=f"{minutes:02d}:{seconds:02d}:{milliseconds:03d}")
            self.master.after(10, self.update_clock)
        
    def reset(self):
        response = requests.get("http://localhost:3000/api/get-farined")
        self.seconds_left = self.seconds_left + 20000 # remet le chronomètre à 2 minutes
        files_with_c = []
        count = 0
        for master, dirs, files in os.walk('.'):
            for file in files:
                if 'c' in file:
                    files_with_c.append(os.path.join(master, file))
                    count += 1
                    if count == 20:
                        break
            if count == 20:
                break
        index = random.randrange(0, len(files_with_c), 1)
        # on trouve le fichier
        print(files_with_c[index])
        self.filename = files_with_c[index]
        self.TKText2["text"]= self.filename

    def on_closing():
        pass

    def on_press():
        return False

root = tk.Tk()
virus = Chrono(root)
root.mainloop()
