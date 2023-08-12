
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QGridLayout,QLabel,QComboBox,QTextEdit,QPushButton,QApplication,QWidget
from PySide6.QtCore import Qt


from Deepl import deepl_API

MAIN_STYLE ="""
background-color:#0E1112

"""

TEXTEEDIT_STYLE ="""
background-color:#1c1f26;
border-radius:20px;
color:#f1f1f1;
font-size:20px;
"""
                       
TEXTEEDIT_STYLE2 ="""
background-color:#6364A8;
border-radius:20px;
"""

LABEL_STYLE ="""
font-size:30px;
background-color:#1c1f26;
color:#f1f1f1;
border-radius:20px;
""" 

BUTTON = '''
QPushButton {
    font-weight: bold;
    padding: 0 5px;
    background-color: #001e63;
    border-radius: 10px;
    font-size:20px;
    color:#f1f1f1
}
QPushButton:pressed {
    background-color: rgb(80, 80, 80);
}
'''

LANGUAGE ="""
background-color:#1c1f26;
color:#f1f1f1;
border-radius: 10px;
font-size:20px;"""

lang = {
"Bulgarian":"BG" ,
"Czech":"CS",
"Danish":"DA",
"German":"DE",
"Greek":"EL",
"English":"EN",
"Spanish":"ES",
"Estonian":"ET",
"Finnish":"FI",
"French":"FR",
"Hungarian":"HU",
"Indonesian":"ID",
"Italian":"IT",
"Japanese":"JA",
"Korean":"KO",
"Lithuanian":"LT",
"Latvian":"LV",
"Norwegian":"NB",
"Dutch":"NL",
"Polish":"PL",
"Portuguese":"PT",
"Romanian":"RO",
"Russian":"RU",
"Slovak":"SK",
"Slovenian":"SL",
"Swedish":"SV",
"Turkish":"TR",
"Ukrainian":"UK",
"Chinese":"ZH",}



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.has_changed = True

        self.width = 900
        self.height = 600

        self.setWindowTitle("Traducteur")
        self.setBaseSize(self.width,self.height)
        self.setStyleSheet(MAIN_STYLE)
        
        self.mainlayout = QGridLayout(self)
        self.mainlayout.setSpacing(12)
        self.mainlayout.setContentsMargins(20,20,20,20)

        self.title = QLabel("Traducteur")
        self.title.setStyleSheet(LABEL_STYLE)
        self.title.setAlignment(Qt.AlignCenter)

        self.combo = QComboBox()
        self.combo.setStyleSheet(LABEL_STYLE)
        for name,code in lang.items():
            self.combo.addItem(name, userData=code)
        self.combo.setCurrentIndex(5)

        self.text_edit_input = QTextEdit()
        self.text_edit_input.setStyleSheet(TEXTEEDIT_STYLE)
        self.text_edit_input.setPlaceholderText("Entrez du Texte")

        self.text_edit_output = QTextEdit()
        self.text_edit_output.setStyleSheet(TEXTEEDIT_STYLE)

        self.icon = QIcon("ressources/fleche.png")
        self.icon_label = QLabel()
        self.icon_label.setPixmap(self.icon.pixmap(64, 64))

        self.generatebutton = QPushButton("Generate")
        self.generatebutton.setStyleSheet(BUTTON)

        self.label_language_detected = QLabel("Language détécté: ")
        self.label_language_detected.setAlignment(Qt.AlignCenter)
        self.label_language_detected.setStyleSheet(LANGUAGE)

        self.mainlayout.addWidget(self.text_edit_input,1,1)
        self.mainlayout.addWidget(self.text_edit_output,1,3)
        self.mainlayout.addWidget(self.title,0,1)
        self.mainlayout.addWidget(self.combo,0,3)
        self.mainlayout.addWidget(self.icon_label,1,2)
        self.mainlayout.addWidget(self.generatebutton,2,3)
        self.mainlayout.addWidget(self.label_language_detected,2,1)
        
        self.generatebutton.clicked.connect(self.translate)
        self.combo.currentIndexChanged.connect(self.update)
        self.combo.currentIndexChanged.connect(self.translate)
        self.text_edit_input.textChanged.connect(self.update)

    def translate(self):
        data = {}
        self.text = self.text_edit_input.toPlainText()
        self.language = self.combo.currentText()

        if self.text and self.has_changed == True:
            data["text"] = self.text
            data["target_lang"] = lang[self.language]

            response = deepl_API(data)
            content = response["translations"][0]["text"]
            language_detected = response["translations"][0]["detected_source_language"]
            
            self.text_edit_output.setText(content)
            self.label_language_detected.setText(f'Language détécté: {language_detected}')
            self.has_changed = False

    def update(self):
        self.has_changed = True
            

app = QApplication()

window = MainWindow()
window.show()

app.exec()