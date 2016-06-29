# -*- coding: utf-8 -*-

# windows struct define
from wintydef import *

class STARTUPINFOA(ctypes.Structure):
	_fields_ = [
			("cb",DWORD),
			("lpReserved",LPSTR),
			("lpDesktop",LPSTR),
			("lpTitle",LPSTR),
			("dwX",DWORD),
			("dwY",DWORD),
			("dwXSize",DWORD),
			("dwYSize",DWORD),
			("dwXCountChars",DWORD),
			("dwYCountChars",DWORD),
			("dwFillAttribute",DWORD),
			("dwFlags",DWORD),
			("wShowWindow",WORD),
			("cbReserved2",WORD),
			("lpReserved2",LPBYTE),
			("hStdInput",HANDLE),
			("hStdOutput",HANDLE),
			("hStdError",HANDLE)
			]
	
class STARTUPINFOW(ctypes.Structure):
	_fields_ = [	
			("cb",DWORD),
			("lpReserved",LPWSTR),
			("lpDesktop",LPWSTR),
			("lpTitle",LPWSTR),
			("dwX",DWORD),
			("dwY",DWORD),
			("dwXSize",DWORD),
			("dwYSize",DWORD),
			("dwXCountChars",DWORD),
			("dwYCountChars",DWORD),
			("dwFillAttribute",DWORD),
			("dwFlags",DWORD),
			("wShowWindow",WORD),
			("cbReserved2",WORD),
			("lpReserved2",LPBYTE),
			("hStdInput",HANDLE),
			("hStdOutput",HANDLE),
			("hStdError",HANDLE)
			]

class WNDCLASSA(ctypes.Structure):
	_fields_ = [
			("style",UINT),
			("lpfnWndProc",HANDLE),
			("cbClsExtra",INT),
			("cbWndExtra",INT),
			("hInstance",HINSTANCE),
			("hIcon",HICON),
			("hCursor",HCURSOR),
			("hbrBackground",HBRUSH),
			("lpszMenuName",LPCSTR),
			("lpszClassName",LPCSTR),
			]
			
class WNDCLASSW(ctypes.Structure):
	_fields_ = [
			("style",UINT),
			("lpfnWndProc",HANDLE),
			("cbClsExtra",INT),
			("cbWndExtra",INT),
			("hInstance",HINSTANCE),
			("hIcon",HICON),
			("hCursor",HCURSOR),
			("hbrBackground",HBRUSH),
			("lpszMenuName",LPCWSTR),
			("lpszClassName",LPCWSTR),
			]			
					
class WNDCLASSEXA(ctypes.Structure):
	_fields_ = [
			("cbSize",UINT),
			("style",UINT),
			("lpfnWndProc",HANDLE),
			("cbClsExtra",INT),
			("cbWndExtra",INT),
			("hInstance",HINSTANCE),
			("hIcon",HICON),
			("hCursor",HCURSOR),
			("hbrBackground",HBRUSH),
			("lpszMenuName",LPCSTR),
			("lpszClassName",LPCSTR),
			("hIconSm",HICON)
			]
			
class WNDCLASSEXW(ctypes.Structure):
	_fields_ = [
			("cbSize",UINT),
			("style",UINT),
			("lpfnWndProc",HANDLE),
			("cbClsExtra",INT),
			("cbWndExtra",INT),
			("hInstance",HINSTANCE),
			("hIcon",HICON),
			("hCursor",HCURSOR),
			("hbrBackground",HBRUSH),
			("lpszMenuName",LPCWSTR),
			("lpszClassName",LPCWSTR),
			("hIconSm",HICON)
			]
			
class POINT(ctypes.Structure):
	_fields_=  [
			("x",LONG),
			("y",LONG)
			]
			
			
class MSG(ctypes.Structure):
	_fields_ = [
			("hwnd",HWND),
			("message",UINT),
			("wParam",WPARAM),
			("lParam",LPARAM),
			("time",DWORD),
			("pt",POINT)
			]
			
			
#非ms定义结构
#CreateWindow
class CWindowA(ctypes.Structure):
	_fields_ = [
			("lpClassName",LPCSTR),
			("lpWindowName",LPCSTR),
			("dwStyle",DWORD),
			("x",INT),
			("y",INT),
			("nWidth",INT),
			("nHeight",INT),
			("hWndParent",HWND),
			("hMenu",HMENU),
			("hlnstance",HANDLE),
			("lpParam",LPVOID)
			]
					
class CWindowW(ctypes.Structure):
	_fields_ = [
			("lpClassName",LPCWSTR),
			("lpWindowName",LPCWSTR),
			("dwStyle",DWORD),
			("x",INT),
			("y",INT),
			("nWidth",INT),
			("nHeight",INT),
			("hWndParent",HWND),
			("hMenu",HMENU),
			("hlnstance",HANDLE),
			("lpParam",LPVOID)
			]

class CWindowExA(ctypes.Structure):
	_fields_ = [
			("dwExStyle",DWORD),
			("lpClassName",LPCSTR),
			("lpWindowName",LPCSTR),
			("dwStyle",DWORD),
			("x",INT),
			("y",INT),
			("nWidth",INT),
			("nHeight",INT),
			("hWndParent",HWND),
			("hMenu",HMENU),
			("hlnstance",HANDLE),
			("lpParam",LPVOID)
			]	
			
class CWindowExW(ctypes.Structure):
	_fields_ = [
			("dwExStyle",DWORD),
			("lpClassName",LPCWSTR),
			("lpWindowName",LPCWSTR),
			("dwStyle",DWORD),
			("x",INT),
			("y",INT),
			("nWidth",INT),
			("nHeight",INT),
			("hWndParent",HWND),
			("hMenu",HMENU),
			("hlnstance",HANDLE),
			("lpParam",LPVOID)
			]
		
			
class RECT(ctypes.Structure):
	_fields_ = [
			("left", LONG),
			("top", LONG),
			("right", LONG),
			("bottom", LONG)
			]				
			
class PAINTSTRUCT(ctypes.Structure):
	_fields_ = [
			("hdc",HDC),
			("fErase",BOOL),
			("rcPaint",RECT),
			("fRestore",DWORD),
			("fIncUpdate",INT),
			("rgbReserved",BYTE*33),
			]			
			
		
			
			
			