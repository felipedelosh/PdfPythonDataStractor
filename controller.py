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
        self.config_v1_tokens = ["NUMERO DE CONTENEDOR", "BOOKING", "ORDEN DE COMPRA", "HORA EMISION", "FECHA EMISION", "PLACA DEL VEHICULO", "PLACA DE CARRETA"]

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
        
    
    def getALLPagesNamesOfCurrentData(self):
        if self._txt_data == {}:
            return []
        
        data = []
        for i in self._txt_data:
            data.append(i)

        return data
    
    def getTxtData(self, key):
        txt = ""

        try:
            txt = self._txt_data[key]
        except:
            pass

        return txt
    

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


    def proceesAllInformationToExcelV1(self):
        # EXCEL
        _EXCEL = ""
        _EXCEL_HEADER = ""
        _EXCEL_DATA = {}
        for i in self.config_v1_tokens:
            _EXCEL_HEADER = _EXCEL_HEADER + i + "|"
            _EXCEL_DATA[i] = []


        # READ ALL TEXT and save in _EXCEL_DATA
        for iterPAGE in self._txt_data:
            for iterLINE in str(self._txt_data[iterPAGE]).split("\n"):
                if str(iterLINE).strip() != "": 
                    if self.config_v1_tokens[0] in iterLINE:
                        _nro_contenedor = iterLINE.split(":")[1]
                        _nro_contenedor = _nro_contenedor.strip()
                        _EXCEL_DATA[self.config_v1_tokens[0]].append(_nro_contenedor)
                        


                    if self.config_v1_tokens[1] in iterLINE:
                        _booking = iterLINE.split(":")[1]
                        _booking = _booking.strip()
                        _EXCEL_DATA[self.config_v1_tokens[1]].append(_booking)
                       


                    if self.config_v1_tokens[2] in iterLINE:
                        _nro_buy_order = iterLINE.split(":")[1]
                        _nro_buy_order = _nro_buy_order.strip()
                        _EXCEL_DATA[self.config_v1_tokens[2]].append(_nro_buy_order)
                        
   

                    if self.config_v1_tokens[3] in iterLINE:
                        _hour = iterLINE.split(": ")[1]
                        _hour = _hour.strip()
                        _EXCEL_DATA[self.config_v1_tokens[3]].append(_hour)
                       


                    if self.config_v1_tokens[4] in iterLINE:
                        _date = iterLINE.split(": ")[1]
                        _date = _date.strip()
                        _EXCEL_DATA[self.config_v1_tokens[4]].append(_date)
                        


                    if self.config_v1_tokens[5] in iterLINE:
                        _id_vehicle = iterLINE.split(": ")[1]
                        _id_vehicle = _id_vehicle.strip()
                        _EXCEL_DATA[self.config_v1_tokens[5]].append(_id_vehicle)
                        


                    if self.config_v1_tokens[6] in iterLINE:
                        _id_way = iterLINE.split(": ")[1]
                        _id_way = _id_way.strip()
                        _EXCEL_DATA[self.config_v1_tokens[6]].append(_id_way)
        

        len_data = len(_EXCEL_DATA)
        _final_data = ""

        for i in range(0, len_data):
            print(i)


            

            
