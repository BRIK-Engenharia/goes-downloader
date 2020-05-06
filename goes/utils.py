# -*- coding: utf-8 -*-

__author__ = 'Douglas Uba'
__email__  = 'douglas.uba@inpe.br'

import datetime
from PyQt5.QtCore import QObject, pyqtSignal
from tqdm import tqdm

def generateListOfDays(start, end):
    '''This function returns all-days between given two dates.'''
    delta = end - start
    return [start + datetime.timedelta(i) for i in range(delta.days + 1)]

def isChannelSeparated(product):
    '''This function verifies if the given product is separeted by channels.'''
    return 'L1b-Rad' in product or 'L2-CMI' in product

'''Simple notification system.'''
class Notifier(QObject):
    startDownloadTask = pyqtSignal(int) # int: number of file that will be download
    startFileDownload = pyqtSignal(str) # str: remote file name
    endFileDownload = pyqtSignal(str) # str: remote file name
    endDownloadTask = pyqtSignal() # none

class TqdmProgress:
    def __init__(self):
        self.progressBar = None
    def onStartDownloadTask(self, numberOfFiles):
        self.progressBar = tqdm(desc='Download GOES data', total=numberOfFiles, unit='file')
    def onStartFileDownload(self, file):
        pass
    def onEndFileDownload(self, file):
        self.progressBar.update()
    def onEndDownloadTask(self):
        pass
    def wasCanceled(self):
        return False
