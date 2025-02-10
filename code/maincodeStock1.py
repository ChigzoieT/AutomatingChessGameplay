from playwright.sync_api import sync_playwright
#from undetected_playwright import sync_playwright
import threading
import random
import sys
import multiprocessing
from multiprocessing import Process
import json
import ctypes
import re
import firebase_admin
from firebase_admin import db, credentials
from PyQt5.QtWidgets import QCheckBox, QScrollArea, QApplication, \
     QWidget, QVBoxLayout, QHBoxLayout, QLabel, QStyledItemDelegate,  \
     QPushButton, QFrame, QHBoxLayout, QLineEdit, QDesktopWidget,  QComboBox 
from PyQt5.QtCore import Qt, QSize, pyqtSignal, QObject,  QThread, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QFont, QCursor, QFontDatabase
import speedtest
import time
import os
import subprocess
import traceback
#from playwright_stealth import stealth_sync
from undetected_playwright import stealth_sync

state = "inactive"

sec = 1000000000
ms = 10000000
sleeper_dll = ctypes.CDLL('C:/Users/algorithm/lichess_driver/sleeper.dll')
sleep_ns = sleeper_dll.sleep_ns
sleep_ns.argtypes = [ctypes.c_longlong]
sleep_ns.restype = None



cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL" : "https://xyz-7c8de-default-rtdb.firebaseio.com/"})

best = "variation-view-column best"
good = "variation-view-column good"
inaccuracy = "variation-view-column inaccuracy"
mistake = "variation-view-column mistake"
blunder = "variation-view-column blunder"
orientation = 'div[class*="cg-wrap"]'
trigz = 0

cur_poslichess = ["0"]
prev_poslichess = ["0"]
lichesscombined = []
terminate = 1

data_key = 7
callkey = 0
cookiecode = 0
d1 = ["0", "68", "132", "198", "264", "330", "396", "462"]
d2 = ["462", "396", "330", "264", "198", "132", "68", "0"]

a = {"a1": [d1[0], d2[0]], "a2": [d1[0], d2[1]], "a3": [d1[0], d2[2]], "a4": [d1[0], d2[3]], "a5": [d1[0], d2[4]], "a6": [d1[0], d2[5]], "a7": [d1[0], d2[6]], "a8": [d1[0], d2[7]]}
b = {"b1": [d1[1], d2[0]], "b2": [d1[1], d2[1]], "b3": [d1[1], d2[2]], "b4": [d1[1], d2[3]], "b5": [d1[1], d2[4]], "b6": [d1[1], d2[5]], "b7": [d1[1], d2[6]], "b8": [d1[1], d2[7]]}
c = {"c1": [d1[2], d2[0]], "c2": [d1[2], d2[1]], "c3": [d1[2], d2[2]], "c4": [d1[2], d2[3]], "c5": [d1[2], d2[4]], "c6": [d1[2], d2[5]], "c7": [d1[2], d2[6]], "c8": [d1[2], d2[7]]}
d = {"d1": [d1[3], d2[0]], "d2": [d1[3], d2[1]], "d3": [d1[3], d2[2]], "d4": [d1[3], d2[3]], "d5": [d1[3], d2[4]], "d6": [d1[3], d2[5]], "d7": [d1[3], d2[6]], "d8": [d1[3], d2[7]]}
e = {"e1": [d1[4], d2[0]], "e2": [d1[4], d2[1]], "e3": [d1[4], d2[2]], "e4": [d1[4], d2[3]], "e5": [d1[4], d2[4]], "e6": [d1[4], d2[5]], "e7": [d1[4], d2[6]], "e8": [d1[4], d2[7]]}
f = {"f1": [d1[5], d2[0]], "f2": [d1[5], d2[1]], "f3": [d1[5], d2[2]], "f4": [d1[5], d2[3]], "f5": [d1[5], d2[4]], "f6": [d1[5], d2[5]], "f7": [d1[5], d2[6]], "f8": [d1[5], d2[7]]}
g = {"g1": [d1[6], d2[0]], "g2": [d1[6], d2[1]], "g3": [d1[6], d2[2]], "g4": [d1[6], d2[3]], "g5": [d1[6], d2[4]], "g6": [d1[6], d2[5]], "g7": [d1[6], d2[6]], "g8": [d1[6], d2[7]]}
h = {"h1": [d1[7], d2[0]], "h2": [d1[7], d2[1]], "h3": [d1[7], d2[2]], "h4": [d1[7], d2[3]], "h5": [d1[7], d2[4]], "h6": [d1[7], d2[5]], "h7": [d1[7], d2[6]], "h8": [d1[7], d2[7]]}

variants = ["3check", "antichess", "atomic", "standard", "crazyhouse", "kingofthehill"]
nnues = ["3check-313cc226a173.nnue", "antichess-689c016df8e0.nnue", "atomic-2cf13ff256cc.nnue", "nn-46832cfbead3.nnue", "crazyhouse-8ebf84784ad2.nnue", "kingofthehill-978b86d0e6a4.nnue"]


dictx = [a, b, c, d, e, f, g, h]
dicta = ["a", "b", "c", "d", "e", "f", "g", "h"]
color = ""
dictrr = 0
values = [".signin", "#form3-username", "#form3-password", ".submit", "orientation", "classList", "orientation-white", "orientation-black", ".last-move", "style", "transform: ", "transform: translate(0px, 0px);", "white", "black", "a[class = 'user-link']"]
currentlastmoveindexposition = 14
currentindexposition = 4
text = ["you play white", "you play black", "reload driver please/navigate to lichess.org", "move-dest", "piece"]
currentindexpositionnow = 5
movesarr = ["0", "0"]
claszz = ["board-piece", "board-destination", "pawn", "piece"]
tagz = ["div", "img"]
bestpos = [["0", "0"], ["0", "0"]]
lastvalues = ["0", "0"]
lock = threading.Lock()
position = "best"
clasz = ""
global_dict = {}
usernames = ["", ""]
verifier = 0
roomid = ""
coast = ""
username = ""
password = ""
analysisstate = "none"
analysiscode = "play"
total = ""
correctmove = []
chain = 0
variant = "standard"
nnue_file = "nn-46832cfbead3.nnue"
enginecode = 0
kickstarterkey = 0
compassstate = 0
callstate = 0
lichessstate = 0 
movestray = []
call_event = threading.Event()
analyze_event = threading.Event()
cookie_data = {}
styles = ""
#num_bits = 14
bit_mask = (1 << num_bits) - 1
row = "" #either short or long
wkingside = "e1g1"
wqueenside = "e1c1"
bkingside = "e8g8"
bqueenside = "e8c8"

