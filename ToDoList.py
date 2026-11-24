from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import os

class ToDoList(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        ruta_ui = os.path.join(os.path.dirname(__file__), "ToDoList.ui")
        uic.loadUi(ruta_ui, self)
        self.btnAgregar.clicked.connect(self.AgragarTarea)
        self.btnEliminar.clicked.connect(self.EliminarTarea)
        self.btnActualizar.clicked.connect(self.ActualizarTarea)
        self.lstTareas.itemClicked.connect(self.CargarTareaSelect)


    def AgragarTarea(self):
        tarea=self.edtTarea.text().strip()
        if not tarea:
            QMessageBox.warning(self, "Advertencia", "No se puede agregar una tarea vacía.")
            self.edtTarea.clear()
            self.edtTarea.setFocus()
            return
        self.lstTareas.addItem(tarea)
        self.edtTarea.clear()
        self.edtTarea.setFocus()

    def ActualizarTarea(self):
        indiceTareaActualizar=self.lstTareas.currentRow()
        tareaActualizar=self.edtTarea.text()
        nuevoTexto=self.edtTarea.text().strip()
        if not nuevoTexto:
            QMessageBox.warning(self, "Texto invalido", "No se puede actualizar a una tarea vacía ni solo contener solo espacios.")
            self.edtTarea.clear()
            self.edtTarea.setFocus()
            return
        self.lstTareas.item(indiceTareaActualizar).setText(tareaActualizar)
        self.edtTarea.clear()
        self.edtTarea.setFocus()

    def CargarTareaSelect(self):
        itemSelec=self.lstTareas.currentItem()
        if itemSelec:
            self.edtTarea.setText(itemSelec.text())

    def EliminarTarea(self):
        indiceTareaBorrar=self.lstTareas.currentRow()
        self.lstTareas.takeItem(indiceTareaBorrar)







#holaaaaaaas 😸 MARCAS DE AGUAAAA 😺krn😺