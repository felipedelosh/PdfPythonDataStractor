"""
FELIPEDELOSH - 2024

WARNING: you need install:


Enter a PDF files in folder: PDF
"""
from tkinter import *
from tkinter import ttk
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
        self.btnSaveAllPDFInTXTPages = Button(self.canvas, text="SAVE ALL IN TXT", command=self.saveAllInTXT)
        self.btnViewALLText = Button(self.canvas, text="VIEW ALL TEXT", command=self.viewALLFilesInfo)
        self.btnSaveEXCELv1 = Button(self.canvas, text="SAVE EXCEL V1", command=self.saveExcelVr1)
        self.lblFooterProgram = Label(self.canvas, text="FelipedelosH")
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

        #self.btnSaveAllPDFInTXTPages.place(x=self.controller.w*0.05, y=self.controller.h*0.4)
        #self.btnViewALLText.place(x=self.controller.w*0.3, y=self.controller.h*0.4)
        #self.btnSaveEXCELv1.place(x=self.controller.w*0.5, y=self.controller.h*0.4)
        
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
                self.btnViewALLText.place(x=self.controller.w*0.3, y=self.controller.h*0.4)
                self.btnSaveEXCELv1.place(x=self.controller.w*0.5, y=self.controller.h*0.4)
            else:
                self.btnChargeTXTData['bg'] = "red"
                self.btnSaveAllPDFInTXTPages.place_forget()
                self.btnViewALLText.place_forget()
                self.btnSaveEXCELv1.place_forget()


    def saveAllInTXT(self):
        if self.controller._txt_data == {}:
            self.btnSaveAllPDFInTXTPages['bg'] = "red"
        else:
            self.btnSaveAllPDFInTXTPages['bg'] = "green"
            self.controller.saveAllInTXT()

    def viewALLFilesInfo(self):
        if self.controller._txt_data == {}:
            self.btnViewALLText['bg'] = "red"
        else:
            self.btnViewALLText['bg'] = "green"

            # SHOW MINI WINDOW
            t = Toplevel(self.screem)
            t.geometry("640x480")
            t.title("PDF TEXT")
            _data_combo = self.controller.getALLPagesNamesOfCurrentData()
            combo = ttk.Combobox(t, values=_data_combo)
            combo.place(x=260, y=20) 
            text = Text(t, width=77, height=23)
            text.insert(END, "CHANGE A OPTION TO READ TEXT...")
            text.place(x=10, y=50)

            if len(_data_combo) > 0:
                combo.current(0)

            combo.bind("<<ComboboxSelected>>", lambda event: self.changeVisorPage(event.widget.get(), text))


    def changeVisorPage(self, event, TEXT_WIDGET):
        TEXT_WIDGET.delete("1.0", END)
        txt = self.controller.getTxtData(event)
        TEXT_WIDGET.insert(END, txt)


    def saveExcelVr1(self):
        if self.controller._txt_data == {}:
            self.btnSaveEXCELv1['bg'] = "red"
        else:
            self.btnSaveEXCELv1['bg'] = "green"
            self.controller.proceesAllInformationToExcelV1()
        

s = Software()
