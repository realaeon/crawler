from ui import Ui_Dialog
import sys
from PyQt4.QtGui import QApplication, QDialog

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
