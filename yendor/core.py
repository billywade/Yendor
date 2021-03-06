#! /usr/bin/python3
import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QVBoxLayout, QTabWidget)
from .gui import npc, places, items, quest, monsterbuilder

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Yendor'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.table_widget = TableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.show()


class TableWidget(QWidget):

    def __init__(self, parent):
        super(TableWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # List of tabs and their names
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tabs.addTab(self.tab1, "NPCs")
        self.tabs.addTab(self.tab2, "Places")
        self.tabs.addTab(self.tab3, "Items")
        self.tabs.addTab(self.tab4, "Quest")
        self.tabs.addTab(self.tab5, "Monster Saver")

        self.npc_object = npc.Tab()
        self.tab1.setLayout(self.npc_object.layout)
        self.places_object = places.Tab()
        self.tab2.setLayout(self.places_object.layout)
        self.items_object = items.Tab()
        self.tab3.setLayout(self.items_object.layout)
        self.quest_object = quest.Tab()
        self.tab4.setLayout(self.quest_object.layout)
        self.monsterbuilder_object = monsterbuilder.Tab()
        self.tab5.setLayout(self.monsterbuilder_object.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)



def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
