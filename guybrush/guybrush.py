#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from myImage import MyImage
from alphabet import Alphabet
import os

def main():
    args = readCommandLineOptions()
    (myimg, alphab) = generateImageAndAlphabet(args.inputFile,'imgs/bigPinkFont.png') #only 1 alphabet for now
    myimg = addTextToImage(myimg, alphab, args.text)
    myimg.saveImageToFile(args.outputFile)
    print "Inputfile->" + args.inputFile
    print "Outputfile->" + args.outputFile
    print "Text->" + args.text

def addCharacterToImage(myimg, alphab, c):
    region, verticalOffset = alphab.regionForLetterAndVerticalOffset(c) 
    myimg.pasteRegion(region, verticalOffset)

def addTextToImage(myimg, alphab, text):
    for c in text:
        print "About to paste " + c + " character"
        addCharacterToImage(myimg, alphab, c)
    return myimg

def generateImageAndAlphabet(fileNameForImage, fileNameForAlphabet):
    myimg = MyImage(fileNameForImage)
    alphab = Alphabet(fileNameForAlphabet)
    return (myimg, alphab)
    
def readCommandLineOptions():
    parser = InitializeCommandLineArgumentsParser()
    parser = addCommandLineArguments(parser)
    args = parser.parse_args()
    return args

def addCommandLineArguments(parser):
    parser.add_argument("text", help="Text to include in the input file")
    parser.add_argument('-i','--inputFile', help='Filename for the input of the script', required=True)
    parser.add_argument('-o','--outputFile', help='Filename for the output of the script', required=True)
    return parser

def InitializeCommandLineArgumentsParser():
    parser = argparse.ArgumentParser(description='Script to include 8bit text into images')
    return parser

if __name__ == '__main__':
    main()


