#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import sys

class Image:

	def __init__(self, stringOfFileWithSrcImage, textStartCoordinate=(50,50)):
        try:
            self.fileWithImage = stringOfFileWithSrcImage
            self.img = Image.open(stringOfFileWithSrcImage)
            self.textStartCoordinate = textStartCoordinate
        except:
            self.img = ''
            e = sys.exc_info()[0]
			print "Error: " + str(e) 
            sys.exit(2)

    def saveImageToFile(self, stringOfFileToSave):
    	try:
    		self.img.save(stringOfFileToSave)
    	except:
    		e = sys.exc_info()[0]
			print "Error: " + str(e) 
    		sys.exit(3)

    def pasteRegion(self, regionToPaste):
    	try:
    		self.img.paste(regionToPaste,self.textStartCoordinate,regionToPaste)
		except:
    		e = sys.exc_info()[0]
			print "Error: " + str(e) 
			exit(4) 