def compute_bitmask(num_bits):
        return (1 << num_bits) - 1


def castle_lookupw():
        global wkingside, wqueenside, movestray, row
        if row == "short":
                movestray.pop()
                movestray.append(wkingside)
        else:
                movestray.pop()
                movestray.append(wqueenside)

def castle_lookupb():
        global bqueenside, bkingside, movestray, row
        if row == "short":
                movestray.pop()
                movestray.append(bkingside)
        else:
                movestray.pop()
                movestray.append(bqueenside)

def color_locator():
        global color
        if color == "white" and verifier != 1:
                castle_lookupb()
        elif color == "white" and verifier == 1:
                castle_lookupw()

        if color == "black" and verifier != 1:
                castle_lookupw()

        elif color == "black" and verifier == 1:
                castle_lookupb()

def promotion():
        global movestray
        string = f"{movestray[-1]}q"
        movestray.pop()
        movestray.append(string)


def calleset():
        call_event.set()

def anaeset():
        analyze_event.set()

def increks():
        global kickstarterkey
        with lock:
                kickstarterkey += 1

def increcallkey():
        global callkey
        with lock:
                if callkey == 0:
                        callkey += 1

def deccallkey():
        global deccallkey
        with lock:
                if callkey == 1:
                        callkey -=1

def terminateapp():
        global compassstate, callstate
        with lock: 
                compassstate += 1
                callstate += 1
                lichessstate += 1

def codelock():
        global analysiscode
        with lock:
                analysiscode = text

def coastlock(text):
        with lock:
                coast = text

def analysislock(text):
        global analysisstate
        with lock:
                analysisstate = text

def calllock(text):
        global state
        with lock:
                state = text


def test_download_speed():
        st = speedtest.Speedtest()
        download_speed = st.download()
        download_speed_kbps = download_speed / 1_0000  # Convert from bits per second to kilobits per second

        if download_speed_kbps < 500:
                return 0

        else:
                return 1


def set_room(meetlink):
        global roomid, global_dict
        ref = db.reference(privateroom)
        ref.set({
                "roomid": roomid
                })


def get_room():
        global roomid, global_dict
        ref = db.reference(privateroom)
        linkin = ref.get()
        if linkin and "roomid" in linkin:
                return linkin["roomid"]


def clear_room():
        ref = db.reference(privateroom)
        ref.delete()


def write_data(file_dict):
        with open("data.json", "w") as file:
                json.dump(file_dict, file, indent = 4)
                file.close()


def load_data():
        global global_dict, username, password, cookiecode
        with open("data.json", "r") as file:
                global_dict =  json.load(file)
                username = global_dict["username"]
                password = global_dict["password"]
                cookiecode = global_dict["cookiecode"]
                file.close()

def write_cookiedata(cookie_data):
        #global cookie_data
        with open("cookie.json", "w") as cook:
                json.dump(cookie_data, cook, indent = 4)
                cook.close()

def read_cookedata():
        global cookie_data
        with open("cookie.json", "r") as cook:
                cookie_data =  json.load(cook)
                cook.close()


def update_cookie():
        global file_dict
        file_dict["cookiecode"] = 1
        with open("data.json", "w") as f:
                json.dump(file_dict)
                f.close()


class WelcomeWindow(QWidget):
        def __init__(self):
                super().__init__()
                self.initUI()


        def initUI(self):
                self.setWindowTitle('ChessMod')
                self.setWindowIcon(QIcon('knight.png'))
                self.setStyleSheet("background-color: white;")

                screen = QDesktopWidget().screenGeometry()
                self.setGeometry(0, 0, screen.width() // 3, screen.height() // 3)
                self.center()

                font_id = QFontDatabase.addApplicationFont('PTSerif-Regular.ttf')
                font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
                custom_font = QFont(font_family, 30)

                self.text_label = QLabel('Welcome', self)
                self.text_label.setFont(custom_font)
                self.text_label.setAlignment(Qt.AlignCenter)

                layout = QVBoxLayout()
                layout.addWidget(self.text_label)
                self.setLayout(layout)


        def center(self):
                qr = self.frameGeometry()
                cp = QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())

        def close_window(self):
                self.close()



class ConnectionCheckWindow(QWidget):
        def __init__(self):
                super().__init__()
                self.initUI()

        def initUI(self):
                self.setWindowTitle('ChessMod')
                self.setWindowIcon(QIcon('knight.png'))
                self.setGeometry(100, 100, 300, 150)
                self.setStyleSheet("background-color: white;")
                self.center()


                font_id = QFontDatabase.addApplicationFont('PTSerif-Regular.ttf')
                font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
                custom_font = QFont(font_family, 12)


                self.error_label = QLabel('ChessMod Initialization Failing...', self)
                self.error_label.setFont(custom_font)
                self.error_label.setAlignment(Qt.AlignCenter)
                self.error_label.setStyleSheet('color: red')

                self.label = QLabel('Please verify the stability of your internet connection.', self)
                self.label.setFont(custom_font)

                self.image_label = QLabel(self)
                self.image_label.setPixmap(QPixmap('cloud.png'))

                h_layout = QHBoxLayout()
                h_layout.addWidget(self.image_label)
                h_layout.addWidget(self.label)


                main_layout = QVBoxLayout()
                main_layout.addWidget(self.error_label)
                main_layout.addLayout(h_layout)
                self.setLayout(main_layout)


                self.ellipsis_timer = QTimer(self)
                self.ellipsis_timer.timeout.connect(self.updateEllipsis)
                self.ellipsis_state = 0
                self.ellipsis_timer.start(500)


        def center(self):
                qr = self.frameGeometry()
                cp = QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())


        def updateEllipsis(self):
                ellipsis_states = ['.', '..', '...']
                self.error_label.setText(f'ChessMod Initialization Failing{ellipsis_states[self.ellipsis_state]}')
                self.ellipsis_state = (self.ellipsis_state + 1) % len(ellipsis_states)


        def close_window(self):
                self.close()



