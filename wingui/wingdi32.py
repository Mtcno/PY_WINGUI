# -*- coding: utf-8 -*-

from wintydef import *
#gdi32.dll
#GetStockObject Parameters 
BLACK_BRUSH = 4
DKGRAY_BRUSH = 3
GRAY_BRUSH = 2
HOLLOW_BRUSH = 5
LTGRAY_BRUSH = 1
NULL_BRUSH = 5
WHITE_BRUSH = 0
BLACK_PEN = 7
NULL_PEN = 8
WHITE_PEN = 6
SYSTEM_FONT = 13
DEFAULT_PALETTE = 15
#gdi32 function
GetStockObject = gdi32.GetStockObject


def GetRValue(value):
	return BYTE(DWORD(value))
	
def GetGValue(value):
	return BYTE(DWORD(value) >> 8)

def GetBValue(value):
	return BYTE(DWORD(value) >> 16)




		
		
		
		
		
		
		
		

