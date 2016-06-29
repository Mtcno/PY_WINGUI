# -*- coding: utf-8 -*-

from wintydef import *
from winstruct import *

#_WIN32_WINNT version constants 
#_WIN32_WINNT_NT4                    0x0400 // Windows NT 4.0 
#_WIN32_WINNT_WIN2K                  0x0500 // Windows 2000 
#_WIN32_WINNT_WINXP                  0x0501 // Windows XP 
#_WIN32_WINNT_WS03                   0x0502 // Windows Server 2003 
#_WIN32_WINNT_WIN6                   0x0600 // Windows Vista 
#_WIN32_WINNT_VISTA                  0x0600 // Windows Vista 
#_WIN32_WINNT_WS08                   0x0600 // Windows Server 2008 
#_WIN32_WINNT_LONGHORN               0x0600 // Windows Vista 
#_WIN32_WINNT_WIN7                   0x0601 // Windows 7 
#_WIN32_WINNT_WIN8                   0x0602 // Windows 8 
#_WIN32_WINNT_WINBLUE                0x0603 // Windows 8.1 
#_WIN32_WINNT_WINTHRESHOLD           0x0A00 // Windows 10 
#_WIN32_WINNT_WIN10                  0x0A00 // Windows 10
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

	
	
	
	
	
#WndProc MSG define	
WM_APP  = 32768
WM_ACTIVATE  = 6
WM_ACTIVATEAPP  = 28
WM_AFXFIRST  = 864
WM_AFXLAST  = 895
WM_ASKCBFORMATNAME  = 780
WM_CANCELJOURNAL  = 75
WM_CANCELMODE  = 31
WM_CAPTURECHANGED  = 533
WM_CHANGECBCHAIN  = 781
WM_CHAR  = 258
WM_CHARTOITEM  = 47
WM_CHILDACTIVATE  = 34
WM_CLEAR  = 771
WM_CLOSE  = 16
WM_COMMAND  = 273
WM_COMMNOTIFY  = 68		
WM_COMPACTING  = 65
WM_COMPAREITEM  = 57
WM_CONTEXTMENU  = 123
WM_COPY = 769
WM_COPYDATA  = 74
WM_CREATE  = 1
WM_CTLCOLORBTN = 309
WM_CTLCOLORDLG = 310
WM_CTLCOLOREDIT = 307
WM_CTLCOLORLISTBOX = 308
WM_CTLCOLORMSGBOX = 306
WM_CTLCOLORSCROLLBAR = 311
WM_CTLCOLORSTATIC = 312
WM_CUT = 768
WM_DEADCHAR = 259
WM_DELETEITEM = 45
WM_DESTROY = 2
WM_DESTROYCLIPBOARD = 775
WM_DEVICECHANGE  = 537
WM_DEVMODECHANGE  = 27
WM_DISPLAYCHANGE  = 126
WM_DRAWCLIPBOARD  = 776
WM_DRAWITEM = 43
WM_DROPFILES = 563
WM_ENABLE  = 10
WM_ENDSESSION  = 22
WM_ENTERIDLE  = 289
WM_ENTERMENULOOP  = 529
WM_ENTERSIZEMOVE  = 561
WM_ERASEBKGND  = 20
WM_EXITMENULOOP  = 530
WM_EXITSIZEMOVE  = 562
WM_FONTCHANGE  = 29
WM_GETDLGCODE  = 135
WM_GETFONT  = 49
WM_GETHOTKEY  = 51
WM_GETICON  = 127
WM_GETMINMAXINFO  = 36
WM_GETTEXT  = 13
WM_GETTEXTLENGTH  = 14
WM_HANDHELDFIRST  = 856
WM_HANDHELDLAST  = 863
WM_HELP  = 83
WM_HOTKEY  = 786
WM_HSCROLL  = 276
WM_HSCROLLCLIPBOARD  = 782
WM_ICONERASEBKGND  = 39
WM_INITDIALOG  = 272
WM_INITMENU  = 278
WM_INITMENUPOPUP  = 279