class DisclaimerWindow(QWidget):
        def __init__(self):
                super().__init__()
                self.initUI()

        def initUI(self):
                self.setWindowTitle('Chess Mod Disclaimer')
                self.setGeometry(100, 100, 650, 700)

                layout = QVBoxLayout()
                disclaimer_text = """
                <h3>Disclaimer for Chess Mod</h3>
                <ul>
                <li><b>General Information</b>
                <p>Chess Mod is a browser and web-driven application. While we strive to ensure that our app provides accurate and up-to-date information, we cannot guarantee the completeness, reliability, or suitability of the data and functionality provided.</p></li>
                
                <li><b>Functionality and Availability</b>
               <p>The app is provided "as is" and "as available" without any warranties, expressed or implied. We do not guarantee that the app will be error-free or uninterrupted. Periodic updates will be implemented to enhance performance and ensure optimal functionality.</p></li>

                <li><b>Accuracy of Information</b>
                <p>We make every effort to ensure the accuracy and reliability of the information provided through Chess Mod. However, we make no representations or warranties regarding the accuracy, completeness, or timeliness of the information. Users should independently verify any information before relying on it.</p></li>

                <li><b>Third-Party Links and Services</b>
                <p>We have used third-party links according to protocol. However, we have no control over and assume no responsibility for the content, privacy policies, or practices of any third-party websites or services. Accessing third-party links is at your own risk.</p></li>

                <li><b>Limitation of Liability</b>
                <p>To the fullest extent permitted by law, we disclaim any liability for any direct, indirect, incidental, consequential, or special damages arising out of or in any way connected with the use of or inability to use Chess Mod, including but not limited to any errors or omissions in the content.</p></li>


                <li><b>User Responsibility</b>
                <p>Users are responsible for ensuring that their use of Chess Mod complies with all applicable laws and regulations. Any use of the app’s content or functionality for illegal purposes is strictly prohibited.</p></li>

                <li><b>Changes to the Disclaimer</b>
                <p>We reserve the right to modify this disclaimer at any time without prior notice. Any changes will be effective immediately upon posting the updated disclaimer within the app. Your continued use of Chess Mod constitutes acceptance of the revised disclaimer.</p></li>


                <li><b>Contact Information</b>
                <p>If you have any questions or concerns about this disclaimer, please contact us at [Your Contact Information].</p></li>


                </ul>

                """

                disclaimer_label = QLabel(disclaimer_text)
                disclaimer_label.setWordWrap(True)
                disclaimer_label.setFont(QFont('Arial', 12))
                disclaimer_label.setFixedWidth(580)

                scroll_area = QScrollArea()
                scroll_area.setWidgetResizable(True)
                scroll_area.setWidget(disclaimer_label)


                self.checkbox = QCheckBox('I accept the terms and conditions')
                self.checkbox.stateChanged.connect(self.checkbox_toggled)

                self.accept_button = QPushButton('Accept')
                self.accept_button.setEnabled(False)
                self.accept_button.clicked.connect(self.accept_clicked)


                button_layout = QHBoxLayout()
                button_layout.addWidget(self.checkbox)
                button_layout.addWidget(self.accept_button)


                layout.addWidget(scroll_area)
                layout.addLayout(button_layout)

                self.setLayout(layout)

        

        def checkbox_toggled(self):
                self.accept_button.setEnabled(self.checkbox.isChecked())


        def accept_clicked(self):
                self.close()



def disclaimer():
        app = QApplication(sys.argv)
        disclaim = DisclaimerWindow()
        disclaim.show()
        return app.exec_()




class GetDetails(QWidget):
        def __init__(self):
                super().__init__()

                self.Details()


        def Details(self):
                self.setWindowTitle('ChessMod')
                self.setGeometry(100, 100, 500, 300) 
                self.setWindowIcon(QIcon('knight.png'))

                self.setStyleSheet("background-color: white;")

                font_id = QFontDatabase.addApplicationFont('PTSerif-Regular.ttf')
                font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
                custom_font = QFont(font_family, 12)


                layout = QVBoxLayout()

                font = QFont()
                font.setPointSize(14) 


                self.inputField1 = QLineEdit(self)
                self.inputField1.setPlaceholderText('Enter Lichess username')
                self.inputField1.setFont(font)
                self.inputField1.setFixedSize(500, 40)

                self.inputField2 = QLineEdit(self)
                self.inputField2.setPlaceholderText('Enter Lichess password...')
                self.inputField2.setEchoMode(QLineEdit.Password)
                self.inputField2.setFont(font)
                self.inputField2.setFixedSize(500, 40)


                self.submitButton = QPushButton('Submit', self)
                self.submitButton.setFont(font)
                self.submitButton.setFixedSize(250, 40)
                self.submitButton.setStyleSheet("""
                        QPushButton {
                        background-color: black;
                        border-radius: 20px;
                        border: none;
                        color: white;

                        }
                        QPushButton:hover {
                        background-color: #404040;
                        }

                        """)
                self.submitButton.clicked.connect(self.showInput)


                layout.addWidget(self.inputField1)
                layout.addWidget(self.inputField2)
                layout.addWidget(self.submitButton)

                self.setLayout(layout)


        def showInput(self):
                global global_dict, file_dict, cookiecode
                text = "saved"
                lichess_username = self.inputField1.text()
                lichess_password = self.inputField2.text()
                if lichess_username != None and lichess_password != None:
                        file_dict = {"username":lichess_username, "password": lichess_password, "cookiecode":cookiecode}
                        global_dict = {"username":lichess_username, "password": lichess_password, "cookiecode":cookiecode}
                        write_data(file_dict)
                        with open("file.txt", "w") as f:
                                f.write(text)

                        sleep_ns(sec)
                        self.close()


class CustomComboBox(QComboBox):
        def __init__(self, parent=None):
                super().__init__(parent)
                self.setItemDelegate(ItemDelegate(self))

        def showPopup(self):
                super().showPopup()
                self.view().viewport().setCursor(QCursor(Qt.PointingHandCursor))


class ItemDelegate(QStyledItemDelegate):
        def helpEvent(self, event, view, option, index):
                view.viewport().setCursor(QCursor(Qt.PointingHandCursor))
                return super().helpEvent(event, view, option, index)


