# Guybrush script
This is just an attempt to make an script for generating Monkey Island style images with custom text on them.


# Mind dump

I'll get some ideas/files from this project: http://www.int33h.com/test/mi/


The JS code/offsets for the font creation:

```
function createSpeakerGrandi(img){
	var sp = new Speaker(img);
	sp.add("a",1112,40,32,40);
	sp.add("b",1144,40,32,40);
	sp.add("c",1176,40,28,40);
	sp.add("d",1204,40,32,40);
	sp.add("e",1236,40,32,40);
	sp.add("f",0,80,32,40);
	sp.add("g",32,80,32,40);
	sp.add("h",64,80,32,40);
	sp.add("i",100,80,24,40);
	sp.add("j",128,80,28,40);
	sp.add("k",156,80,32,40);
	sp.add("l",192,80,24,40);
	sp.add("m",216,80,36,40);
	sp.add("n",252,80,32,40);
	sp.add("o",284,80,32,40);
	sp.add("p",316,80,32,40);
	sp.add("q",348,80,32,40);
	sp.add("r",380,80,32,40);
	sp.add("s",412,80,32,40);
	sp.add("t",444,80,32,40);
	sp.add("u",476,80,32,40);
	sp.add("v",508,80,32,40);
	sp.add("w",540,80,36,40);
	sp.add("x",576,80,32,40);
	sp.add("y",608,80,32,40);
	sp.add("z",640,80,32,40);


	sp.add("ö",672,80,32,40);
	sp.add("ä",704,80,32,40);
	sp.add("Ö",736,80,32,40);
	sp.add("ß",768,80,32,40);

	sp.add("ç",840,80,32,40);
	sp.add("ü",872,80,32,40);
	sp.add("é",904,80,32,40);
	sp.add("â",936,80,32,40);
	sp.add("ä",968,80,32,40);
	sp.add("à",1000,80,32,40);

	sp.add("ê",1068,80,32,40);
	sp.add("ë",1100,80,32,40);
	sp.add("è",1132,80,32,40);
	sp.add("ï",1168,80,24,40);
	sp.add("ï",1196,80,24,40);
	sp.add("ì",1228,80,24,40);

	sp.add("Ä",0,120,32,40);
	sp.add("å",32,120,32,40);
	sp.add("É",64,120,32,40);
	sp.add("ù",92,120,32,40);
	sp.add("ò",124,120,32,40);


	sp.add("?",0,40,32,40);
	sp.add("-",32,40,36,40);
	sp.add("A",68,40,32,40);
	sp.add("B",100,40,32,40);
	sp.add("C",132,40,32,40);
	sp.add("D",164,40,32,40);
	sp.add("E",196,40,32,40);
	sp.add("F",228,40,32,40);
	sp.add("G",260,40,32,40);
	sp.add("H",292,40,32,40);
	sp.add("I",328,40,24,40);
	sp.add("J",356,40,32,40);
	sp.add("K",388,40,32,40);
	sp.add("L",420,40,32,40);
	sp.add("M",452,40,36,40);
	sp.add("N",488,40,32,40);
	sp.add("O",520,40,32,40);
	sp.add("P",552,40,32,40);
	sp.add("Q",584,40,32,40);
	sp.add("R",616,40,32,40);
	sp.add("S",648,40,32,40);
	sp.add("T",680,40,32,40);
	sp.add("U",712,40,32,40);
	sp.add("V",744,40,32,40);
	sp.add("W",776,40,36,40);
	sp.add("X",812,40,32,40);
	sp.add("Y",844,40,32,40);
	sp.add("Z",876,40,32,40);
	sp.add("ü",908,40,32,40);
	sp.add("ä",940,40,32,40);
	sp.add("Ü",972,40,32,40);


	sp.add("™",120,0,44,40);
	sp.add(" ",164,0,12,40);
	sp.add("!",324,0,16,40);
	sp.add('"',340,0,32,40);
	sp.add("#",372,0,40,40);
	sp.add("$",412,0,32,40);
	sp.add("%",444,0,32,40);
	sp.add("&",476,0,32,40);
	sp.add("'",516,0,20,40);
	sp.add("(",540,0,28,40);
	sp.add(")",564,0,28,40);
	sp.add("*",592,0,40,40);
	sp.add("+",632,0,32,40);
	sp.add(",",668,0,20,40);
	sp.add("-",688,0,32,40);

	sp.add(".",728,0,16,40);
	sp.add("/",744,0,36,40);

	sp.add("0",780,0,32,40);
	sp.add("1",812,0,32,40);
	sp.add("2",844,0,32,40);
	sp.add("3",876,0,32,40);
	sp.add("4",908,0,36,40);
	sp.add("5",944,0,32,40);
	sp.add("6",976,0,32,40);
	sp.add("7",1008,0,32,40);
	sp.add("8",1040,0,32,40);
	sp.add("9",1072,0,32,40);
	sp.add(":",1108,0,24,40);
	sp.add(";",1132,0,24,40);
	sp.add("<",1152,0,32,40);
	sp.add("©",1184,0,32,40);
	sp.add(">",1220,0,32,40);


	sp.add("á",156,120,32,40);
	sp.add("í",186,120,24,40);
	sp.add("ó",210,120,32,40);
	sp.add("ú",242,120,32,40);
	sp.add("ñ",274,120,32,40);
	sp.add("¡",306,120,16,40);
	sp.add("¿",322,120,32,40);
	sp.add("ã",354,120,32,40);
	sp.add("õ",386,120,32,40);

 
	sp.adjustY = function(c,bmp){
		// to override
		if (c == "p")	bmp.y += 4*Const.MOB;
		if (c == "q")	bmp.y += 4*Const.MOB;
		if (c == "j")	bmp.y += 4*Const.MOB;
		if (c == "y")	bmp.y += 4*Const.MOB;
		if (c == "g")	bmp.y += 4*Const.MOB;
		if (c == ",")	bmp.y += 4*Const.MOB;
		if (c == "¡")	bmp.y += 4*Const.MOB;
		if (c == "¿")	bmp.y += 4*Const.MOB;
	}

	sp.interlinea = 36;

	return sp;
}

```