if _WIN32_WINNT >= 0x0501:
	WM_INPUT  = 0x00FF

WM_INPUTLANGCHANGE  = 81
WM_INPUTLANGCHANGEREQUEST  = 80
WM_KEYDOWN  = 256
WM_KEYUP  = 257
WM_KILLFOCUS  = 8
WM_MDIACTIVATE  = 546
WM_MDICASCADE  = 551
WM_MDICREATE  = 544
WM_MDIDESTROY  = 545
WM_MDIGETACTIVE  = 553
WM_MDIICONARRANGE  = 552
WM_MDIMAXIMIZE  = 549
WM_MDINEXT  = 548
WM_MDIREFRESHMENU  = 564
WM_MDIRESTORE  = 547
WM_MDISETMENU  = 560
WM_MDITILE  = 550
WM_MEASUREITEM  = 44

if WINVER >= 0x0500:
	WM_GETOBJECT  = 0x003D
	WM_CHANGEUISTATE  = 0x0127
	WM_UPDATEUISTATE  = 0x0128
	WM_QUERYUISTATE  = 0x0129
	WM_UNINITMENUPOPUP  = 0x0125
	WM_MENURBUTTONUP  = 290
	WM_MENUCOMMAND  = 0x0126
	WM_MENUGETOBJECT  = 0x0124
	WM_MENUDRAG  = 0x0123
	WM_APPCOMMAND  = 0x0319

WM_MENUCHAR  = 288
WM_MENUSELECT  = 287
WM_NEXTMENU  = 531
WM_MOVE  = 3
WM_MOVING  = 534
WM_NCACTIVATE  = 134
WM_NCCALCSIZE  = 131
WM_NCCREATE  = 129
WM_NCDESTROY  = 130
WM_NCHITTEST  = 132
WM_NCLBUTTONDBLCLK  = 163
WM_NCLBUTTONDOWN  = 161
WM_NCLBUTTONUP  = 162
WM_NCMBUTTONDBLCLK  = 169
WM_NCMBUTTONDOWN  = 167
WM_NCMBUTTONUP  = 168

if _WIN32_WINNT >= 0x0500:
	WM_NCXBUTTONDOWN  = 171
	WM_NCXBUTTONUP  = 172
	WM_NCXBUTTONDBLCLK  = 173
	WM_NCMOUSEHOVER  = 0x02A0
	WM_NCMOUSELEAVE  = 0x02A2

