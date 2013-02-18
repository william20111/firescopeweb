import logging
import sys
import suds
from PyQt4 import QtCore, QtGui
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
    def __init__(self,parent=None):
        
	QtGui.QMainWindow.__init__(self,parent)
        self.resize(400,340)
	self.ciEditLine = QtGui.QLineEdit(self)
	self.ciEditLine.move(20,0)
        self.monitorEditLine = QtGui.QLineEdit(self)
	self.monitorEditLine.move(20,35)
        self.bolEditLine = QtGui.QLineEdit(self)
	self.bolEditLine.move(20,70)
        self.dnsEditLine = QtGui.QLineEdit(self)
	self.dnsEditLine.move(20,105)
	self.ipEditLine = QtGui.QLineEdit(self)
	self.ipEditLine.move(20,140)
	self.tmpEditLine = QtGui.QLineEdit(self)
	self.tmpEditLine.move(20,175)
	self.tmpopEditLine = QtGui.QLineEdit(self)
	self.tmpopEditLine.move(20,210)
	self.createButton = QtGui.QPushButton(self)
        self.createButton.move(20,245)
        self.createButton2 = QtGui.QPushButton(self)
        self.createButton2.move(20, 280)

	####BUTTON SIGNALS####
	QtCore.QObject.connect(self.createButton,QtCore.SIGNAL("clicked()"), self.create_srv)
	QtCore.QObject.connect(self.createButton2,QtCore.SIGNAL("clicked()"), self.create_tmp)
	
	####LABELS####
	self.monitorLabel = QtGui.QLabel(self)
	self.monitorLabel.move (130,35)
	self.ciLabel = QtGui.QLabel(self)
	self.ciLabel.move(130,0)
	self.ipLabel = QtGui.QLabel(self)
	self.ipLabel.move(130,140)
	self.bolLabel = QtGui.QLabel(self)
	self.bolLabel.move(130,70)
	self.dnsLabel = QtGui.QLabel(self)
	self.dnsLabel.move(130,105)
	self.tmpLabel = QtGui.QLabel(self)
	self.tmpLabel.move(130,175)
	self.tmpopLabel = QtGui.QLabel(self)
	self.tmpopLabel.move(130,210)
	
	####LABELS#####
	self.monitorLabel.setText(QtGui.QApplication.translate("From", "MONITORED", None, QtGui.QApplication.UnicodeUTF8))
	self.ciLabel.setText(QtGui.QApplication.translate("Form", "CI Name", None, QtGui.QApplication.UnicodeUTF8))
        self.bolLabel.setText(QtGui.QApplication.translate("Form", "useIP=True / False", None, QtGui.QApplication.UnicodeUTF8))
        self.ipLabel.setText(QtGui.QApplication.translate("Form", "IP Address", None, QtGui.QApplication.UnicodeUTF8))
        self.createButton.setText(QtGui.QApplication.translate("Form", "Create", None, QtGui.QApplication.UnicodeUTF8))
	self.dnsLabel.setText(QtGui.QApplication.translate("Form", "DNS Name", None, QtGui.QApplication.UnicodeUTF8))
	self.createButton2.setText(QtGui.QApplication.translate("Form", "Create Temp",None, QtGui.QApplication.UnicodeUTF8))
	self.tmpLabel.setText(QtGui.QApplication.translate("Form", "Template",None, QtGui.QApplication.UnicodeUTF8))
	self.tmpopLabel.setText(QtGui.QApplication.translate("Form", "CREATE UPDATE",None, QtGui.QApplication.UnicodeUTF8))
	
    def create_srv(self):
        try:
                response = client.service.createConfigurationItem(self.ciEditLine.text(), self.monitorEditLine.text(), self.bolEditLine.text(), self.dnsEditLine.text(), self.ipEditLine.text())
                print response
        except WebFault, e:
                print e
	

    def create_tmp(self):
	try:
		response = client.service.linkTemplate(self.tmpEditLine.text(), self.ciEditLine.text(), self.tmpopEditLine.text())
		print response
	except WebFault, e:
		print e

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
