#-*- coding: utf8 -*-
from Tkinter import *
import tkFileDialog
from parser import Parser

class CreateGui():
    def __init__(self):
        root = Tk()
        self.template_file = ""
        self.label_text = StringVar()
        win = Frame(root)
        win.pack()
        Button(win,text=u"Выбрать шаблон", command = self.openTemplate).pack()
        Label(win,text=u"Hey",textvariable = self.label_text).pack()
        Button(win,text = u"Сгенерировать шаблоны",command =self.generateTemplates ).pack()
        mainloop()
    def openTemplate(self):
        self.template_file = tkFileDialog.askopenfilename()
        self.label_text.set(self.template_file)

    def generateTemplates(self):
        if self.template_file:
            parser = Parser(self.template_file)
            parser.generateTemplates()
        else:
            self.label_text.set("Укажите путь к шаблону!")


if __name__ == "__main__":
    CreateGui()