WM_NCMOUSEMOVE  = 160
WM_NCPAINT  = 133
WM_NCRBUTTONDBLCLK  = 166
WM_NCRBUTTONDOWN  = 164
WM_NCRBUTTONUP  = 165
WM_NEXTDLGCTL  = 40
WM_NEXTMENU  = 531
WM_NOTIFY  = 78
WM_NOTIFYFORMAT  = 85
WM_NULL  = 0
WM_PAINT  = 15
WM_PAINTCLIPBOARD  = 777
WM_PAINTICON  = 38
WM_PALETTECHANGED  = 785
WM_PALETTEISCHANGING  = 784
WM_PARENTNOTIFY  = 528
WM_PASTE  = 770
WM_PENWINFIRST  = 896
WM_PENWINLAST  = 911
WM_POWER  = 72
WM_POWERBROADCAST  = 536
WM_PRINT  = 791
WM_PRINTCLIENT  = 792
WM_QUERYDRAGICON  = 55
WM_QUERYENDSESSION  = 17
WM_QUERYNEWPALETTE  = 783
WM_QUERYOPEN  = 19
WM_QUEUESYNC  = 35
WM_QUIT  = 18
WM_RENDERALLFORMATS  = 774
WM_RENDERFORMAT  = 773
WM_SETCURSOR  = 32
WM_SETFOCUS  = 7
WM_SETFONT  = 48
WM_SETHOTKEY  = 50
WM_SETICON  = 128
WM_SETREDRAW  = 11
WM_SETTEXT  = 12
WM_SETTINGCHANGE  = 26
WM_SHOWWINDOW  = 24
WM_SIZE  = 5
WM_SIZECLIPBOARD  = 779
WM_SIZING  = 532
WM_SPOOLERSTATUS  = 42
WM_STYLECHANGED  = 125
WM_STYLECHANGING  = 124
WM_SYSCHAR  = 262
WM_SYSCOLORCHANGE  = 21
WM_SYSCOMMAND  = 274
WM_SYSDEADCHAR  = 263
WM_SYSKEYDOWN  = 260
WM_SYSKEYUP  = 261
WM_TCARD  = 82
WM_THEMECHANGED  = 794
WM_TIMECHANGE  = 30
WM_TIMER  = 275
WM_UNDO  = 772
WM_USER  = 1024
WM_USERCHANGED  = 84
WM_VKEYTOITEM  = 46
WM_VSCROLL  = 277
WM_VSCROLLCLIPBOARD  = 778
WM_WINDOWPOSCHANGED  = 71
WM_WINDOWPOSCHANGING  = 70
WM_WININICHANGE  = 26
WM_KEYFIRST  = 256

if _WIN32_WINNT >= 0x0501:
	WM_KEYLAST  = 265
	WM_UNICHAR  = 265
	UNICODE_NOCHAR = 0xffff
else:
	WM_KEYLAST  = 264

WM_SYNCPAINT   = 136
WM_MOUSEACTIVATE  = 33
WM_MOUSEMOVE  = 512
WM_LBUTTONDOWN  = 513
WM_LBUTTONUP  = 514
WM_LBUTTONDBLCLK  = 515
WM_RBUTTONDOWN  = 516
WM_RBUTTONUP  = 517
WM_RBUTTONDBLCLK  = 518
WM_MBUTTONDOWN  = 519
WM_MBUTTONUP  = 520
WM_MBUTTONDBLCLK  = 521
WM_MOUSEWHEEL  = 522
WM_MOUSEFIRST  = 512

if _WIN32_WINNT >= 0x0500:
	WM_XBUTTONDOWN  = 523
	WM_XBUTTONUP  = 524
	WM_XBUTTONDBLCLK  = 525
	WM_MOUSELAST  = 525
else:
	WM_MOUSELAST  = 522

WM_MOUSEHOVER = 0x2A1
WM_MOUSELEAVE = 0x2A3

if _WIN32_WINNT >= 0x0400:
	WHEEL_DELTA = 120

if _WIN32_WINNT >= 0x0601:
	WM_TOUCHMOVE  = 576
	WM_TOUCHDOWN  = 577
	WM_TOUCHUP  = 578


#lpIconName
IDI_APPLICATION = 32512
IDI_ASTERISK = 32516
IDI_ERROR = 32513
IDI_EXCLAMATION = 32515
IDI_HAND = 32513
IDI_INFORMATION = 332516
IDI_QUESTION = 32514
IDI_SHIELD_A = 32518
IDI_WARNING = 32515
IDI_WINLOGO = 32517
#lpCursorName
IDC_APPSTARTING = 32650
IDC_ARROW = 32512
IDC_CROSS = 32515
IDC_HAND = 32649
IDC_HELP = 32651
IDC_IBEAM = 32513
IDC_ICON = 32641
IDC_NO = 32648
IDC_SIZE = 32640
IDC_SIZEALL = 32646
IDC_SIZENESW = 32643
IDC_SIZENS = 32645
IDC_SIZENWSE = 32642
IDC_SIZEWE = 32644
IDC_UPARROW = 32516
IDC_WAIT = 32514



