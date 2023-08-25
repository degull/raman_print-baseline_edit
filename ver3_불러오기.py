""" from PyQt5.QtGui import QDesktopServices
import sys
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, QVariant
from BaselineRemoval import BaselineRemoval
from scipy.signal import find_peaks, peak_prominences
from PyQt5.QtWidgets import QPushButton
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import QAbstractTableModel
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import scipy.sparse as sparse
from scipy.sparse import linalg
from numpy.linalg import norm


from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont, QDesktopServices
 """
import sys
import os
import numpy as np
import pandas as pd
import pyqtgraph as pg
import scipy.sparse as sparse
from scipy.sparse import linalg
from numpy.linalg import norm

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont, QDesktopServices
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, QVariant

from BaselineRemoval import BaselineRemoval
from scipy.signal import find_peaks, peak_prominences
from matplotlib import pyplot as plt
from pyqtgraph import PlotWidget, plot


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1327, 1246)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_1 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_1.setMaximumSize(QtCore.QSize(16777215, 70))
        self.groupBox_1.setTitle("")
        self.groupBox_1.setObjectName("groupBox_1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_1 = QtWidgets.QLabel(self.groupBox_1)
        self.label_1.setObjectName("label_1")
        self.gridLayout_4.addWidget(self.label_1, 0, 0, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox_1)
        self.pushButton_1.setMaximumSize(QtCore.QSize(250, 16777215))
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout_4.addWidget(self.pushButton_1, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 550))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.graphwidget_1 = PlotWidget(self.groupBox_2)
        self.graphwidget_1.setObjectName("graphwidget_1")
        self.gridLayout_5.addWidget(self.graphwidget_1, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 70))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_6.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 550))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)
        self.graphwidget_2 = PlotWidget(self.groupBox_4)
        self.graphwidget_2.setObjectName("graphwidget_2")
        self.gridLayout_7.addWidget(self.graphwidget_2, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setMinimumSize(QtCore.QSize(450, 0))
        self.groupBox_6.setMaximumSize(QtCore.QSize(600, 16777215))
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout_9.addWidget(self.lineEdit_1, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_5.setText("Search")
        self.gridLayout_9.addWidget(self.pushButton_5, 0, 1, 1, 1)
        self.tableView_1 = QtWidgets.QTableView(self.groupBox_6)
        self.tableView_1.setObjectName("tableView_1")
        self.gridLayout_9.addWidget(self.tableView_1, 1, 0, 1, 2)
        self.horizontalLayout_2.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_7.setMinimumSize(QtCore.QSize(800, 0))
        self.groupBox_7.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_6 = QtWidgets.QLabel(self.groupBox_7)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_3.setMaximumSize(QtCore.QSize(250, 16777215))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_8.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.graphwidget_3 = PlotWidget(self.groupBox_7)
        self.graphwidget_3.setObjectName("graphwidget_3")
        self.gridLayout_8.addWidget(self.graphwidget_3, 1, 0, 1, 2)
        self.horizontalLayout_2.addWidget(self.groupBox_7)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # Define groupBox_9 before pushButton_4
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_7.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.search_and_display)
        self.gridLayout_3.addWidget(self.pushButton_7, 0, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_9, 0, 0, 1, 1)

        #excel 버튼
        self.pushButton_4 = QPushButton(self.groupBox_9)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 28))
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 4, 1, 1, Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.groupBox_8)

        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView_2 = QtWidgets.QTableView(self.groupBox_11)
        self.tableView_2.setObjectName("tableView_2")
        self.gridLayout.addWidget(self.tableView_2, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_11)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_12)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_8 = QtWidgets.QLabel(self.groupBox_12)
        self.label_8.setObjectName("label_8")
        self.gridLayout_10.addWidget(self.label_8, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_12)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_13 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_13)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_9 = QtWidgets.QLabel(self.groupBox_13)
        self.label_9.setObjectName("label_9")
        self.gridLayout_11.addWidget(self.label_9, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_13)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "Attach File"))
        self.pushButton_1.setText(_translate("MainWindow", "Attach File 1"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Graph 1"))
        self.label_2.setText(_translate("MainWindow", "Graph1"))
        self.label_3.setText(_translate("MainWindow", "Attach File"))
        self.pushButton_2.setText(_translate("MainWindow", "Attach File 2"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Graph 2"))
        self.label_4.setText(_translate("MainWindow", "Graph2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Baseline Correction"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Difference Value (File1 - File2)"))
        self.pushButton_5.setText(_translate("MainWindow", "Search"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Graph Comparsion"))
        self.label_6.setText(_translate("MainWindow", "Graph3"))
        self.pushButton_3.setText(_translate("MainWindow", "Attach 2 files"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Comparsion"))
        self.groupBox_9.setTitle(_translate("MainWindow", "파수 구간 입력"))
        self.pushButton.setText(_translate("MainWindow", "PubMed Link"))
        self.label_7.setText(_translate("MainWindow", "~"))
        self.pushButton_7.setText(_translate("MainWindow", "Search"))
        # excel 버튼
        self.pushButton_4.setText(_translate("MainWindow", "Peak Table 불러오기"))

        self.groupBox_11.setTitle(_translate("MainWindow", "GroupBox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Peak Table"))
        self.groupBox_12.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Help"))
        self.groupBox_13.setTitle(_translate("MainWindow", "GroupBox"))

        #ABOUT
        self.label_9.setText(_translate("MainWindow", "About"))
        font = QFont("Arial", 14)
        self.label_9.setFont(font)
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "About"))
        # Assuming you have a reference to label_9
        # Set the text for label_9
        self.label_9.setText(_translate("MainWindow", "DEVELOPER\n\n\n\n\n윤승현 \n순천향대학교 (컴퓨터소프트웨어공학과 20)\n-------------------------------------------------------------\n GitHub : https://github.com/degull \n Email : skytmdgus99@gmail.com\n\n\n\n권나경 \n한양여자대학교 (소프트웨어융합과 20) \n-------------------------------------------------------------\n GitHub : https://github.com/na-kyoung \n Email : nakyoung-kwon@naver.com" ))


        # Set font and style for "DEVELOPER" part
        font_developer = QFont("Arial", 18)
        font_developer.setBold(True)
        self.label_9.setFont(font_developer)

        # Set font and style for the rest of the text
        font_other = QFont("Arial", 14)
        self.label_9.setFont(font_other)


        self.graphwidget_1.setBackground('w')
        self.graphwidget_2.setBackground('w')
        self.graphwidget_3.setBackground('w')

        self.pushButton.clicked.connect(self.open_pubmed_url)
        self.pushButton_1.clicked.connect(self.load_file_1)
        self.pushButton_2.clicked.connect(self.load_file_2)
        self.pushButton_3.clicked.connect(self.load_file_3)
        self.pushButton_5.clicked.connect(self.filter_data_by_wavelength)########
        self.pushButton_4.clicked.connect(self.load_file_5)

        self.graphwidget_3.scene().sigMouseMoved.connect(self.updateTooltip)
        




    

    def open_pubmed_url(self):
        pubmed_url = "https://pubmed.ncbi.nlm.nih.gov/"  # Replace this with the desired URL
        QDesktopServices.openUrl(QUrl(pubmed_url))

    def filter_data_by_wavelength(self):
        wavelength = int(self.lineEdit_1.text())

        filtered_df = self.df_change[self.df_change['Wavelength'] == wavelength]

        if self.tableView_1_model is not None:
            self.tableView_1_model.clear()

        model = PandasTableModel(filtered_df)
        self.tableView_1.setModel(model)

        self.tableView_1_model = model

        self.tableView_1.resizeColumnsToContents()


    def updateTooltip(self, event):
        pos = event 
        view = self.graphwidget_3.plotItem.vb   
        if self.graphwidget_3.sceneBoundingRect().contains(pos):
            mousePoint = view.mapSceneToView(pos)
            x_coord = int(mousePoint.x())  
            # y_coord = mousePoint.y()
                
            tooltip_msg = f"X: {x_coord}"  # 삭제  {y_coord:.2f} from tooltip_msg
            QtWidgets.QToolTip.showText(self.graphwidget_3.mapToGlobal(QtCore.QPoint(pos.x(), pos.y())), tooltip_msg, self.graphwidget_3)
        else:
            QtWidgets.QToolTip.hideText()


    # baseline_arPLS로 baseline 수정 
    def baseline_arPLS(self, y, ratio=1e-6, lam=100, niter=10):
        L = len(y)
        diag = np.ones(L - 2)
        D = sparse.spdiags([diag, -2 * diag, diag], [0, -1, -2], L, L - 2)
        H = lam * D.dot(D.T)
        w = np.ones(L)
        W = sparse.spdiags(w, 0, L, L)
        crit = 1
        count = 0
        while crit > ratio:
            z = linalg.spsolve(W + H, W * y)
            d = y - z
            dn = d[d < 0]
            m = np.mean(dn)
            s = np.std(dn)
            w_new = 1 / (1 + np.exp(2 * (d - (2 * s - m)) / s))
            crit = norm(w_new - w) / norm(w)
            w = w_new
            W.setdiag(w)
            count += 1
            if count > niter:
                print('Maximum number of iterations exceeded')
                break
        return z

                

##파일첨부1
    def load_file_1(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        file_dialog.setNameFilter("CSV Files (*.csv)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            df = pd.read_csv(file_path)
            self.getData_1(df)

    def getData_1(self, df):
        # 빈 리스트
        list1 = []

        # 소수점 둘째 자리까지 반올림
        df = df.round(2)

        # 첫번째 행 읽기
        col1 = df.columns

        # X축 데이터
        x1 = df[col1[0]].replace('[\$,]', '', regex=True).astype(float)
        
        # Raw - Y좌표
        for i in range(1, len(col1)):
            colName = f'ROI {i} []'
            list1.append(colName)
            
        # Y좌표 평균값
        for i in list1:
            df[list1] = df[list1].replace('[\$,]', '', regex=True).astype(float)
        y1 = df[list1].mean(axis=1).values

        # 베이스라인 조정
        baseline = self.baseline_arPLS(y1)  # Assuming baseline_arPLS is a method within the same class
        corrected_y1 = y1 - baseline
        
        # 그래프 그리기
        self.graphwidget_1.addLegend(offset=(10, 5))
        self.graphwidget_1.plot(x1, y1, pen=pg.mkPen('b', width=2), name='Raw')
        self.graphwidget_1.plot(x1, corrected_y1, pen=pg.mkPen('r', width=2), name='BaselineCorrection')



    def graph_1(self, x, y):
        self.graphwidget_1.plot(x, y)

##파일첨부2
    def load_file_2(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        file_dialog.setNameFilter("CSV Files (*.csv)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            df = pd.read_csv(file_path)
            self.getData_2(df)

    def getData_2(self, df):
        # 빈 리스트
        list1 = []

        # 소수점 둘째 자리까지 반올림
        df = df.round(2)

        # 첫번째 행 읽기
        col1 = df.columns

        # X축 데이터
        x1 = df[col1[0]].replace('[\$,]', '', regex=True).astype(float)
        
        # Raw - Y좌표
        for i in range(1, len(col1)):
            colName = f'ROI {i} []'
            list1.append(colName)
            
        # Y좌표 평균값
        for i in list1:
            df[list1] = df[list1].replace('[\$,]', '', regex=True).astype(float)
        y1 = df[list1].mean(axis=1).values

        # 베이스라인 조정
        baseline = self.baseline_arPLS(y1)  # Assuming baseline_arPLS is a method within the same class
        corrected_y1 = y1 - baseline
        
        # 그래프 그리기
        self.graphwidget_2.addLegend(offset=(10, 5))
        self.graphwidget_2.plot(x1, y1, pen=pg.mkPen('b', width=2), name='Raw')
        self.graphwidget_2.plot(x1, corrected_y1, pen=pg.mkPen('r', width=2), name='BaselineCorrection')



    def graph_2(self, x, y):
        self.graphwidget_2.plot(x, y)

##파일첨부3
    def load_file_3(self):
        if hasattr(self, 'data_loaded_3') and self.data_loaded_3:
            #중복 첨부 방지
            return
        
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        file_dialog.setNameFilter("CSV Files (*.csv)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            df1 = pd.read_csv(file_path)
            #self.getData_3(df)
            self.load_file_4(df1)
            self.data_loaded_3 = True  # 데이터 첨부 완료

##파일첨부4
    def load_file_4(self, df1):
        if hasattr(self, 'data_loaded_4') and self.data_loaded_4:
            #중복 첨부 방지
            return
        
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        file_dialog.setNameFilter("CSV Files (*.csv)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            df2 = pd.read_csv(file_path)
            #self.getData_4(df)
            self.getData_4(df1, df2)
            self.data_loaded_4 = True  # 데이터 첨부 완료

    #데이터 2개 그래프 그리기
    def getData_4(self, df1, df2):
        # Lists to store column names
        list1 = []
        list2 = []

        # Round values to two decimal places
        df1 = df1.round(2)
        df2 = df2.round(2)

        # Get column names
        col1 = df1.columns
        col2 = df2.columns

        # X-axis data
        x1 = df1[col1[0]].replace('[\$,]', '', regex=True).astype(float)
        x2 = df2[col2[0]].replace('[\$,]', '', regex=True).astype(float)

        # Raw and UR2 - Y-coordinates
        for i in range(1, len(col1)):
            colName = f'ROI {i} []'
            list1.append(colName)
        for i in range(1, len(col2)):
            colName = f'ROI {i} []'
            list2.append(colName)

        # Process Raw data
        for i in list1:
            df1[list1] = df1[list1].replace('[\$,]', '', regex=True).astype(float)
        y1 = df1[list1].mean(axis=1).values
        baseline1 = self.baseline_arPLS(y1)
        corrected_y1 = y1 - baseline1

        # Process UR2 data
        for i in list2:
            df2[list2] = df2[list2].replace('[\$,]', '', regex=True).astype(float)
        y2 = df2[list2].mean(axis=1).values
        baseline2 = self.baseline_arPLS(y2)
        corrected_y2 = y2 - baseline2

        # Plot graphs
        self.graphwidget_3.addLegend(offset=(10, 5))
        self.graphwidget_3.plot(x1, corrected_y1, pen=pg.mkPen('b', width=2), name='First')
        self.graphwidget_3.plot(x2, corrected_y2, pen=pg.mkPen('r', width=2), name='Second')

        # Output data frame
        self.data_value(x1, corrected_y1, corrected_y2)

        # Call peak point display function
        self.peak(x1, x2, corrected_y1, corrected_y2)

    ## 데이터 프레임 출력
    def data_value(self, x, y1, y2):
        # Calculate the difference values
        change_value = y1 - y2

        # Convert wavelength to integers
        x_int = list(map(int, x))

        # Create a DataFrame for the difference value
        df_change = pd.DataFrame({
            'Wavelength': x_int,
            'ChangeValue': change_value
        })

        # Sort DataFrame by ChangeValue in descending order
        df_change = df_change.sort_values(by='ChangeValue', ascending=False)

        # Create a PandasTableModel from the sorted DataFrame
        model = PandasTableModel(df_change)

        # Set the model for tableView_1
        self.tableView_1.setModel(model)
        self.tableView_1.verticalHeader().setDefaultSectionSize(30)
        self.tableView_1.horizontalHeader().setDefaultSectionSize(80)
        self.tableView_1.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView_1.show()

        # Save the sorted DataFrame for later use
        self.df_change = df_change

        # Save the reference to the model for later use
        self.tableView_1_model = model


## peak 점 출력
    def peak(self, x1, x2, y1, y2):
        #qp = QPainter()
        #qp.setPen(QPen(Qt.blue, 18))

        x_list = []
        y_list = []
        
        # peak 변수
        baselined_spectrum1 = y1
        baselined_spectrum2 = y2

        # peak값 찾기
        peaks, _ = find_peaks(baselined_spectrum2, height=0, width=2)
        prominences = peak_prominences(baselined_spectrum2, peaks)[0]
        prominence_new = np.percentile(prominences, [0, 25, 50, 75, 80, 100], interpolation='nearest')[4]
        peaks, _ = find_peaks(baselined_spectrum2, prominence=prominence_new)

        # peak 점 표시
        for i in range(len(peaks)):
            x_list.append(x2[peaks[i]])  # x좌표
            y_list.append(baselined_spectrum2[peaks[i]])
        self.graphwidget_3.plot(x_list, y_list, symbol='o', pen=None, symbolSize=10, symbolBrush=('g'))

        
        # peak점 값 출력 (UR2)
        for i in range(len(peaks)):
            x_value = x2[peaks[i]]  # 피크의 x 값
            y_value1 = baselined_spectrum1[peaks[i]]  # 피크의 y 값
            y_value2 = baselined_spectrum2[peaks[i]]  # 피크의 y 값
            change_value = y_value2 - y_value1 # (UR2 - Raw) 차이
            x_value = int(x_value)
            #self.graphwidget_3.plot.text(x_value, y_value2, f'{x_value} \n +{change_value: .2f}', fontsize=10, verticalalignment='bottom')




##파일첨부 Peak Table
    def load_file_5(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Excel Files (*.xlsx)")

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            df = pd.read_excel(file_path)  # .xlsx 파일을 불러옴
            self.getData_5(df)  # 수정된 메서드 이름을 사용하여 데이터 출력

    def getData_5(self, df):
        df.columns = ["Raman peaks (cm−1)", "Strength", "Assignment", "Vibrational mode", "PMID"]

        # 데이터프레임을 tableView_2에 출력
        self.tableView_2.setModel(DataFrameModel(df))
        self.df = df

    def search_and_display(self):
        # Check if df is loaded
        if self.df is None:
            print("No data loaded. Please load the data first.")
            return

        # lineEdit_2와 lineEdit_3에서 값을 읽어옴
        lower_value = float(self.lineEdit_2.text())
        upper_value = float(self.lineEdit_3.text())

        # Raman peaks (cm−1)이 lower_value와 upper_value 사이인 데이터만 필터링
        filtered_df = self.df[(self.df["Raman peaks (cm−1)"] >= lower_value) & (self.df["Raman peaks (cm−1)"] <= upper_value)]

        # 필터링된 데이터를 새로운 데이터프레임으로 생성하여 tableView_2에 출력
        self.tableView_2.setModel(DataFrameModel(filtered_df))


# table model 만드는 object
class PandasTableModel(QAbstractTableModel):
    def __init__(self, data):
        super(PandasTableModel, self).__init__()
        self.data = data

    def rowCount(self, parent=QModelIndex()):
        return len(self.data)

    def columnCount(self, parent=QModelIndex()):
        return len(self.data.columns)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return QVariant()

        if role == Qt.DisplayRole:
            value = self.data.iloc[index.row(), index.column()]
            return str(value)

        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.data.columns[section])

            if orientation == Qt.Vertical:
                return str(section + 1)

        return QVariant()
    
    def clear(self):
        # 모델의 데이터를 비우는 메서드
        self.beginResetModel()
        self.data = pd.DataFrame()
        self.endResetModel()


        
class DataFrameModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent):
        return self._data.shape[0]

    def columnCount(self, parent):
        return self._data.shape[1]

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            return str(self._data.iloc[row, col])

        return None

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return str(self._data.columns[section])

        return None

   #####




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