class CustomWindow(QWidget):
        def __init__(self):
                self.active = "active"
                self.play = "play"
                self.pause = "pause"
                self.hangup = "hangup"
                self.muteaudio = "muteaudio"
                super().__init__()
                self.initUI()


        def initUI(self):
                self.setWindowTitle('ChessMod')
                self.setWindowIcon(QIcon('knight.png'))

                font_id = QFontDatabase.addApplicationFont('PTSerif-Regular.ttf')
                font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
                custom_font = QFont(font_family, 12)


                screen_geometry = QApplication.desktop().screenGeometry()
                window_width, window_height = 300, 250
                x_pos = screen_geometry.width() - window_width - 10
                x_pos = max(0, min(x_pos, screen_geometry.width() - window_width))
                y_pos = 40
                self.setGeometry(x_pos, y_pos, window_width, window_height)


                self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
                self.setStyleSheet("background-color:white;")

                layout = QVBoxLayout()
                container = QFrame()
                container_layout = QVBoxLayout(container)

                self.dropdown = CustomComboBox()
                self.dropdown.addItems(["3check", "antichess", "atomic", "standard", "crazyhouse", "kingofthehill"])
                self.dropdown.setStyleSheet(f"""
                        QComboBox {{
                        background-color: white;
                        font-size: 14px;
                        border: 2px solid black;
                        border-radius: 5px;
                        padding: 5px;
                        }}

                        QComboBox::drop-down {{
                        subcontrol-origin: padding;
                        subcontrol-position: top right;
                        width: 15px;
                        border-left-width: 1px;
                        border-left-color: black;
                        border-left-style: solid;
                        border-top-right-radius: 5px;
                        border-bottom-right-radius: 5px;

                        }}
                        /* Remove the custom dropdown arrow image */
                        QComboBox::down-arrow {{
                        image: url(downa.png);
                        height: 20px;
                        width: 20px;
                        }}
                        """)
                self.dropdown.currentIndexChanged.connect(self.on_dropdown_item_selected)
                container_layout.addWidget(self.dropdown, alignment=Qt.AlignCenter)

                self.controls_label = QLabel("Controls")
                self.controls_label.setAlignment(Qt.AlignCenter)
                self.controls_label.setFont(custom_font)
                container_layout.addWidget(self.controls_label, alignment=Qt.AlignCenter)
                button_layout = QHBoxLayout()

                self.playbtn = QPushButton()
                self.playbtn.setIcon(QIcon("play.png"))
                self.playbtn.setIconSize(QSize(30, 30))
                self.playbtn.setStyleSheet("""

                        QPushButton {
                        border: 2px solid black;
                        border-radius: 25px;

                        }


                        QPushButton:hover {
                        background-color: #FAF9F6;
                        }

                        QPushButton:pressed {
                        background-color: lightgray;
                        }

                        """)

                self.playbtn.setCursor(QCursor(Qt.PointingHandCursor))
                self.playbtn.setFixedSize(50, 50)
                self.playbtn.setFont(custom_font)
                self.playbtn.clicked.connect(self.play_button)
                button_layout.addWidget(self.playbtn)

                self.pausebtn = QPushButton()
                self.pausebtn.setIcon(QIcon("pause.png"))
                self.pausebtn.setIconSize(QSize(30, 30))
                self.pausebtn.setStyleSheet("""
                        QPushButton {
                        border: 2px solid black; 
                        border-radius: 25px;
                        }


                        QPushButton:hover {
                        background-color: #FAF9F6;
                        }

                        QPushButton:pressed {
                        background-color: lightgray;
                        }

                        """)

                self.pausebtn.setCursor(QCursor(Qt.PointingHandCursor))
                self.pausebtn.setFixedSize(50, 50)
                self.pausebtn.setFont(custom_font)
                self.pausebtn.clicked.connect(self.pause_button)
                button_layout.addWidget(self.pausebtn)
                self.stopbtn = QPushButton()
                self.stopbtn.setIcon(QIcon("stop.png"))
                self.stopbtn.setIconSize(QSize(30, 30))
                self.stopbtn.setStyleSheet("""
                        QPushButton {
                        border: 2px solid black; 
                        border-radius: 25px;
                        }
                        QPushButton:hover {
                        background-color: #FAF9F6;
                        }


                        QPushButton:pressed {
                        background-color: lightgray;
                        }
                        """)


                self.stopbtn.setCursor(QCursor(Qt.PointingHandCursor))
                self.stopbtn.setFixedSize(50, 50)
                self.stopbtn.setFont(custom_font)
                self.stopbtn.clicked.connect(self.stop_button)
                button_layout.addWidget(self.stopbtn)

                container_layout.addLayout(button_layout)
                container_layout.addSpacing(20)
                additional_button_layout = QHBoxLayout()

                self.muteun = QPushButton()
                self.muteun.setIcon(QIcon('micoff.png'))
                self.muteun.setIconSize(QSize(30, 30))
                self.muteun.setStyleSheet("""
                        QPushButton {
                        border: 2px solid black; 
                        border-radius: 25px;
                        }

                        QPushButton:hover {
                        background-color: #FAF9F6;
                        }

                        QPushButton:pressed {
                        background-color: lightgray;
                        }

                        """)
                self.muteun.setCursor(QCursor(Qt.PointingHandCursor))
                self.muteun.setFixedSize(50, 50)
                self.muteun.clicked.connect(self.mutun_button)
                additional_button_layout.addWidget(self.muteun)

                self.cutcall = QPushButton()
                self.cutcall.setIcon(QIcon("call.png"))
                self.cutcall.setIconSize(QSize(30, 30))
                self.cutcall.setStyleSheet("""

                        QPushButton {
                        border: 2px solid black; 
                        border-radius: 25px;
                        }

                        QPushButton:hover {
                        background-color: #FAF9F6;
                        }

                        QPushButton:pressed {
                        background-color: lightgray;
                        }
                        """)

                self.cutcall.setCursor(QCursor(Qt.PointingHandCursor))
                self.cutcall.setFixedSize(50, 50)
                self.cutcall.clicked.connect(self.cutcall_button)
                additional_button_layout.addWidget(self.cutcall)
                container_layout.addLayout(additional_button_layout)

                specials_layout = QHBoxLayout()

                self.short_button = QPushButton("shrt")
                self.long_button = QPushButton("lng")
                self.promote_button = QPushButton("promotion")

                specials_layout.addWidget(self.short_button)
                specials_layout.addWidget(self.long_button)
                specials_layout.addWidget(self.promote_button)

                button_style = """
                QPushButton {
                border-radius: 10px;
                border: 1px solid black;
                padding: 10px;
                }
                QPushButton:hover {
                background-color: lightgray;
                }
                """

                self.short_button.setStyleSheet(button_style)
                self.short_button.setCursor(QCursor(Qt.PointingHandCursor))
                self.short_button.setFont(custom_font)
                self.short_button.clicked.connect(self.short)

                self.long_button.setStyleSheet(button_style)
                self.long_button.setCursor(QCursor(Qt.PointingHandCursor))
                self.long_button.setFont(custom_font)
                self.long_button.clicked.connect(self.long)

                self.promote_button.setStyleSheet(button_style)
                self.promote_button.setCursor(QCursor(Qt.PointingHandCursor))
                self.promote_button.setFont(custom_font)
                self.promote_button.clicked.connect(self.promote)

                specials_layout.addSpacing(10)

                container_layout.addWidget(specials_layout, alignment=Qt.AlignCenter)

                layout.addWidget(container)
                self.setLayout(layout)


        def on_dropdown_item_selected(self, index):
                global variant, nnue_file, enginecode
                selected_item = self.dropdown.itemText(index)
                variant = variants[index]
                nnue_file = nnues[index]
                with lock:
                        enginecode == 1


        def play_button(self):
                codelock(self.play)


        def pause_button(self):
                codelock(self.pause)


        def stop_button(self):
                terminateapp()
                time.sleep(2)
                self.close()

        def cutcall_button(self):
                global state
                if state == self.active:
                        increcallkey()
                        calllock(self.hangup)

        def mutun_button(self):
                global state
                if state == self.active:
                        increcallkey()
                        calllock(self.muteaudio)

        def short(self):
                global row
                row = "short"
                color_locator()

        def long (self):
                global row
                row = "long"
                color_locator()

        def promote(self):
                promotion()

