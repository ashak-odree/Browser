from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

class Browser(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Odree Browser")

        self.web_view = QtWebEngineWidgets.QWebEngineView(self)
        self.setCentralWidget(self.web_view)

        self.web_view.load(QtCore.QUrl("http://www.google.com"))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    browser = Browser()
    browser.show()
    app.exec_()