#
#Window exStyles	
WS_EX_ACCEPTFILES = 0x00000010	
WS_EX_APPWINDOW = 0x00040000
WS_EX_CLIENTEDGE = 0x00000200
WS_EX_COMPOSITED = 0x02000000
WS_EX_CONTEXTHELP = 0x00000400
WS_EX_CONTROLPARENT = 0x00010000
WS_EX_DLGMODALFRAME = 0x00000001
WS_EX_LAYERED = 0x00080000
WS_EX_LAYOUTRTL = 0x00400000
WS_EX_LEFT = 0x00000000
WS_EX_LEFTSCROLLBAR = 0x00004000
WS_EX_LTRREADING = 0x00000000
WS_EX_MDICHILD = 0x00000040
WS_EX_NOACTIVATE = 0x08000000
WS_EX_NOINHERITLAYOUT = 0x00100000
WS_EX_NOPARENTNOTIFY = 0x00000004
WS_EX_NOREDIRECTIONBITMAP = 0x00200000
WS_EX_RIGHT = 0x00001000
WS_EX_RIGHTSCROLLBAR = 0x00000000
WS_EX_RTLREADING = 0x00002000
WS_EX_STATICEDGE = 0x00020000
WS_EX_TOOLWINDOW = 0x00000080
WS_EX_TOPMOST = 0x00000008
WS_EX_TRANSPARENT = 0x00000020
WS_EX_WINDOWEDGE = 0x00000100
WS_EX_OVERLAPPEDWINDOW = WS_EX_WINDOWEDGE | WS_EX_CLIENTEDGE
WS_EX_PALETTEWINDOW = WS_EX_WINDOWEDGE | WS_EX_TOOLWINDOW | WS_EX_TOPMOST

#
#Window Styles
WS_BORDER = 0x00800000
WS_CAPTION = 0x00C00000
WS_CHILD = 0x40000000
WS_CHILDWINDOW = 0x40000000
WS_CLIPCHILDREN = 0x02000000
WS_CLIPSIBLINGS = 0x04000000
WS_DISABLED = 0x08000000
WS_DLGFRAME = 0x00400000
WS_GROUP = 0x00020000
WS_HSCROLL = 0x00100000
WS_ICONIC = 0x20000000
WS_MAXIMIZE = 0x01000000
WS_MAXIMIZEBOX = 0x00010000
WS_MINIMIZE = 0x20000000
WS_MINIMIZEBOX = 0x00020000
WS_OVERLAPPED = 0x00000000
WS_POPUP = 0x80000000
WS_SIZEBOX = 0x00040000
WS_SYSMENU = 0x00080000
WS_TABSTOP = 0x00010000
WS_THICKFRAME = 0x00040000
WS_TILED = 0x00000000
WS_VISIBLE = 0x10000000
WS_VSCROLL = 0x00200000
WS_POPUPWINDOW = WS_POPUP | WS_BORDER | WS_SYSMENU
WS_OVERLAPPEDWINDOW = WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU | WS_THICKFRAME | WS_MINIMIZEBOX | WS_MAXIMIZEBOX
WS_TILEDWINDOW = WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU | WS_THICKFRAME | WS_MINIMIZEBOX | WS_MAXIMIZEBOX

CW_USEDEFAULT = 0x80000000


#User32
#nCmdShow
SW_FORCEMINIMIZE = 11
SW_HIDE = 0
SW_MAXIMIZE = 3
SW_MINIMIZE = 6
SW_RESTORE = 9
SW_SHOW = 5
SW_SHOWDEFAULT = 10
SW_SHOWMAXIMIZED = 2
SW_SHOWMINIMIZED = 3
SW_SHOWMINNOACTIVE = 7
SW_SHOWNA = 8
SW_SHOWNOACTIVATE = 4
SW_SHOWNORMAL = 1

#WNDCLASSE style 
CS_DBLCLKS = 8
CS_HREDRAW = 2
CS_NOCLOSE = 512
CS_PARENTDC = 128
CS_VREDRAW = 1

