#!-*-coding:utf-8-*-

from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest

import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import ui_MyForm

#Summ
import FrequencySummarizer
import TextRank_Test

class MainWindow(QMainWindow, ui_MyForm.Ui_MainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.horizontalSlider.valueChanged.connect(self.Summ)

    def Summ(self):
        text = self.textEdit.toPlainText()
        sents = sent_tokenize(text)
        n = len(sents) * self.horizontalSlider.value() // 100
        if n == 0:
             n = 1
        summ_text = ''
        if self.radioButton.isChecked():
            fs = FrequencySummarizer.SimpleFrequencySummarizer()
            summ_text = fs.summarize(text, n)
        elif self.radioButton_2.isChecked():
            text1 = TextRank_Test.extractSentences(text)
            # reduction = TextRank.Reduction()
            # summ_text = reduction.reduce(text, self.horizontalSlider.value() / 100)
        self.textEdit_2.clear()
        # text1 = ''
        # for s in summ_text:
        #     text1 = text1 + s
        # # for s in summ_text:
        # #     self.textEdit_2.text
        self.textEdit_2.setText(text1)
# -----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('untitled12')

    # create widget
    w = MainWindow()
    #w.setWindowTitle('untitled12')
    w.show()

    # connection
    QObject.connect(app, SIGNAL('lastWindowClosed()'), app, SLOT('quit()'))

    # execute application
    sys.exit(app.exec_())