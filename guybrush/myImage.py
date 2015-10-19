#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import sys

class MyImage:

    def __init__(self, stringOfFileWithSrcImage, textStartCoordinate=(50,50)):
        try:
            self.fileWithImage = stringOfFileWithSrcImage
            self.imag = Image.open(stringOfFileWithSrcImage)
            self.imag.load()
            self.textStartCoordinate = textStartCoordinate
        except:
            self.imag = ''
            e = sys.exc_info()[0]
            print "When initializing image object"
            print "Error: " + str(e) 
            sys.exit(2)

    def saveImageToFile(self, stringOfFileToSave):
        try:
    	    self.imag.save(stringOfFileToSave)
        except:
            e = sys.exc_info()[0]
            print "When saving Image to file"
            print "Error: " + str(e) 
            sys.exit(3)

    def pasteRegion(self, regionToPaste, verticalOffset):
        try:
            startPoint = (self.textStartCoordinate[0], self.textStartCoordinate[1]+verticalOffset)
            self.imag.paste(regionToPaste,startPoint,regionToPaste)
            (width, heigth)=regionToPaste.size
            self.textStartCoordinate = (self.textStartCoordinate[0]+width, self.textStartCoordinate[1])
        except:
            e = sys.exc_info()[0]
            print "When pasting the region into the Image"
            print "Error: " + str(e) 
            exit(4) 
