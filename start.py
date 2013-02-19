import logging
import sys
import suds
from PyQt4 import QtCore, QtGui
from suds.wsse import *

token = UsernameToken("webservices", "password")
security = Security()
security.tokens.append(token)
url = "http://firescopetest:8048/services/FireScopeConfigurationWebService/v1?wsdl"
client = suds.client.Client(url)
client.set_options(wsse = security)


class StartQT4(QtGui.QMainWindow):
    def __init__(self,parent=None):
        
	QtGui.QMainWindow.__init__(self,parent)
        self.setWindowIcon(QtGui.QIcon('firescope.png'))
	self.setMouseTracking(True)
        self.setWindowTitle('Firescope Web Services')    
#	self.menuBar = QtGui.QMenuBar(self)
#	self.menuBar.move(0,400)
	
	self.resize(400,400)
	self.ciEditLine = QtGui.QLineEdit(self)
	self.ciEditLine.move(20,35)
        self.monitorEditLine = QtGui.QLineEdit(self)
	self.monitorEditLine.move(20,70)
        self.bolEditLine = QtGui.QLineEdit(self)
	self.bolEditLine.move(20,105)
        self.dnsEditLine = QtGui.QLineEdit(self)
	self.dnsEditLine.move(20,140)
	self.ipEditLine = QtGui.QLineEdit(self)
	self.ipEditLine.move(20,175)
	self.tmpEditLine = QtGui.QLineEdit(self)
	self.tmpEditLine.move(20,210)
	self.tmpopEditLine = QtGui.QLineEdit(self)
	self.tmpopEditLine.move(20,245)
	self.logEditLine = QtGui.QLineEdit(self)
	self.logEditLine.move(20,280)
	self.createButton = QtGui.QPushButton(self)
        self.createButton.move(20,315)
        self.createButton2 = QtGui.QPushButton(self)
        self.createButton2.move(20,350)
	self.delButton = QtGui.QPushButton(self)
	self.delButton.move(130,315)
	self.createButton3 = QtGui.QPushButton(self)
	self.createButton3.move(130,350)
	self.createButton4 = QtGui.QPushButton(self)
	self.createButton4.move(240, 315)

	####BUTTON SIGNALS####
	QtCore.QObject.connect(self.createButton,QtCore.SIGNAL("clicked()"), self.create_srv)
	QtCore.QObject.connect(self.createButton2,QtCore.SIGNAL("clicked()"), self.create_tmp)
	QtCore.QObject.connect(self.delButton,QtCore.SIGNAL("clicked()"), self.del_ci)
	QtCore.QObject.connect(self.createButton3,QtCore.SIGNAL("clicked()"), self.create_log)
	QtCore.QObject.connect(self.createButton4,QtCore.SIGNAL("clicked()"), self.create_srv_grp)
	
	####LABELS####
	self.monitorLabel = QtGui.QLabel(self)
	self.monitorLabel.move (130,70)
	self.ciLabel = QtGui.QLabel(self)
	self.ciLabel.move(130,35)
	self.ipLabel = QtGui.QLabel(self)
	self.ipLabel.move(130,175)
	self.bolLabel = QtGui.QLabel(self)
	self.bolLabel.move(130,105)
	self.dnsLabel = QtGui.QLabel(self)
	self.dnsLabel.move(130,140)
	self.tmpLabel = QtGui.QLabel(self)
	self.tmpLabel.move(130,210)
	self.tmpopLabel = QtGui.QLabel(self)
	self.tmpopLabel.move(130,245)
	self.logLabel = QtGui.QLabel(self)
	self.logLabel.move(130,280)
	
	####LABELS####
	self.bolLabel.setText(QtGui.QApplication.translate("Form", "useIP=True", None, QtGui.QApplication.UnicodeUTF8))
        self.ipLabel.setText(QtGui.QApplication.translate("Form", "IP Address", None, QtGui.QApplication.UnicodeUTF8))
        self.createButton.setText(QtGui.QApplication.translate("Form", "Create CI", None, QtGui.QApplication.UnicodeUTF8))
	self.dnsLabel.setText(QtGui.QApplication.translate("Form", "DNS Name", None, QtGui.QApplication.UnicodeUTF8))
	self.createButton2.setText(QtGui.QApplication.translate("Form", "Create Temp",None, QtGui.QApplication.UnicodeUTF8))
	self.tmpLabel.setText(QtGui.QApplication.translate("Form", "Template",None, QtGui.QApplication.UnicodeUTF8))
	self.tmpopLabel.setText(QtGui.QApplication.translate("Form", "CREATE UPDATE",None, QtGui.QApplication.UnicodeUTF8))
	self.delButton.setText(QtGui.QApplication.translate("Form", "Delete CI",None, QtGui.QApplication.UnicodeUTF8))
	self.createButton3.setText(QtGui.QApplication.translate("Form", "Create Logical", None, QtGui.QApplication.UnicodeUTF8))
	self.monitorLabel.setText(QtGui.QApplication.translate("Form", "MONITORED", None, QtGui.QApplication.UnicodeUTF8))
	self.ciLabel.setText(QtGui.QApplication.translate("Form", "CI Name", None, QtGui.QApplication.UnicodeUTF8))
	self.logLabel.setText(QtGui.QApplication.translate("Form", "Group",None, QtGui.QApplication.UnicodeUTF8))
	self.createButton4.setText(QtGui.QApplication.translate("Form", "Create Service",None, QtGui.QApplication.UnicodeUTF8))
	
    def create_srv(self):
	try:
                response = client.service.createConfigurationItem(self.ciEditLine.text(), self.monitorEditLine.text(), self.bolEditLine.text(), self.dnsEditLine.text(), self.ipEditLine.text())
		QtGui.QMessageBox.about(self, "Success", "Success")
        except WebFault, e:
		QtGui.QMessageBox.about(self, "Failed", "Failed")
	

    def create_tmp(self):
	try:
		response = client.service.linkTemplate(self.tmpEditLine.text(), self.ciEditLine.text(), self.tmpopEditLine.text())
		QtGui.QMessageBox.about(self, "Success", "Success")
	except WebFault, e:
		QtGui.QMessageBox.about(self, "Failed", "Failed")

    def del_ci(self):
	try:
		response = client.service.deleteConfigurationItem(self.ciEditLine.text())
		QtGui.QMessageBox.about(self, "Success", "Success")
	except WebFault, e:
		QtGui.QMessageBox.about(self, "Failed", "Failed")

    def create_log(self):
	try:
		response = client.service.createLogicalGroup(self.logEditLine.text())
		QtGui.QMessageBox.about(self, "Success", "Success")
	except Webfault, e:
		QtGui.QMessageBox.about(self, "Failed", "Failed")
    def create_srv_grp(self):
	try:
		response = client.service.createServiceGroup(self.logEditLine.text())
		QtGui.QMessageBox.about(self, "Success", "Success")
        except Webfault, e:
                QtGui.QMessageBox.about(self, "Failed", "Failed")

#    def checkText(self):
#        if self._before != self.text():
#            self._before = self.text()
#            self.textModified.emit(self._before, self.text())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