#hbrBackground
COLOR_ACTIVEBORDER = 10
COLOR_ACTIVECAPTION = 2
COLOR_APPWORKSPACE = 12
COLOR_BACKGROUND = 1
COLOR_BTNFACE = 15
COLOR_BTNHIGHLIGHT = 20
COLOR_BTNSHADOW = 16
COLOR_BTNTEXT = 18
COLOR_CAPTIONTEXT = 9
COLOR_GRAYTEXT = 17
COLOR_HIGHLIGHT = 13
COLOR_HIGHLIGHTTEXT = 14
COLOR_INACTIVEBORDER = 11
COLOR_INACTIVECAPTION = 3
COLOR_MENU = 4
COLOR_MENUTEXT = 7
COLOR_SCROLLBAR = 0
COLOR_WINDOW = 5
COLOR_WINDOWFRAME = 6
COLOR_WINDOWTEXT = 8
#??
COLOR_3DDKSHADOW = 21
COLOR_3DFACE = 15
COLOR_3DHILIGHT = 20
COLOR_3DHIGHLIGHT = 20
COLOR_3DLIGHT = 22
COLOR_BTNHILIGHT = 20
COLOR_3DSHADOW = 16
COLOR_DESKTOP = 1
COLOR_INACTIVECAPTIONTEXT = 19
COLOR_INFOBK = 24
COLOR_INFOTEXT = 23
COLOR_HOTLIGHT = 26
COLOR_GRADIENTACTIVECAPTION = 27
COLOR_GRADIENTINACTIVECAPTION =28



#User32.dll function
GetSysColorBrush = user32.GetSysColorBrush
GetSysColor = user32.GetSysColor
BeginPaint = user32.BeginPaint
EndPaint = user32.EndPaint


#菜单
MF_BYCOMMAND	=0
MF_BYPOSITION	=1024
MF_UNCHECKED	=0
MF_HILITE	=128
MF_UNHILITE	=0

MF_ENABLED	=0
MF_GRAYED	=1
MF_DISABLED	=2
MF_BITMAP	=4
MF_CHECKED	=8
MF_MENUBARBREAK =32
MF_MENUBREAK	=64
MF_OWNERDRAW	=256
MF_POPUP	=16
MF_SEPARATOR	=0x800
MF_STRING	=0
MF_UNCHECKED	=0
MF_DEFAULT	=4096
MF_SYSMENU	=0x2000
MF_HELP	=0x4000
MF_END	=128
MF_RIGHTJUSTIFY	=0x4000
MF_MOUSESELECT	=0x8000
MF_INSERT =0
MF_CHANGE =128
MF_APPEND =256
MF_DELETE =512
MF_REMOVE =4096
MF_USECHECKBITMAPS =512
MF_UNHILITE =0
MF_HILITE =128

MIIM_STATE =1
MIIM_ID =2
MIIM_SUBMENU =4
MIIM_CHECKMARKS =8
MIIM_TYPE =16
MIIM_DATA =32
MIIM_STRING =64
MIIM_BITMAP =128
MIIM_FTYPE =256

class MENUITEMINFOA(ctypes.Structure):
	_fields_ =[ 
				("cbSize",UINT),
				("fMask",UINT),
				("fType",UINT),
				("fState",UINT),
				("wID",UINT),
				("hSubMenu",HMENU),
				("hbmpChecked",HBITMAP),
				("hbmpUnchecked",HBITMAP),
				("dwItemData",ULONG_PTR),
				("dwTypeData",LPSTR),
				("cch",UINT),
				("hbmpItem",HBITMAP)
				]
				
