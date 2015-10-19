#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import sys

class Alphabet:

    def __init__(self, stringOfFileWithAlphabet):
        try:
            self.fileWithAlphabet = stringOfFileWithAlphabet
            self.im = Image.open(stringOfFileWithAlphabet)
            self.lettersOffset=self.__generateLettersOffsetDict()
            self.defaultVerticalOffset=7
        except:
            self.im = ''
            e = sys.exc_info()[0]
            print "When trying to initialize the alphabet object"
            print "Error: " + str(e) 
            sys.exit(1)

    def regionForLetterAndVerticalOffset(self, letter):
        try:
            region = self.im.crop(self.lettersOffset[letter])
        except:
            e = sys.exc_info()[0]
            print "When extracting region for letter" + letter
            print "Error: " + str(e)
            region=''
        return region, self.letterVerticalOffset(letter)
    
    def letterVerticalOffset(self, letter):
        if letter in 'pqjyg,¡¿':
            return self.defaultVerticalOffset
        else:
            return 0

    def __generateLettersOffsetDict(self):
        lettersOffset = {}
        #Offsets
        lettersOffset["a"]=(1112,40,1143,79)
        lettersOffset["b"]=(1144,40,1175,79)
        lettersOffset["c"]=(1176,40,1203,79)
        lettersOffset["d"]=(1204,40,1235,79)
        lettersOffset["e"]=(1236,40,1267,79)
        lettersOffset["f"]=(0,80,32,119)
        lettersOffset["g"]=(32,80,63,119)
        lettersOffset["h"]=(64,80,99,119)
        lettersOffset["i"]=(100,80,123,119)
        lettersOffset["j"]=(132,80,150,119)
        lettersOffset["k"]=(156,80,188,119)
        lettersOffset["l"]=(192,80,215,119)
        lettersOffset["m"]=(216,80,251,119)
        lettersOffset["n"]=(252,80,283,119)
        lettersOffset["o"]=(284,80,315,119)
        lettersOffset["p"]=(316,80,347,119)
        lettersOffset["q"]=(348,80,379,119)
        lettersOffset["r"]=(380,80,411,119)
        lettersOffset["s"]=(412,80,443,119)
        lettersOffset["t"]=(444,80,475,119)
        lettersOffset["u"]=(476,80,507,119)
        lettersOffset["v"]=(508,80,539,119)
        lettersOffset["w"]=(540,80,575,119)
        lettersOffset["x"]=(576,80,607,119)
        lettersOffset["y"]=(608,80,639,119)
        lettersOffset["z"]=(640,80,671,119)
        lettersOffset["ö"]=(672,80,703,119)
        lettersOffset["ä"]=(704,80,735,119)
        lettersOffset["Ö"]=(736,80,767,119)
        lettersOffset["ß"]=(768,80,839,119)
        lettersOffset["ç"]=(840,80,871,119)
        lettersOffset["ü"]=(872,80,903,119)
        lettersOffset["é"]=(904,80,935,119)
        lettersOffset["â"]=(936,80,967,119)
        lettersOffset["ä"]=(968,80,999,119)
        lettersOffset["à"]=(1000,80,1067,119)
        lettersOffset["ê"]=(1068,80,1099,119)
        lettersOffset["ë"]=(1100,80,1131,119)
        lettersOffset["è"]=(1132,80,1167,119)
        lettersOffset["ï"]=(1168,80,1195,119)
        lettersOffset["ï"]=(1196,80,1227,119)
        lettersOffset["ì"]=(1228,80,1251,119)
        lettersOffset["Ä"]=(0,120,31,139)
        lettersOffset["å"]=(32,120,63,139)
        lettersOffset["É"]=(64,120,91,139)
        lettersOffset["ù"]=(92,120,123,139)
        lettersOffset["ò"]=(124,120,155,139)
        lettersOffset["?"]=(0,40,31,79)
        lettersOffset["-"]=(32,40,67,79)
        lettersOffset["A"]=(68,40,99,79)
        lettersOffset["B"]=(100,40,131,79)
        lettersOffset["C"]=(132,40,163,79)
        lettersOffset["D"]=(164,40,195,79)
        lettersOffset["E"]=(196,40,227,79)
        lettersOffset["F"]=(228,40,259,79)
        lettersOffset["G"]=(260,40,291,79)
        lettersOffset["H"]=(292,40,327,79)
        lettersOffset["I"]=(328,40,355,79)
        lettersOffset["J"]=(356,40,387,79)
        lettersOffset["K"]=(388,40,419,79)
        lettersOffset["L"]=(420,40,451,79)
        lettersOffset["M"]=(452,40,487,79)
        lettersOffset["N"]=(488,40,519,79)
        lettersOffset["O"]=(520,40,551,79)
        lettersOffset["P"]=(552,40,583,79)
        lettersOffset["Q"]=(584,40,615,79)
        lettersOffset["R"]=(616,40,647,79)
        lettersOffset["S"]=(648,40,679,79)
        lettersOffset["T"]=(680,40,711,79)
        lettersOffset["U"]=(712,40,743,79)
        lettersOffset["V"]=(744,40,775,79)
        lettersOffset["W"]=(776,40,811,79)
        lettersOffset["X"]=(812,40,843,79)
        lettersOffset["Y"]=(844,40,875,79)
        lettersOffset["Z"]=(876,40,907,79)
        lettersOffset["ü"]=(908,40,939,79)
        lettersOffset["ä"]=(940,40,971,79)
        lettersOffset["Ü"]=(972,40,1003,79)
        lettersOffset["™"]=(120,0,163,40)
        lettersOffset[" "]=(164,0,195,40)
        lettersOffset["!"]=(324,0,339,40)
        lettersOffset['"']=(340,0,371,40)
        lettersOffset["#"]=(372,0,411,40)
        lettersOffset["$"]=(412,0,443,40)
        lettersOffset["%"]=(444,0,475,40)
        lettersOffset["&"]=(476,0,515,40)
        lettersOffset["'"]=(516,0,539,40)
        lettersOffset["("]=(540,0,563,40)
        lettersOffset[")"]=(564,0,591,40)
        lettersOffset["*"]=(592,0,631,40)
        lettersOffset["+"]=(632,0,667,40)
        lettersOffset[","]=(668,0,687,40)
        lettersOffset["]"]=(668,0,687,40)
        lettersOffset["-"]=(688,0,727,40)
        lettersOffset["."]=(728,0,743,40)
        lettersOffset["/"]=(744,0,779,40)
        lettersOffset["0"]=(780,0,811,40)
        lettersOffset["1"]=(812,0,843,40)
        lettersOffset["2"]=(844,0,875,40)
        lettersOffset["3"]=(876,0,907,40)
        lettersOffset["4"]=(908,0,943,40)
        lettersOffset["5"]=(944,0,975,40)
        lettersOffset["6"]=(976,0,1007,40)
        lettersOffset["7"]=(1008,0,1039,40)
        lettersOffset["8"]=(1040,0,1071,40)
        lettersOffset["9"]=(1072,0,1107,40)
        lettersOffset[":"]=(1108,0,1131,40)
        lettersOffset[";"]=(1132,0,1151,40)
        lettersOffset["<"]=(1152,0,1183,40)
        lettersOffset["©"]=(1184,0,1219,40)
        lettersOffset[">"]=(1220,0,1251,40)
        lettersOffset["á"]=(156,120,185,159)
        lettersOffset["í"]=(186,120,209,159)
        lettersOffset["ó"]=(210,120,241,159)
        lettersOffset["ú"]=(242,120,273,159)
        lettersOffset["ñ"]=(274,120,305,159)
        lettersOffset["¡"]=(306,120,321,159)
        lettersOffset["¿"]=(322,120,353,159)
        lettersOffset["ã"]=(354,120,385,159)
        lettersOffset["õ"]=(386,120,417,159)
        return lettersOffset