class lichess:
        def __init__(self, page, values, claszz, browser, context):
                self.page = page
                self.claszz =claszz
                self.active = "active"
                self.white = "white"
                self.black = "black"
                self.values = values
                self.browser = browser
                self.context = context
                self.a = 71
                self.b = 91
                self.p = 211
                self.bucket_list =  [[] for _ in range(211)]
                self.values_list =  [[] for _ in range(211)]
                self.values_listb = [[] for _ in range(211)]
                self.valid = "#89CFF0"
                self.color = ""
                self.c12 = compute_bitmask(14)
                self.c36 = compute_bitmask(29)
                self.n36 = 29
                self.n12 = 14
                self.n1 = 1
                self.n0 = 0
                self.n2 = 2
                self.speclookw = [["a8", ""], ["b8", ""], ["c8", ""], ["d8", ""], ["e8", ""], ["f8", ""], ["g8", ""], ["h8", ""]]
                self.speclookb = [["a1", ""], ["b1", ""], ["c1", ""], ["d1", ""], ["e1", ""], ["f1", ""], ["g1", ""], ["h1", ""]]
                self.cur_array = []
                self.cur_pross = [""]
                self.prev_pross = [""]
                self.text_array = ["", ""]
                self.cur_poslichess = [""]
                self.prev_poslichess = [""]
                self.prev_array = ["", ""]
                self.styles = ["", ""]
                self.error_text = ""


        def stockback(self, retmove):
               for i in range(2):
                       move_data = retmove[i]
                       int_val = self.extract_bits(move_data, self.c12, self.n12)
                       move_details = self.check_in(self.bucket_list, int_val, move_data)
                       self.place_best(move_details[:3], move_details[3:], self.valid)
                       bestpos[i] = [move_details[:3], move_details[3:]]

        def special_lookuptable(self):
                global  d1
                x = 8
                y = 0
                while x!= 0:
                        x -= 1
                        self.speclookw[y][self.n1] ="transform: translate({}px);".format(d1[x])
                        self.speclookb[y][self.n1] ="transform: translate({}px);".format(d1[x])
                        y +=1

        def special_lookup(self, string, arr):
                y  = 0
                while arr[y][self.n1] != string:
                        y+=1
                return arr[y][self.n0]

        def movexcur(self, arr, string):
                int1 = self.extract_bits(string, self.c36, self.n36)
                self.cur_pross[0] = self.check_in(self.cur_array, int1, string)

        def movexprev(self, arr, string):
                int2 = self.extract_bits(string, self.c36, self.n36)
                self.prev_pross[0] = self.check_in(self.cur_array, int2, string)         

        def set_array(self):
                if self.color == self.white:
                        self.cur_array = self.values_list
                else:
                        self.cur_array = self.values_listb

        def format_moves(self, move1, move2):
                return "{}{}".format(move1, move2)

        def handle_verifier(self, total, validator):
                global movestray
                movestray.append(total)
                if validator != verifier and analysiscode != "pause":
                        analysislock("analyzemove")
                        self.wait_for_chain()

        def wait_for_chain(self):
                global chain, correctmove
                while True:
                        if chain == 1:
                                self.stockback(correctmove)
                                with lock:
                                        chain -= 1
                                        break
                        sleep_ns(ms)
                
        def transchesscompass(self, validator):
                global  total, analysiscode, correctmove
                #move1, move2 = self.get_moves_based_on_color()
                total = self.format_moves(self.prev_pross[0], self.cur_pross[0])
                print(total)
                #self.handle_verifier(total, validator)

        def retrievecookies(self):
                global cookiecode
                sleep_ns(sec*2)
                if cookiecode == 0:
                        cookies = self.context.cookies()
                        write_cookiedata(cookies[0])
                        update_cookie()

        def calc_hash(self, val):
                return ((val * self.b) + self.a) % self.p

        def check_in(self, arr, position, value):
                i = 0
                while arr[position][i][0] != value:
                        i+=1
                return arr[position][i][1]

        def  slot_in(self, arr, position, k,value):
                arr[position].append([k, value])

        def extract_bits(self, string, mask, num_bits):
                byte_data = string.encode('utf-8')
                data_int = int.from_bytes(byte_data, byteorder='big')
                length = data_int.bit_length()
                if length < 30:
                        padding_bits = 32 - length
                        data_int = (data_int << padding_bits)
                bottom = data_int & mask
                top = (data_int >> (data_int.bit_length() - num_bits)) & mask
                total = bottom + top
                return self.calc_hash(total)

        def appender(self):
                self.prev_array[0] = self.cur_poslichess[0]
                self.prev_array[1] = self.prev_poslichess[0]

        def handle_color(self, text, num, validator):
                if self.color == "white":
                        self.handle_error(text, num, self.speclookw,validator)
                        return
                self.handle_error(text, num, self.speclookb, validator)
                        
        def handle_error(self, text, num, arr,validator):
                if num == 0:
                        self.text_array[self.n0] = text
                        self.cur_pross[self.n0] = self.special_lookup(self.text_array[num], arr)
                elif num == 1:
                        self.text_array[self.n1] = text
                        self.prev_pross[self.n0] = self.special_lookup(self.text_array[num], arr)
                        self.transchesscompass(validator)

        def parsetext(self, text, num, validator):
                global d1, d2, data_key
                try:
                        matches = re.findall(r'[-+]?\d*\.\d+|\d+', text)
                        x = matches[0]
                        y = matches[1]
                        if num ==0:
                                self.cur_poslichess[0] = "{}{}".format(x, y)
                                self.movexcur(self.cur_array, self.cur_poslichess[0])
                                return
                        elif num == 1:
                                self.prev_poslichess[0] = "{}{}".format(x, y)
                                self.movexprev(self.cur_array, self.prev_poslichess[0])
                                if self.prev_array[0] == self.cur_poslichess[0] and self.prev_array[1] == self.prev_poslichess[0]:
                                        return
                                self.transchesscompass(validator)
                                self.appender()
                                return
                        elif num > 1:
                                d1[data_key] = f"{x}"
                                d2[data_key] = f"{x}"
                                data_key -=1                                
                except Exception as e:
                        #print("an error occured", text)
                        if self.error_text == text:
                                return
                        self.handle_color(text, num, validator)
                        self.error_text = text
                        return


        def forrevhash(self, clr):
                i = 0
                while i != 8:
                        for k, v in dictx[i].items():
                                position = self.extract_bits(k,self.c12 ,self.n12)
                                string = "{}{}".format(v[0], v[1])
                                self.slot_in(self.bucket_list, position,k,  string)
                                position1 = self.extract_bits(string,self.c36 ,self.n36)
                                if clr == 0:
                                        self.slot_in(self.values_list, position1, string,  k)
                                else:
                                        self.slot_in(self.values_listb, position1, string, k)

                        i+=1


        def place_best(self, height, width, color):
                global clasz, colored
                colored = 1
                selector = 'piece[class*="{}"][style*="transform: translate({}px, {}px);"]'.format(clasz, height, width)
                points = self.finder(selector, 1, 0)
                points.evaluate('(elem, color) => elem.style.backgroundColor = color', color)

        def remove_background_color(self):
                global clasz, bestpos
                for i in range(0, 2):
                        self.place_best(bestpos[i][0], bestpos[i][1], "")



        def modify_dict(self, num):
                global dictx, d1, d2
                if num == 1:
                        i = 7
                        for dicts in dictx:
                                q = 0
                                for key in dicts:
                                        value_lists = dicts[key]
                                        value_lists[1] = d1[q]
                                        value_lists[0] = d2[i]
                                        q+=1

                                i-=1

                elif num == 2:
                        i = 7
                        for dicts in dictx:
                                q = 0
                                for key in dicts:
                                        value_lists = dicts[key]
                                        value_lists[0] = d1[i]
                                        value_lists[1] = d2[q]
                                        q+=1

                                i-=1

        def finder(self, selector, data, terminator):
                while True:
                        try:
                                if data == 1:
                                        element = self.page.query_selector(selector)
                                        return element
                                elif data == 2:
                                        element = self.page.query_selector_all(selector)
                                        return element

                        except Exception as e:
                                if terminator == 1:
                                        return
                                print("an error occured")
                                sleep_ns(ms*50)
                                continue

        def find_positions(self):
                while True:
                        selector = f"{self.claszz[3]}.{self.claszz[2]}"
                        x = self.finder(selector, 2, 0)
                        r = 0
                        for i in x:
                                style_attrbute = i.get_attribute(self.values[9])
                                self.parsetext( style_attrbute, self.n2, None)
                                if r == 7:
                                        return
                                r+=1


                        sleep_ns(ms*5)

        def bb_locator(self, element):
                if element:
                        bb = element.bounding_box()
                        if bb:
                                x = bb['x'] + bb['width'] / 2
                                y = bb['y'] + bb['height'] / 2
                                return [x, y]

        def box_click(self, element, num, text):
                p = self.bb_locator(element)
                if num == 1:
                        self.page.mouse.move(p[0], p[1])
                        self.page.mouse.down()
                        self.page.mouse.up()
                        #self.page.mouse.click(p[0], p[1])

                elif num == 2:
                        self.page.mouse.move(p[0], p[1])
                        self.page.mouse.down()
                        self.page.mouse.move((p[0]+x), p[1])
                        self.page.mouse.up()

                elif num == 3:
                        self.page.mouse.move(p[0], p[1])
                        self.page.mouse.down()
                        self.page.mouse.up()
                        for char in text:
                                element.type(char, delay=random.uniform(0.1, 0.5))
                                time.sleep(random.uniform(0.05, 0.2))

        def lmaction(self, tur, vr, element):
                global verifier, colored
                xr = vr
                for i in element:
                        style_attrbute = i.get_attribute(self.values[9])
                        if tur == verifier:                         
                                if colored == 1:
                                        self.remove_background_color()
                                        colored -=1
                                self.parsetext(style_attrbute, xr, self.n1)
                                verifier += 1
                                        
                        elif tur != verifier and verifier != 0:
                                self.parsetext(style_attrbute, xr, self.n0)
                                verifier -= 1                                                 
                        xr+=1


        def lmretriever(self, tur):
                global db
                self.set_array()
                #selector = "a[class = 'fbt']"
                while True:
                        xr = 0
                        #new_opponent = self.finder(selector, 1, 1)
                        #if new_opponent:
                                #print("new_opponent")
                                #break

                        element = self.finder(self.values[8] ,2, 1)
                        if element:
                                self.lmaction(tur, xr, element)
                        sleep_ns(sec)
                enginelock(self.deactivated)

        def get_usernames(self):
                global usernames
                i = 0
                element = self.finder(self.values[14], 2, 0)
                for ele in element:
                        usernames[i] = ele.inner_text()
                        i+=1
                        print(usernames[i])


        def human_type(self, element_handle, text):
                for char in text:
                        element_handle.type(char, delay=random.uniform(0.8, 1.3))
                        time.sleep(random.uniform(0.05, 0.2))

        def code(self, color, num):
                self.color = color
                #callset()
                #calllock(active)
                #coastlock(color)
                self.lmretriever(num)


        def initializer(self, num, value, color, num1):
                self.find_positions()
                self.modify_dict(num)
                self.forrevhash(num1)
                clasz = value
                #self.printele()
                self.special_lookuptable()
                self.code(color, num1)

        def elementpresent(self, element):
                global trigw, coast, usernames, clasz, verifier, trigz
                class_attribute = element.get_attribute("class")
                if class_attribute:
                        class_list = class_attribute.split()
                        for x in class_list:
                                if x == self.values[6]:
                                        #self.get_usernames()
                                        verifer = self.n0
                                        if trigw == 0:
                                                self.initializer(self.n1, self.values[12], self.white, self.n0)
                                                trigw+=1
                                        else:
                                                self.code(self.white, self.n0)


                                elif x == self.values[7]:
                                        #self.get_usernames()
                                        verifier = self.n1
                                        if trigz == 0:                                           
                                                self.initializer(self.n2, self.values[13], self.black, self.n1)
                                                trigz+=1
                                        else:
                                                self.code(self.black, self.n1)

       
        def game_start_query(self):
                global orientation, trigz, clasz, usernames, coast
                while True:
                        element = self.finder(orientation, 1, 1)
                        if element:
                                self.elementpresent(element)
                        sleep_ns(sec)
                        print("orientation not found")


        def perform_signin(self, username, password):
                signin_element = self.finder(self.values[0], 1, 0)
                self.box_click(signin_element, 1, None)
                time.sleep(2)

                user_element = self.finder(self.values[1], 1, 0)
                self.box_click(user_element, 3, username)
                sleep_ns(sec)

                password_element = self.finder(self.values[2], 1, 0)
                self.box_click(password_element, 3, password)
                sleep_ns(2 * sec)

                enter_element = self.finder(self.values[3], 1, 0)
                self.box_click(enter_element, 1, None)
                time.sleep(5)



        def signin(self, username, password):
                global cookiecode
                #print(username, password)
                if cookiecode == 1:
                        self.game_start_query()
                
                else:
                        self.perform_signin(username, password)
                        self.retrievecookies()
                        self.game_start_query()