class MENUITEMINFOW(ctypes.Structure):
	_fields_ =[ 
				("cbSize",UINT),
				("fMask",UINT),
				("fType",UINT),
				("fState",UINT),
				("wID",UINT),
				("hSubMenu",HMENU),
				("hbmpChecked",HBITMAP),
				("hbmpUnchecked",HBITMAP),
				("dwItemData",ULONG_PTR),
				("dwTypeData",LPWSTR),
				("cch",UINT),
				("hbmpItem",HBITMAP)
				]				
				
GetMenuItemInfoA = user32.GetMenuItemInfoA
GetMenuItemInfoW = user32.GetMenuItemInfoW

def AppendMenu( hMenu, uFlags, uIDNewltem, lpNewltem):
	if isinstance(lpNewltem,bytes):
		return user32.AppendMenuA( hMenu, uFlags, uIDNewltem, lpNewltem)
	else:
		return user32.AppendMenuW( hMenu, uFlags, uIDNewltem, lpNewltem)

	
# DWORD WINAPI CheckMenuItem(
# 	_In_ HMENU hmenu,     	 	//Type: HMENU ,A handle to the menu of interest.
# 	_In_ UINT  uIDCheckItem,  	//Type: UINT ,The menu item whose check-mark attribute is to be set, as determined by the uCheck parameter.
# 	_In_ UINT  uCheck			//Type: UINT ,The flags that control the interpretation of the uIDCheckItem parameter and the state of the menu item's check-mark attribute. This parameter can be a combination of either MF_BYCOMMAND, or MF_BYPOSITION and MF_CHECKED or MF_UNCHECKED.
# );
	
CheckMenuItem = user32.CheckMenuItem
CheckMenuRadioItem = user32.CheckMenuRadioItem	
CreateMenu = user32.CreateMenu
CreatePopupMenu = user32.CreatePopupMenu
DeleteMenu = user32.DeleteMenu
DestroyMenu = user32.DestroyMenu
DrawMenuBar = user32.DrawMenuBar
RemoveMenu = user32.RemoveMenu

EndMenu = user32.EndMenu
SetMenu = user32.SetMenu
EnableMenuItem = user32.EnableMenuItem
GetMenuItemID = user32.GetMenuItemID
GetMenuState = user32.GetMenuState #高位返回 子项数目 ，低位返回菜单 uFlags
def ModifyMenu(	hMnu,
				uPosition,
				uFlags,
				uIDNewItem,
				lpNewItem):
	if isinstance(lpNewItem,str):			
		return user32.ModifyMenuW(hMnu,uPosition,uFlags,uIDNewItem,lpNewItem)
	else:
		return user32.ModifyMenuA(hMnu,uPosition,uFlags,uIDNewItem,lpNewItem)

		
def InsertMenu(hMnu,uPosition,uFlags,uIDNewItem,lpNewItem):		
	if isinstance(lpNewItem,str):				
		return user32.InsertMenuW(hMnu,uPosition,uFlags,uIDNewItem,lpNewItem)
	else:		
		return user32.InsertMenuA(hMnu,uPosition,uFlags,uIDNewItem,lpNewItem)	
		
		
		
		

