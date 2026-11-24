import sys
from PyQt5.QtWidgets import QApplication
from ToDoList import ToDoList


app=QApplication(sys.argv)
ventana=ToDoList()
ventana.show()
sys.exit(app.exec())