input_slider = ".input-range__slider"

class compass():
        global values, claszz
        def __init__(self, global_dict):
                self.global_dict = global_dict
                self.path = stockfish_path = 'C:\\Users\\algorithm\\Downloads\\fairy-stockfish-largeboard_x86-64'
                self.process = None
                self.moves = []
                self.threads = 2
                self.start_engine()
                self.configure_engine()

        def engine_on(self):
                while True:
                        analyze_event.wait()
                        self.state_ana()


        def state_ana(self):
                global total, enginecode, compassstate
                while True:
                        if analysisstate == "analyze":
                                self.make_move(total)
                                break

                        elif enginecode == 1:
                                self.configure_engine()
                                break

                        elif compassstate == 1:
                                self.close_engine()
                                break
                        sleep_ns(ms)


        def start_engine(self):
                creation_flags = subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
                self.process = subprocess.Popen(
                        [self.path],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True,
                        creationflags=creation_flags
                        )


        def configure_engine(self):
                global variant, nnue_file
                self.send_command('uci')
                while True:
                        response = self.get_response()
                        if response == "uciok":
                                print("Engine is ready")
                                break


                self.send_command('setoption name Use NNUE value true')
                self.send_command(f'setoption name EvalFile value {nnue_file}')
                self.send_command(f'setoption name UCI_Variant value {variant}')
                self.send_command(f'setoption name Threads value {self.threads}')
                self.send_command('isready')

                while True:
                        response = self.get_response()
                        if response == "readyok":
                                print("NNUE and variant are ready")
                                break
                self.engine_on()


        def send_command(self, command):
                if self.process:
                        self.process.stdin.write(command + '\n')
                        self.process.stdin.flush()


        def get_response(self):
                if self.process:
                        return self.process.stdout.readline().strip()

        """def append_move(self, move):
                self.moves.append(move)
                analysislock("none")"""


        def make_move(self, move):
                global correctmove, chain, movestray
                #self.moves.append(move)
                self.send_command(f'position startpos moves {" ".join(movestray)}')
                self.send_command(f'go movetime {self.movetime}')
                while True:
                        response = self.get_response()
                        if response.startswith('bestmove'):
                                move = response.split()[1]
                                source = move[:2]
                                destination = move[2:]
                                correctmove[0] = source
                                correctmove [1] = destination
                                with lock:
                                        chain +=1

                analysislock("none")
                analyze_event.clear()

        def close_engine(self):
                if self.process:
                        self.send_command('quit')
                        self.process.terminate()
                        self.process.wait()