#屏幕
SM_CXSCREEN =0
SM_CYSCREEN =1
SM_CXVSCROLL =2
SM_CYHSCROLL =3
SM_CYCAPTION =4
SM_CXBORDER =5
SM_CYBORDER =6
SM_CXDLGFRAME =7
SM_CXFIXEDFRAME =7
SM_CYDLGFRAME =8
SM_CYFIXEDFRAME =8
SM_CYVTHUMB =9
SM_CXHTHUMB =10
SM_CXICON =11
SM_CYICON =12
SM_CXCURSOR =13
SM_CYCURSOR =14
SM_CYMENU =15
SM_CXFULLSCREEN =16
SM_CYFULLSCREEN =17
SM_CYKANJIWINDOW =18
SM_MOUSEPRESENT =19
SM_CYVSCROLL =20
SM_CXHSCROLL =21
SM_DEBUG =22
SM_SWAPBUTTON =23
SM_RESERVED1 =24
SM_RESERVED2 =25
SM_RESERVED3 =26
SM_RESERVED4 =27
SM_CXMIN =28
SM_CYMIN =29
SM_CXSIZE =30
SM_CYSIZE =31
SM_CXSIZEFRAME =32
SM_CXFRAME =32
SM_CYSIZEFRAME =33
SM_CYFRAME =33
SM_CXMINTRACK =34
SM_CYMINTRACK =35
SM_CXDOUBLECLK =36
SM_CYDOUBLECLK =37
SM_CXICONSPACING =38
SM_CYICONSPACING =39
SM_MENUDROPALIGNMENT =40
SM_PENWINDOWS =41
SM_DBCSENABLED =42
SM_CMOUSEBUTTONS =43
SM_SECURE =44
SM_CXEDGE =45
SM_CYEDGE =46
SM_CXMINSPACING =47
SM_CYMINSPACING =48
SM_CXSMICON =49
SM_CYSMICON =50
SM_CYSMCAPTION =51
SM_CXSMSIZE =52
SM_CYSMSIZE =53
SM_CXMENUSIZE =54
SM_CYMENUSIZE =55
SM_ARRANGE =56
SM_CXMINIMIZED =57
SM_CYMINIMIZED =58
SM_CXMAXTRACK =59
SM_CYMAXTRACK =60
SM_CXMAXIMIZED =61
SM_CYMAXIMIZED =62
SM_NETWORK =63
SM_CLEANBOOT =67
SM_CXDRAG =68
SM_CYDRAG =69
SM_SHOWSOUNDS =70
SM_CXMENUCHECK =71
SM_CYMENUCHECK =72
SM_SLOWMACHINE =73
SM_MIDEASTENABLED =74
SM_MOUSEWHEELPRESENT =75
SM_XVIRTUALSCREEN =76
SM_YVIRTUALSCREEN =77
SM_CXVIRTUALSCREEN =78
SM_CYVIRTUALSCREEN =79
SM_CMONITORS =80
SM_SAMEDISPLAYFORMAT =81
SM_IMMENABLED =82
SM_CXFOCUSBORDER =83
SM_CYFOCUSBORDER =84
SM_TABLETPC =86
SM_MEDIACENTER =87
SM_STARTER =88
SM_SERVERR2 =89

if _WIN32_WINNT < 0x0400:
	SM_CMETRICS =76
else:
	SM_CMETRICS =88
	
SM_REMOTESESSION =0X1000

GetSystemMetrics = user32.GetSystemMetrics

def MoveWindow(hwnd,x,y,width,height,bRepaint):
	return user32.MoveWindow(hwnd,int(x),int(y),width,height,bRepaint)




def MAKEINTRESOURCEA(i):
	return LPSTR(i)

def MAKEINTRESOURCEW(i):
	return LPWSTR(i)

def LoadIconA(hInstance,lpIconName):
	hInstance = HINSTANCE(hInstance)
	lpIconName = MAKEINTRESOURCEA(lpIconName)
	return user32.LoadIconA(hInstance,lpIconName)

def LoadIconW(hInstance,lpIconName):
	hInstance = HINSTANCE(hInstance)
	lpIconName = MAKEINTRESOURCEW(lpIconName)
	return user32.LoadIconW(hInstance,lpIconName)

def LoadCursorA(hInstance,lpCursorName):
	hInstance = HINSTANCE(hInstance)
	lpCursorName = MAKEINTRESOURCEA(lpCursorName)
	return user32.LoadCursorA(hInstance,lpCursorName)

def LoadCursorW(hInstance,lpCursorName):
	hInstance = HINSTANCE(hInstance)
	lpCursorName = MAKEINTRESOURCEW(lpCursorName)
	return user32.LoadCursorW(hInstance,lpCursorName)

def RegisterClassExA(lpWndClass):
	return user32.RegisterClassExA(lpWndClass)

