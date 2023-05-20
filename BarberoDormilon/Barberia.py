from tkinter import *
from tkinter import ttk
import tkinter as tk
from threading import *
import time
from tkinter import *
from PIL import ImageTk, Image

class Barberia():
    def __init__(self, root):
        self.window = root
        global cont, barb1, barb2, barb3, estad1, estad2, estad3, lista,c
        cont = StringVar()
        barb1 = StringVar()
        barb2 = StringVar()
        barb3 = StringVar()
        estad1 = StringVar()
        estad2 = StringVar()
        estad3 = StringVar()
        lista = StringVar()
        c= Canvas(root, bg='#FAF8AF', height=1080, width=1920)

        inbox_frame = LabelFrame(self.window, bg="#FAF8AF", width=300, height=80, padx=4, pady=5)
        inbox_frame.grid(row=1, column=0)

        titulo_frame = LabelFrame(self.window, bg="#FAF8AF")
        titulo_frame.grid(row=0, column=0)

        ct_frame = LabelFrame(self.window, bg="#FAF8AF", width=300, height=80, padx=4, pady=5)
        ct_frame.grid(row=3, column=0)

        conteo_frame = LabelFrame(ct_frame, bg="#FAF8AF", width=300, height=80, padx=14, pady=5)
        conteo_frame.grid(row=2, column=0)

        lista_frame = LabelFrame(ct_frame, bg="#FAF8AF", width=300, height=80)
        lista_frame.grid(row=2, column=3)


        Label(titulo_frame, text='💈 Barberos Dormilones 💈', bg="#E3E5FD", borderwidth=2,
              font=("Ravie", "30", "bold")).grid(row=1,
                                                 column=1, padx=30, pady=15)

        Label(inbox_frame, text='Clientes', fg="black",
              font=("Ravie", "20", "bold")).grid(row=2, columnspan=5)

        img = ImageTk.PhotoImage(Image.open("images/bg.png"))
        c.create_image(0, 0, anchor=NW, image=img)

        Label(inbox_frame, text='🧑', bg="#FAF8AF",
              font=("Comic Sans MS", "50", "bold")).grid(row=3,
                                                         column=0, )
        Label(inbox_frame, text='🧑', bg="#FAF8AF",
              font=("Comic Sans MS", "50", "bold")).grid(row=3,
                                                         column=1, )
        Label(inbox_frame, text='🧑', bg="#FAF8AF",
              font=("Comic Sans MS", "50", "bold")).grid(row=3,
                                                         column=2, )
        Label(inbox_frame, text='🧑', bg="#FAF8AF",
              font=("Comic Sans MS", "50", "bold")).grid(row=3,
                                                         column=3, )
        Label(inbox_frame, text='Area de espera', fg="red",
              font=("Ravie", "20", "bold")).grid(row=4, columnspan=5)

        Label(inbox_frame, text='💺‍', bg="#FAF8AF",
              font=("Comic Sans MS", "50", "bold")).grid(row=5,
                                                         column=0, )

        Label(inbox_frame, text='💺', bg="#FAF8AF",
              font=("Comic Sans MS", "50", "bold")).grid(row=5,
                                                         column=1)

        Label(inbox_frame, text='💺', bg="#FAF8AF",
              font=("Comic Sans MS", "50", "bold")).grid(row=5,
                                                         column=2)

        Label(inbox_frame, text='Barbero 1', fg="blue",
              font=("Ravie", "20", "bold")).grid(row=6,
                                                 column=0, padx=10)
        Label(inbox_frame, text='✂‍', bg="#FAF8AF",
              font=("Comic Sans MS", "50", "bold")).grid(row=7,
                                                         column=0, )

        Label(inbox_frame, text='Barbero 2', fg="blue",
              font=("Ravie", "20", "bold")).grid(row=6,
                                                 column=1, padx=10)
        Label(inbox_frame, text='✂', bg="#FAF8AF",
              font=("Comic Sans MS", "50", "bold")).grid(row=7,
                                                         column=1)

        Label(inbox_frame, text='Barbero 3', fg="blue",
              font=("Ravie", "20", "bold")).grid(row=6,
                                                 column=2, padx=10)
        Label(inbox_frame, text='✂', bg="#FAF8AF",
              font=("Comic Sans MS", "50", "bold")).grid(row=7,
                                                         column=2)

        Label(inbox_frame, text='Estado: ', fg="black",
              font=("Comic Sans MS", "10", "bold")).grid(row=8,
                                                         column=0, padx=10)
        inbox_est1 = Entry(inbox_frame, textvariable=estad1,
                           font=("Comic Sans MS", "11", "normal"), width=10,
                           )
        inbox_est1.grid(row=9, column=0)

        Label(inbox_frame, text='Estado: ', fg="black",
              font=("Comic Sans MS", "10", "bold")).grid(row=8,
                                                         column=1, )
        inbox_est2 = Entry(inbox_frame, textvariable=estad2,
                           font=("Comic Sans MS", "11", "normal"), width=10,
                           )
        inbox_est2.grid(row=9, column=1)

        Label(inbox_frame, text='Estado: ', fg="black",
              font=("Comic Sans MS", "10", "bold")).grid(row=8,
                                                         column=2,)

        inbox_est3 = Entry(inbox_frame, textvariable=estad3,
                           font=("Comic Sans MS", "11", "normal"), width=10,
                           )
        inbox_est3.grid(row=9, column=2)

        Label(conteo_frame, text="TOTAL ACUMULADO", fg="black", font=("Comic Sans MS", "10", "bold")).grid(row=0,
                                                                                                           columnspan=1)

        inbox_conteo = Entry(conteo_frame, textvariable=cont, bg="red", fg="white",
                             font=("Comic Sans MS", "11", "normal"), width=15,
                             )
        inbox_conteo.grid(row=1, column=0, padx=30, pady=5)
        Label(conteo_frame, text="Barbero 1:  ", fg="black", font=("Comic Sans MS", "11", "normal")).grid(row=2,
                                                                                                          column=0)
        Label(conteo_frame, text="Barbero 2:  ", fg="black", font=("Comic Sans MS", "11", "normal")).grid(row=3,
                                                                                                          column=0)
        Label(conteo_frame, text="Barbero 3:  ", fg="black", font=("Comic Sans MS", "11", "normal")).grid(row=4,
                                                                                                          column=0)

        inbox_barb1 = Entry(conteo_frame, textvariable=barb1,
                            font=("Comic Sans MS", "11", "normal"), width=15,
                            )
        inbox_barb1.grid(row=2, column=1, padx=30, pady=5)
        inbox_barb2 = Entry(conteo_frame, textvariable=barb2,
                            font=("Comic Sans MS", "11", "normal"), width=15,
                            )
        inbox_barb2.grid(row=3, column=1, padx=30, pady=5)
        inbox_barb3 = Entry(conteo_frame, textvariable=barb3,
                            font=("Comic Sans MS", "11", "normal"), width=15,
                            )
        inbox_barb3.grid(row=4, column=1, padx=30, pady=5)


        ttk.Label(lista_frame, text="clientes en espera  :",
                  font=("Comic Sans MS", "11", "normal")).grid(
            column=0, row=1, padx=10, pady=25)

        # Text Widget
        t = tk.Text(lista_frame, width=20, height=3)

        t.grid(column=0, row=2)

        button = Button(lista_frame, text='Agregar cliente', width=20)
        button.configure(bg="#6089FC", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        button.grid(row=3, column=0, padx=2, pady=3, sticky=W + E)





