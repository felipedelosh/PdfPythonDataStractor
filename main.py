"""
FELIPEDELOSH - 2024

WARNING: you need install:


Enter a PDF files in folder: PDF
"""
from tkinter import *
from controller import *

class Software:
    def __init__(self) -> None:
        self.controller = Controller()
        self.screem = Tk()
        self.canvas = Canvas(self.screem)
        self.lblBannerProgram = Label(self.canvas, text="Total PDF files in folder: ???")
        self.lblHelpToStart = Label(self.canvas, text="Paso 1: Leer todos los archivos de la carpeta \"PDF\"")
        self.btnReadAllFiles = Button(self.canvas, text="READ FILES", command=self.btnReadAllFiles)
        self.lblHelpToChargeData = Label(self.canvas, text="Paso 2: Analizar todos los textos encontrados en PDF")
        self.btnChargeTXTData = Button(self.canvas, text="CHARGE DATA", command=self.btnChargeTXTData)
        self.lblFooterProgram = Label(self.canvas, text="FelipedelosH")

        self.btnSaveAllPDFInTXTPages = Button(self.canvas, text="SAVE ALL IN TXT", command=self.saveAllInTXT)

        self.vizualizedAndRun()


    def vizualizedAndRun(self):
        self.screem.title("Program Title")
        self.screem.geometry(f"{self.controller.w}x{self.controller.h}")
        self.canvas['width'] = self.controller.w
        self.canvas['height'] = self.controller.h
        self.canvas['bg'] = "snow"
        self.canvas.place(x=0, y=0)
        self.lblBannerProgram.place(x=self.controller.w*0.02, y=self.controller.h*0.02)
        self.lblHelpToStart.place(x=self.controller.w*0.18, y=self.controller.h*0.11)
        self.btnReadAllFiles.place(x=self.controller.w*0.04, y=self.controller.h*0.1)
        self.lblHelpToChargeData.place(x=self.controller.w*0.18, y=self.controller.h*0.22)
        self.btnChargeTXTData.place(x=self.controller.w*0.04, y=self.controller.h*0.21)
        self.lblFooterProgram.place(x=self.controller.w*0.45, y=self.controller.h*0.9)

        
        self.screem.mainloop()


    def btnReadAllFiles(self):
        if self.controller.btnReadAllFiles():
            self.btnReadAllFiles['bg'] = "green"
            self.lblBannerProgram['text'] = f"Total PDF files in folder: {len(self.controller._PDF_FILES_PATH)}"
            self.lblHelpToStart['text'] =  "Paso 1: Leer todos los archivos de la carpeta \"PDF\" CORRECTO."
        else:
            self.btnReadAllFiles['bg'] = "red"
            self.lblBannerProgram['text'] = "Total PDF files in folder: ERROR OR NOT FOUND FILES"
            self.lblHelpToStart['text'] =  "Paso 1: NO SE LEYERON LOS ARCHIVOS DE LA CARPERA \"PDF\""


    def btnChargeTXTData(self):
        if len(self.controller._PDF_FILES_PATH) == 0:
            self.btnChargeTXTData['bg'] = "red"
            self.lblHelpToChargeData['text'] = "Paso 2: ERROR NO SE ENCONTRARON .PDF en la CARPETA \"PDF\""
        else:
            self.controller.btnChargeTXTData()

            if self.controller._txt_data != {}:
                self.btnChargeTXTData['bg'] = "green"
                self.btnSaveAllPDFInTXTPages.place(x=self.controller.w*0.05, y=self.controller.h*0.4)
            else:
                self.btnChargeTXTData['bg'] = "red"
                self.btnSaveAllPDFInTXTPages.place_forget()


    def saveAllInTXT(self):
        if self.controller._txt_data == {}:
            self.btnSaveAllPDFInTXTPages['bg'] = "red"
        else:
            self.btnSaveAllPDFInTXTPages['bg'] = "green"
            self.controller.saveAllInTXT()
        

s = Software()
