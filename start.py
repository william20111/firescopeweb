import logging
import sys
import suds
from PyQt4 import QtCore, QtGui, QtNetwork
from service import Ui_Form
from suds.wsse import *

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("suds.client").setLevel(logging.CRITICAL)
url = "http://firescopetest:8048/services/FireScopeConfigurationWebService/v1?wsdl"
token = UsernameToken("webservices", "password")
security = Security()
security.tokens.append(token)

client = suds.client.Client(url)
client.set_options(wsse = security)

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.createButton,QtCore.SIGNAL("clicked()"), self.create_srv)
        self.ciEditLine = QtGui.QLineEdit()
        self.monitorEditLine = QtGui.QLineEdit()
        self.bolEditLine = QtGui.QLineEdit() 
        self.ipEditLine = QtGui.QLineEdit()



    def create_srv(self):
        try:
                response = client.service.createConfigurationItem(self.ciEditLine.text(), self.monitorEditLine.text(), self.bolEditLine.text(), self.ipEditLine.text())
                print response
        except WebFault, e:
                print e





if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
