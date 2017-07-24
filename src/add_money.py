import sys
from PyQt5.QtWidgets import QMessageBox, QWidget, QTreeWidgetItem
from PyQt5 import uic
from banks import Banks
sys.path.append("./lib")
from func_aux import str_to_float
from bbdd import Bbdd


class AddMoney(QWidget):
	def __init__(self, mainWindows):
		QWidget.__init__(self)
		uic.loadUi("../ui/add_money.ui", self)
		self.mainWindows = mainWindows
		mainWindows.aNew.triggered.connect(mainWindows.newBank)
		self.mainWindows.setWindowTitle("Añadir fondos | Betcon v" + mainWindows.version)
		self.btnAccept.clicked.connect(self.accept)
		self.btnCancel.clicked.connect(self.cancel)
		#self.txtMoney.returnPressed.connect(self.btnAccept.click)

	def close(self):
			self.mainWindows.setCentralWidget(Banks(self.mainWindows))

	def cancel(self):
		self.close()

	def accept(self):
		type = self.cmbType.currentIndex()
		if type == 0:
			type="+"
		else:
			type="-"

		data = ["'+bank"+type+"'"+str(str_to_float(self.txtMoney.text()))]
		columns = ["bank"]

		account = self.cmbAccount.currentIndex()

		bbdd = Bbdd()
		bbdd.update(columns, data, "bank", "id="+str(account+1))
		bbdd.close()

		QMessageBox.information(self, "Añadido", "Fondos añadidos.")

		self.close()
