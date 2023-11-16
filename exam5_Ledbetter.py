#--------------------------------------------------------------------------------------------------------------------------------------
# Project Name: exam5_Ledbetter.py
# Assignment: Exam 5 - GUI application to calculate distance traveled at speed and number of hours.
# Description: Loads a Qt Toolkit .ui file with the graphical interface, implements lListWidget and push buttons to control input and processing. 
# Author: Tiffany Ledbetter
#Date: 11/12/2023
#-------------------------------------------------------------------------------------------------------------------------------------
import sys                        # needed for the sys.argv passed to QApplication below (command line arguments)

from PyQt6.QtWidgets import QDialog, QApplication, QInputDialog, QFileDialog 
from PyQt6.uic import loadUi
from PyQt6.QtCore import QFileInfo
from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtGui import QPainter
# special library to load .ui file directly

class MyForm(QDialog):
    # constructor for this MyForm class 
    def __init__(self):
        super().__init__()   # calls the constructor of the QDialog class that is inherited
        
        # Change 'gui_template.ui' to the .ui file you created with Qt Designer
        # or rename the provided gui_template.ui to your own file and change name
        # the .ui file MUST BE IN THE SAME FOLDER AS THIS .PY FILE
        self.ui = loadUi('exam5_Ledbetter.ui', self)   #<======= this line must be changed to your .UI file!
        
        self.ui.pushButtonExit.clicked.connect( self.exitMethod)
        self.ui.pushButtonCalc.clicked.connect( self.calcMethod)
        self.ui.pushButtonPDF.clicked.connect( self.PDFMethod)
        # add code here to connect the pushButton widgets to your methods.
        # for this first project three empty methods are already created.
        # you are responsible for connecting the clicked signal from your widgets
        
    def calcMethod(self):
        travDist, okPressed = QInputDialog.getInt(self, "Enter Speed", "Speed in MPH:" , 2, 60, 480, 2)
        numHour, okPressed = QInputDialog.getInt(self, "Enter Hours", "Hours Traveled:" , 1, 5, 25, 1)
        if not okPressed:
            return
        
        listWidgetOut = self.ui.listWidgetOut
        listWidgetOut.addItem("Vehicle Speed: " + str(travDist) )
        listWidgetOut.addItem("Time Traveled: " + str(numHour) )
        listWidgetOut.addItem("\n Hours 	Distance Travled" )
        for i in range(1, numHour + 1):
            listWidgetOut.addItem(str(i) + "\t" + str( travDist * i) )
        
        totalDist = travDist * numHour
        listWidgetOut.addItem("Total Distance: " + str( totalDist) )
    
    def PDFMethod(self):
        file_name, okPressed = QFileDialog.getSaveFileName(self, caption ="Export PDF", directory=None, \
                                                          filter ="PDF Files((*.pdf);;All Files(*.*)")
        if file_name != "":
            if QFileInfo(file_name).suffix() =="":
                file_name += ".pdf"
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(file_name)
            painter = QPainter(printer)
            painter.begin(printer)
            screenPixmap = self.listWidgetOut.grab()
            screenPixmap = screenPixmap.scaledToWidth( int(screenPixmap.width() * 8000/screenPixmap.width() ) )
            painter.drawPixmap(10, 10, screenPixmap )
            painter.end()
            
        
        
        
    def exitMethod(self):
        # the following code quits the application.
        # It is connected to the Exit push button in the
        # constructor above.
        QApplication.instance().quit()
        
        
print("\nEnd of Distance Traveled Exam 5, Original Work of: Tiffany Ledbetter" )
# the code below should not be changed and is constant for all GUI programs
if __name__=="__main__":    
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()         
    sys.exit(app.exec())  # note - sys.exit causes traceback in some editors if it does in yours just use app.exec()