def RegisterClassExW(lpWndClass):
	return user32.RegisterClassExW(lpWndClass)	


def ShowWindow(hWnd,nCmdShow):
	return user32.ShowWindow(hWnd,nCmdShow)

def UpdateWindow(hWnd):
	return user32.UpdateWindow(hWnd)

def DefWindowProcA(hwnd,Msg,wParam,IParam):
	return user32.DefWindowProcA(hwnd,Msg,wParam,IParam)

def DefWindowProcW(hwnd,Msg,wParam,IParam):
	return user32.DefWindowProcW(hwnd,Msg,wParam,IParam)

def PostQuitMessage(nExitCode):
	return user32.PostQuitMessage(nExitCode)

def TranslateMessage(pMSG):
	return user32.TranslateMessage(pMSG)	

def CreateWindowA(CWindowA):
	ret = user32.CreateWindowExA(
		0,
		CWindowA.lpClassName,
		CWindowA.lpWindowName,
		CWindowA.dwStyle,
		CWindowA.x,
		CWindowA.y,
		CWindowA.nWidth,
		CWindowA.nHeight,
		CWindowA.hWndParent,
		CWindowA.hMenu,
		CWindowA.hInstance,
		CWindowA.lpParam
	)
	return ret

def CreateWindowW(CWindowW):
	ret = user32.CreateWindowExW(
		0,
		CWindowW.lpClassName,
		CWindowW.lpWindowName,
		CWindowW.dwStyle,
		CWindowW.x,
		CWindowW.y,
		CWindowW.nWidth,
		CWindowW.nHeight,
		CWindowW.hWndParent,
		CWindowW.hMenu,
		CWindowW.hInstance,
		CWindowW.lpParam
	)
	return ret

def CreateWindowExA(CWindowExA):
	ret = user32.CreateWindowExA(
		CWindowExA.dwExStyle,
		CWindowExA.lpClassName,
		CWindowExA.lpWindowName,
		CWindowExA.dwStyle,
		CWindowExA.x,
		CWindowExA.y,
		CWindowExA.nWidth,
		CWindowExA.nHeight,
		CWindowExA.hWndParent,
		CWindowExA.hMenu,
		CWindowExA.hInstance,
		CWindowExA.lpParam
	)
	return ret

def CreateWindowExW(CWindowExW):
	ret = user32.CreateWindowExW(
		CWindowExW.dwExStyle,
		CWindowExW.lpClassName,
		CWindowExW.lpWindowName,
		CWindowExW.dwStyle,
		CWindowExW.x,
		CWindowExW.y,
		CWindowExW.nWidth,
		CWindowExW.nHeight,
		CWindowExW.hWndParent,
		CWindowExW.hMenu,
		CWindowExW.hInstance,
		CWindowExW.lpParam
	)
	return ret


def CreateWindow(wincls):	
	if isinstance(wincls,CWindowA):
		return CreateWindowA(wincls)		
	elif isinstance(wincls,CWindowW):
		return CreateWindowW(wincls)		
	elif isinstance(wincls,CWindowExA):
		return CreateWindowExA(wincls)	
	elif isinstance(wincls,CWindowExW):	
		return CreateWindowExW(wincls)
		
def GetClientRect(hWnd,lpRect):
	return user32.GetClientRect(hWnd,getpointer(lpRect))
		
def SendMessageW(hWnd,Msg,wParam,IParam):		
	return user32.SendMessageW(hWnd,Msg,wParam,IParam)	
		
def SendMessageA(hWnd,Msg,wParam,IParam):	
	return user32.SendMessageA(hWnd,Msg,wParam,IParam)		
		
def AdjustWindowRect(lpRect,dwStyle,bMenu):
	return user32.AdjustWindowRect(hWnd,Msg,wParam,IParam)	
		

		
		
# def GetDlgItem(id):
	# return user32.GetDlgItem(id)		
		
		
