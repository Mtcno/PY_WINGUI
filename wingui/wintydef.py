# -*- coding: utf-8 -*-

import ctypes 

#
import platform
ver = platform.win32_ver()
#Windows Data Types
_WIN32_WINNT_NT4 = 0x0400
_WIN32_WINNT_WIN2K = 0x0500
_WIN32_WINNT_WINXP = 0x0501
_WIN32_WINNT_WS03 = 0x0502
_WIN32_WINNT_WIN6 = 0x0600
_WIN32_WINNT_VISTA = 0x0600
_WIN32_WINNT_WS08 = 0x0600
_WIN32_WINNT_LONGHORN = 0x0600
_WIN32_WINNT_WIN7 = 0x0601
_WIN32_WINNT_WIN8 = 0x0602
_WIN32_WINNT_WINBLUE = 0x0603 
_WIN32_WINNT_WINTHRESHOLD = 0x0A00
_WIN32_WINNT_WIN10 = 0x0A00


_95_NT4_0 =	0x0200	
_IE_3_0 = 0x0300	
_IE_3_01 = 0x0300	
_IE_3_02 = 0x0300	
_IE_4_0 = 0x0400	
_IE_4_01 = 0x0401	
_IE_5_0 = 0x0500	
_IE_5_0a = 0x0500
_IE_5_0b = 0x0500
_IE_5_01 = 0x0501
_IE_5_5 = 0x0550
_IE_6 = 0x0600
_IE_6_0_SP1 = 0x0601
_IE_6_0_SP2 = 0x0603	
_IE_7_0 = 0x07200	
_IE_8_0 = 0x0800	
	


if ver[0] == 'XP':
	WINVER = _WIN32_WINNT = _WIN32_WINNT_WINXP
	_WIN32_IE = _IE_8_0

#
NULL = 0

WORD = ctypes.c_ushort
DWORD = ctypes.c_uint


SHORT = ctypes.c_short
INT = ctypes.c_int
LONG = ctypes.c_long

USHORT = ctypes.c_ushort
UINT = ctypes.c_uint
ULONG = ctypes.c_ulong

FLOAT = ctypes.c_float
DOUBLE = ctypes.c_double

BOOL = ctypes.c_bool
BYTE = ctypes.c_ubyte
BOOLEAN = BYTE

CCHAR = ctypes.c_char
CHAR = ctypes.c_char
TCHAR = ctypes.c_char
WCHAR = ctypes.c_wchar

LPBYTE = ctypes.POINTER(BYTE)
LPCSTR = LPSTR = ctypes.c_char_p
LPCWSTR = LPWSTR = ctypes.c_wchar_p
LPVOID = PVOID = ctypes.c_void_p

LRESULT = INT


ATOM = WORD
COLORREF = DWORD
DWORDLONG = ctypes.c_longlong 
DWORD_PTR = ctypes.POINTER(UINT)
DWORD32 = UINT
DWORD64 = ctypes.c_longlong 
UINT_PTR = ctypes.POINTER(UINT)
ULONG_PTR = ctypes.POINTER(ULONG)
PUINT = UINT

HANDLE = PVOID
HACCEL = HANDLE

HBITMAP = HANDLE
HBRUSH = HANDLE
HCOLORSPACE = HANDLE
HCONV = HANDLE
HCONVLIST = HANDLE
HCURSOR = HANDLE
HDC = HANDLE
HDDEDATA = HANDLE
HDESK = HANDLE
HDROP = HANDLE
HDWP = HANDLE
HENHMETAFILE = HANDLE
HFILE = INT
HFONT = HANDLE
HGDIOBJ = HANDLE
HGLOBAL = HANDLE
HHOOK = HANDLE
HICON = HANDLE
HINSTANCE = HANDLE
HKEY = HANDLE
HKL = HANDLE
HLOCAL = HANDLE
HMENU = HANDLE
HMETAFILE = HANDLE
HMODULE = HANDLE

if WINVER >= 0x0500:
	HMONITOR = HANDLE
	
HPALETTE = HANDLE
HPEN = HANDLE
HRESULT = LONG
HRGN = HANDLE
HRSRC = HANDLE
HSZ = HANDLE
HWINSTA = HANDLE
HWND = HANDLE

# WPARAM is defined as UINT_PTR (unsigned type)
# LPARAM is defined as LONG_PTR (signed type)
if ctypes.sizeof(ctypes.c_long) == ctypes.sizeof(ctypes.c_void_p):
    WPARAM = ctypes.c_ulong
    LPARAM = ctypes.c_long
    HALF_PTR = SHORT
elif ctypes.sizeof(ctypes.c_longlong) == ctypes.sizeof(ctypes.c_void_p):
    WPARAM = ctypes.c_ulonglong
    LPARAM = ctypes.c_longlong
    HALF_PTR = INT
 
#ctypes
#CWINFUNC 返回__stdcall function
#toPointer 获得C类型指针
#topointer 获得obj类型指针
#String 	从指针获取字符串，需decode
#wString	从指针获取宽字符串
#sizeof	相当于sizeof

CWINFUNC = ctypes.WINFUNCTYPE
CALLBACK = CWINFUNC
toPointer = ctypes.POINTER
topointer = ctypes.pointer
tofuncp = ctypes.cast
getpointer = ctypes.addressof
String = ctypes.string_at
wString = ctypes.wstring_at
sizeof = ctypes.sizeof
#end
  
#windll function   
win32 = ctypes.windll
kernel32 = win32.kernel32
user32 = win32.user32
gdi32 = win32.gdi32
comctl32 = win32.comctl32






    