#call_table = ['.breakpoints--desktop', '.zHQkBf', '#identifierNext', '#passwordNext', 'VfPpkd-LgbsSe-OWXEXe-k8QpJ', "li[aria-label='Create a meeting for later']", '.Hayy8b', "button[aria-label='Close dialog']", "input[type='text']", "button[jsname='r9ERUc']", "button[jsname='Qx7uuf']", "button[aria-label='Turn off microphone (ctrl + d)']", "button[aria-label='Leave call']", "button[jsname='oI7Fj']", "button[jsname='dqt8pb]", "button[jsname='BOHaEe']", "button[jsname='EszDEe']"]
#multiparty meeting
call_table = ["#roomId"  , ".MuiButton-root", "#displayname",  "button[aria-label='Mute audio']", "button[aria-label='Leave']"]

class call_api():
        def __init__(self, call_table, page, browser, text):
                self.page = page
                self.text = text
                self.inactive = "inactive"
                self.noe = "none"
                self.lichess = lichess(self.page, 0, 0, 0, 0)
                self.call_table = call_table
                self.browser = browser

        def kickstarter(self):
                global callkey
                print("entered kicstarter fxn")
                callname = self.lichess.finder(self.call_table[0], 1, 0)
                if callname:
                        increks()
                        print("kickstarterkey incremented")

                while True:
                        call_event.wait()
                        self.state_checker()

        def state_checker(self):
                global state, callstate
                while True:
                        if state == "active":
                                self.root()
                                break

                        elif state == "muteaudio" :
                                self.mute_audio()
                                break

                        elif state == "hangup":
                                self.hang_up()
                                break

                        elif callstate == 1:
                                self.browser.close()
                                break


        def root(self):
                global coast, usernames
                if coast == "white":
                        roomname = usernames[1]
                        username = usernames[1]
                        self.entry(roomname, username)

                elif coast == "black":
                        roomname = usernames[0]
                        username = usernames[1]
                        self.entry(roomname, username)



        def entry(self, roomnamed ,username):
                global coast
                roomname = f"{roomnamed}x998"
                callname = self.lichess.finder(self.call_table[0], 1, 0)
                callname.fill(self.roomname)

                callaccess = self.lichess.finder(self.call_table[1], 1, 0)
                callaccess.click()
                sleep_ns(sec*3)
                self.setuser(username)


        def setuser(self, usernamee):
                username = self.lichess.finder(self.call_table[2], 1, 0)
                username.fill(usernamee)

                audioalone = self.lichess.finder(self.call_table[1], 1, 0)
                audioalone.click()
                time.sleep(3)
                calllock(self.inactive)
                coastlock(self.noe)
                call_event.clear()


        def mute_audio(self):
                element = self.lichess.finder(self.call_table[3], 1, 0)
                element.click()
                deccallkey()
                calllock(self.inactive)
                call_event.clear()

        def hang_up(self):
                element = self.lichess.finder(self.call_table[4], 1, 0)
                element.click()
                self.return_home()
                deccallkey()
                calllock(self.inactive)
                call_event.clear()


        def close_call(self):                
                self.page.close()


