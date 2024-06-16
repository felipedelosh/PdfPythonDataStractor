"""
FelipedelosH



"""
import os
from os import scandir # To read all files in folder
# Python -m pip install PyMuPDF 
import fitz # To read PDF text

class Controller:
    def __init__(self) -> None:
        self.w = 720
        self.h = 480
        self._PDF_FILES_PATH = []
        self._txt_data = {}

    def rtnArcheveInfo(self, path):
        info = None
        try:
            f = open(path, 'r', encoding="utf-8")
            return f.read()
        except:
            return info


    def rtnArchieveFilesNames(self, folder, extension):
        """
        Return all files names of data folder
        """
        try:
            path = os.getcwd() + "/" + folder

            filesNames = []
            for i in scandir(path):
                if i.is_file():
                    if extension in i.name:
                        filesNames.append(i.name)

            return filesNames
        except:
            return None
        
    

    def btnReadAllFiles(self):
        self._PDF_FILES_PATH = self.rtnArchieveFilesNames("PDF", ".pdf")
        return len(self._PDF_FILES_PATH) > 0
    

    def btnChargeTXTData(self):
        for i in self._PDF_FILES_PATH:
            _iterPdfPath = f"PDF/{i}"
            document = fitz.open(_iterPdfPath)
            # Read all Text
            for num_page in range(document.page_count):
                pdf_page = document[num_page]
                txt = pdf_page.get_text()

                # Save
                self._txt_data[i + str(num_page)] = txt


    def saveAllInTXT(self):
        for i in self._txt_data:
            _final_file_name = str(i).replace(".pdf", "-") # Erase .pdf of final txt

            # Save a file
            with open("output/"+_final_file_name+".txt", "w",  encoding="UTF-8") as f:
                f.write(self._txt_data[i])
