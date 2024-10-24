import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl  # Importa QUrl

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Cria uma instância do QWebEngineView
        self.browser = QWebEngineView()
        
        # Define a URL a ser aberta usando QUrl
        self.browser.setUrl(QUrl("https://excalidraw.com/#room=94f13a20bb5853a067da,fNwFyeZE8ZLrWmvx-68sMQ"))

        # Define a janela principal
        self.setCentralWidget(self.browser)
        self.setWindowTitle("Excalidraw Browser")
        self.setGeometry(100, 100, 1200, 800)  # Tamanho da janela

        # Exibe a janela
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    sys.exit(app.exec_())