def meet_compass():
        global updater,  kickstarterkey
        textual = "its the original call class"

        def analyzeflick():
                analyzeclass = compass(global_dict)


        def callflick():
                p = sync_playwright().start()
                browser = p.firefox.launch(headless=True, args=['--disable-dev-shm-usage'], firefox_user_prefs={'permissions.default.microphone': 1, 'permissions.default.camera': 1, 'permissions.default.desktop-notification': 1})
                context = browser.new_context()
                page = context.new_page()
                #stealth_sync(page)
                page.goto('https://mm.cedrc.cnr.it/', timeout = 180000)
                callclass = call_api(call_table, page, browser,textual) 
                callclass.kickstarter()
        callflicker = threading.Thread(target = callflick)
        callflicker.start()

        while True:
                if kickstarterkey == 1:
                        print("kickstarter key == 1")
                        analyzeflicker = threading.Thread(target = analyzeflick)
                        analyzeflicker.start()
                        updater = 1
                        break

                print("kickstarter key != 1")
                time.sleep(1)

        print("exited fxn")



def lichess_driver():
        global values, username, password, turns, cookiecode, cookie_data
        with sync_playwright() as playwright:
        # Launch Firefox with specified flags and preferences
        browser = playwright.firefox.launch(
                headless=False,
            args=[
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage',
                '--disable-accelerated-2d-canvas',
                '--no-first-run',
                '--no-zygote',
                '--single-process',
                '--disable-webgl',
                '--disable-webrtc',
                '--disable-images',
                '--disable-gpu',
                '--disable-background-networking',
                '--disable-background-timer-throttling',
                '--disable-javascript-harmony',
                '--disable-sync',
                '--disable-extensions',
                '--disable-translate',
                '--disable-backgrounding-occluded-windows',
                '--disable-renderer-backgrounding',
                '--disable-default-apps',
                '--disable-metrics',
                '--disable-hang-monitor',
                '--disable-domain-reliability',
                '--disable-features=TranslateUI,BlinkGenPropertyTrees',
                '--disk-cache-size=0',
                '--disable-blink-features=AutomationControlled',
                '--no-pings',
                '--disable-notifications',
                '--disable-crash-reporter',
                '--disable-component-extensions-with-background-pages',
                '--disable-site-isolation-trials',
                '--disable-software-rasterizer',
                '--disable-domain-reliability'
            ],
            firefox_user_prefs={
                "dom.ipc.processCount": 1,  # Limit to one content process
                "network.http.speculative-parallel-limit": 0,  # Disable speculative connections
                "gfx.webrender.all": False,  # Disable WebRender
                "layers.acceleration.disabled": True,  # Disable hardware acceleration
                "media.peerconnection.enabled": False,  # Disable WebRTC
                "browser.tabs.animate": False,  # Disable tab animations
                "browser.display.use_system_colors": False,  # Disable system colors
                "browser.chrome.favicons": False,  # Disable favicons
                "browser.sessionstore.resume_from_crash": False,  # Disable session restore after crash
                "browser.sessionhistory.max_total_viewers": 0,  # Disable back/forward cache
                "browser.cache.disk.enable": False,  # Disable disk cache
            }
        )
        
         context.add_init_script("""
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                });
                """)

        context.add_init_script("""
                Object.defineProperty(navigator, 'languages', {
                get: () => ['en-US', 'en']
                });
                Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3]
                });
                """)

        context.add_init_script("""
                Object.defineProperty(navigator, 'connection', { get: () => undefined });
                """)

        context.add_init_script("""
                Object.defineProperty(navigator, 'deviceMemory', { get: () => 8 });
                Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => 4 });
                 """)

        context.add_init_script("""
                Object.defineProperty(document, 'visibilityState', {
                get: () => 'visible'
                });

                Object.defineProperty(document, 'hidden', {
                get: () => false
                });
                """)

        # Additional stealth: Mock touch capabilities
        context.add_init_script("""
                Object.defineProperty(navigator, 'maxTouchPoints', { get: () => 1 });
                Object.defineProperty(navigator, 'platform', { get: () => 'Win32' });
                """)

        if cookiecode == 1:
                read_cookedata()
                context.add_cookies([cookie_data])

        page = context.new_page()
        page.goto('https://lichess.org/')
        
        stoned = lichess(page, values, claszz, browser, context)
        stoned.signin(username, password)
        
        # browser.close()

def show_connection_check_window():
    global conwindow
    conwindow = ConnectionCheckWindow()
    conwindow.show()


def close_connection_window():
    global conwindow
    conwindow.close()


def show_welcome_window():
    global welwindow
    welwindow = WelcomeWindow()
    welwindow.show()
    QTimer.singleShot(7000, close_welcome_window)


def close_welcome_window():
    global welwindow
    welwindow.close()
    proceed_after_welcome()

def second_window():
    global main_window
    main_window = CustomWindow()
    main_window.show()
    QTimer.singleShot(3000, check_updater)


def fresh():
    fres = GetDetails()
    fres.show()
    return app.exec_()


def meet_on():
        global updater
        meet_thread = threading.Thread(target=meet_compass)
        meet_thread.start()
        #time.sleep(10)
        while True:
                if updater == 1:
                        second_window()
                        break
                sleep_ns(sec)


def new_login():
    content = ""
    try:
        with open("file.txt", "r") as f:
            content = f.read()
            if content != "saved":
                disclaimer()
                fresh()
                return 1
            else:
                load_data()
                return 1
    except FileNotFoundError:
        disclaimer()
        fresh()
        return 1


def proceed_after_welcome():
    login = new_login()
    if login == 1:
        print("username and password ready")
        meet_on()

def check_updater():
        lichess_thread = threading.Thread(target=lichess_driver)
        lichess_thread.start()


if __name__ == '__main__':
        global app, main_window, updater
        updater = 0
        app = QApplication(sys.argv)
        failednum = 0
        while True:
                networktest = 1
                if networktest == 0:
                        failednum = 1
                        show_connection_check_window()
                        time.sleep(sec)

                elif networktest == 1:
                        if failednum == 1:
                                close_connection_window()
                        show_welcome_window()
                        break
        sleep_ns(sec*5)
        """while True:
                print("hello world")
                sleep_ns(ms * 60)"""
        sys.exit(app.exec_())
