from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

class ToDoList(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ToDoList.ui", self)
        self.btnAgregar.clicked.connect(self.AgragarTarea)
        self.btnEliminar.clicked.connect(self.EliminarTarea)


    def AgragarTarea(self):
        tarea=self.edtTarea.text()
        self.lstTareas.addItem(tarea)
        self.edtTarea.clear()
        self.edtTarea.setFocus()
        #TODO AGERAGAR VALIDACION PARA QUE NO SE AGREGUEN TAREAS VACIAS
        

    def EliminarTarea(self):
        indiceTareaBorrar=self.lstTareas.currentRow()
        self.lstTareas.takeItem(indiceTareaBorrar)












        # indice=self.lstTareas.currentRow()
        # QMessageBox.information(self, "Notificacion", f"La tarea presionada es la que tiene el indice: {indice}")
    
        # #self.lstTareas.takeItem(indice)