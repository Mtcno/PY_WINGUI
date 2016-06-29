# -*- coding: utf-8 -*-
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


WC_COMBOBOXEXW	=	u"ComboBoxEx32"
WC_COMBOBOXEXA	=	b"ComboBoxEx32"
WC_IPADDRESSW	=	u"SysIPAddress32"
WC_IPADDRESSA	=	b"SysIPAddress32"
WC_LISTVIEWA	=	b"SysListView32"
WC_LISTVIEWW	=	u"SysListView32"
WC_TABCONTROLA	=	b"SysTabControl32"
WC_TABCONTROLW	=	u"SysTabControl32"
WC_TREEVIEWA	=	b"SysTreeView32"
WC_TREEVIEWW	=	u"SysTreeView32"
WC_HEADERA	=	b"SysHeader32"
WC_HEADERW 	=	u"SysHeader32"
WC_PAGESCROLLERW	=	u"SysPager"
WC_PAGESCROLLERA	=	b"SysPager"
WC_NATIVEFONTCTLW	=	u"NativeFontCtu"
WC_NATIVEFONTCTLA	=	b"NativeFontCtu"
WC_BUTTONA	=	b"Button"
WC_BUTTONW	=	u"Button"
WC_STATICA	=	b"Static"
WC_STATICW	=	u"Static"
WC_EDITA	=	b"Edit"
WC_EDITW	=	u"Edit"
WC_LISTBOXA	=	b"ListBox"
WC_LISTBOXW	=	u"ListBox"
WC_COMBOBOXA	=	b"ComboBox"
WC_COMBOBOXW	=	u"ComboBox"
WC_SCROLLBARA	=	b"ScrollBar"
WC_SCROLLBARW	=	u"ScrollBar"
WC_LINKA	=	b"SysLink"
WC_LINKW	=	u"SysLink"

HOTKEY_CLASSA	=	b"msctls_hotkey32"
HOTKEY_CLASSW	=	u"msctls_hotkey32"
PROGRESS_CLASSA	=	b"msctls_progress32"
PROGRESS_CLASSW	=	u"msctls_progress32"
STATUSCLASSNAMEA	=	b"msctls_statusbar32"
STATUSCLASSNAMEW	=	u"msctls_statusbar32"
TOOLBARCLASSNAMEA	=	b"ToolbarWindow32"
TOOLBARCLASSNAMEW	=	u"ToolbarWindow32"
TOOLTIPS_CLASSA	=	b"tooltips_class32"
TOOLTIPS_CLASSW	=	u"tooltips_class32"
TRACKBAR_CLASSA	=	b"msctls_trackbar32"
TRACKBAR_CLASSW	=	u"msctls_trackbar32"
UPDOWN_CLASSA	=	b"msctls_updown32"
UPDOWN_CLASSW	=	u"msctls_updown32"
ANIMATE_CLASSA	=	b"SysAnimate32"
ANIMATE_CLASSW	=	u"SysAnimate32"
DATETIMEPICK_CLASSW =	u"SysDateTimePick32"
DATETIMEPICK_CLASSA =	b"SysDateTimePick32"
MONTHCAL_CLASSW =	u"SysMonthCal32"
MONTHCAL_CLASSA =	b"SysMonthCal32"
REBARCLASSNAMEW =	u"ReBarWindow32"
REBARCLASSNAMEA =	b"ReBarWindow32"


ICC_LISTVIEW_CLASSES =1
ICC_TREEVIEW_CLASSES =2
ICC_BAR_CLASSES	=4
ICC_TAB_CLASSES      =8
ICC_UPDOWN_CLASS =16
ICC_PROGRESS_CLASS =32
ICC_HOTKEY_CLASS =64
ICC_ANIMATE_CLASS =128
ICC_WIN95_CLASSES =255
ICC_DATE_CLASSES =256
ICC_USEREX_CLASSES =512
ICC_COOL_CLASSES =1024

if _WIN32_IE >= 0x0400:
	ICC_INTERNET_CLASSES =2048
	ICC_PAGESCROLLER_CLASS =4096
	ICC_NATIVEFNTCTL_CLASS =8192
	INFOTIPSIZE =1024
	

LVIF_GROUPID =256
LVIF_COLUMNS =512	
	
#list ·ç¸ñ	
LVS_ICON	=0
LVS_REPORT	=1
LVS_SMALLICON	=2
LVS_LIST	=3
LVS_TYPEMASK	=3
LVS_SINGLESEL	=4
LVS_SHOWSELALWAYS	=8
LVS_SORTASCENDING	=16
LVS_SORTDESCENDING	=32
LVS_SHAREIMAGELISTS	=64
LVS_NOLABELWRAP	=128
LVS_AUTOARRANGE	=256
LVS_EDITLABELS	=512
LVS_NOSCROLL	=0x2000
LVS_TYPESTYLEMASK	=0xfc00
LVS_ALIGNTOP	=0
LVS_ALIGNLEFT	=0x800
LVS_ALIGNMASK	=0xc00
LVS_OWNERDRAWFIXED	=0x400
LVS_NOCOLUMNHEADER	=0x4000
LVS_NOSORTHEADER	=0x8000	
	
	
LVS_OWNERDATA =4096
LVS_EX_CHECKBOXES =4
LVS_EX_FULLROWSELECT =32
LVS_EX_GRIDLINES =1
LVS_EX_HEADERDRAGDROP =16
LVS_EX_ONECLICKACTIVATE =64
LVS_EX_SUBITEMIMAGES =2
LVS_EX_TRACKSELECT =8
LVS_EX_TWOCLICKACTIVATE =128
LVSICF_NOINVALIDATEALL	=0x00000001
LVSICF_NOSCROLL	=0x00000002	
	
	
#Columns
LVCF_FMT	=1
LVCF_WIDTH	=2
LVCF_TEXT	=4
LVCF_SUBITEM	=8
if _WIN32_IE >= 0x0300:
	LVCF_IMAGE =16
	LVCF_ORDER =32

LVCFMT_LEFT	=0
LVCFMT_RIGHT	=1
LVCFMT_CENTER	=2
LVCFMT_JUSTIFYMASK	=3

if (_WIN32_IE >= 0x0300):
	LVCFMT_BITMAP_ON_RIGHT =4096
	LVCFMT_COL_HAS_IMAGES  =32768
	LVCFMT_IMAGE =2048 	

#cmd msg	
LVM_FIRST = 0x1000	
	
LVM_GETCOLUMNA	=(LVM_FIRST+25)
LVM_GETCOLUMNW	=(LVM_FIRST+95)
LVM_SETCOLUMNA	=(LVM_FIRST+26)
LVM_SETCOLUMNW	=(LVM_FIRST+96)
LVM_INSERTCOLUMNA	=(LVM_FIRST+27)
LVM_INSERTCOLUMNW	=(LVM_FIRST+97)
LVM_DELETECOLUMN	=(LVM_FIRST+28)
LVM_GETCOLUMNWIDTH	=(LVM_FIRST+29)
LVSCW_AUTOSIZE	=(-1)
LVSCW_AUTOSIZE_USEHEADER	=(-2)
LVM_SETCOLUMNWIDTH	=(LVM_FIRST+30)
LVM_CREATEDRAGIMAGE	=(LVM_FIRST+33)
LVM_GETVIEWRECT	=(LVM_FIRST+34)
LVM_GETTEXTCOLOR	=(LVM_FIRST+35)
LVM_SETTEXTCOLOR	=(LVM_FIRST+36)
LVM_GETTEXTBKCOLOR	=(LVM_FIRST+37)
LVM_SETTEXTBKCOLOR	=(LVM_FIRST+38)
LVM_GETTOPINDEX	=(LVM_FIRST+39)
LVM_GETCOUNTPERPAGE	=(LVM_FIRST+40)
LVM_GETORIGIN	=(LVM_FIRST+41)
LVM_GETORIGIN	=(LVM_FIRST+41)
LVM_UPDATE	=(LVM_FIRST+42)
LVM_SETITEMSTATE	=(LVM_FIRST+43)
LVM_GETITEMSTATE	=(LVM_FIRST+44)
LVM_GETITEMTEXTA	=(LVM_FIRST+45)
LVM_GETITEMTEXTW	=(LVM_FIRST+115)
LVM_SETITEMTEXTA	=(LVM_FIRST+46)
LVM_SETITEMTEXTW	=(LVM_FIRST+116)
LVM_SETITEMCOUNT	=(LVM_FIRST+47)
LVM_SORTITEMS	=(LVM_FIRST+48)
LVM_SETITEMPOSITION32	=(LVM_FIRST+49)
LVM_GETSELECTEDCOUNT	=(LVM_FIRST+50)
LVM_GETITEMSPACING	=(LVM_FIRST+51)
LVM_GETISEARCHSTRINGA	=(LVM_FIRST+52)
LVM_GETISEARCHSTRINGW	=(LVM_FIRST+117)	
	

from wintydef import *

class INITCOMMONCONTROLSEX(ctypes.Structure):
	_fields_ = [
				("dwSize",DWORD),
				("dwICC",DWORD)
				]

if _WIN32_IE >= 0x0300:				
	class _LVCOLUMNA(ctypes.Structure):			
		_fields_ = [
					("mask",UINT),
					("fmt",INT),
					("cx",INT),
					("pszText",LPSTR),
					("cchTextMax",INT),
					("iSubItem",INT),
					("iImage",INT),
					("iOrder",INT)
					]
				
	class _LVCOLUMNW(ctypes.Structure):			
		_fields_ = [
					("mask",UINT),
					("fmt",INT),
					("cx",INT),
					("pszText",LPWSTR),
					("cchTextMax",INT),
					("iSubItem",INT),
					("iImage",INT),
					("iOrder",INT)
					]
elif _WIN32_WINNT >= 0x0600:
	class _LVCOLUMNA(ctypes.Structure):			
		_fields_ = [
					("mask",UINT),
					("fmt",INT),
					("cx",INT),
					("pszText",LPSTR),
					("cchTextMax",INT),
					("iSubItem",INT),
					("iImage",INT),
					("iOrder",INT)
					("cxMin",INT),
					("cxDefault",INT),
					("cxIdeal",INT)
					]
				
	class _LVCOLUMNW(ctypes.Structure):			
		_fields_ = [
					("mask",UINT),
					("fmt",INT),
					("cx",INT),
					("pszText",LPWSTR),
					("cchTextMax",INT),
					("iSubItem",INT),
					("iImage",INT),
					("iOrder",INT)
					("cxMin",INT),
					("cxDefault",INT),
					("cxIdeal",INT)
					]	
else:
	class _LVCOLUMNA(ctypes.Structure):			
		_fields_ = [
					("mask",UINT),
					("fmt",INT),
					("cx",INT),
					("pszText",LPSTR),
					("cchTextMax",INT),
					("iSubItem",INT),
					]
				
	class _LVCOLUMNW(ctypes.Structure):			
		_fields_ = [
					("mask",UINT),
					("fmt",INT),
					("cx",INT),
					("pszText",LPWSTR),
					("cchTextMax",INT),
					("iSubItem",INT),
					]						
					
					
LVCOLUMNA = _LVCOLUMNA
LVCOLUMNW = _LVCOLUMNW

from winuser import *
#function
InitCommonControlsEx = comctl32.InitCommonControlsEx
#(int)SNDMSG((w),LVM_INSERTCOLUMN,i,(LPARAM)(const LV_COLUMN*)(p))
def ListView_InsertColumnW(hWndListView,iCol,LVCOLUMN):
	pLVCOLUMN = ctypes.addressof(LVCOLUMN)
	if isinstance(LVCOLUMN,LVCOLUMNW):
		return SendMessageW(hWndListView,LVM_INSERTCOLUMNW,iCol,LPARAM(pLVCOLUMN))
	elif isinstance(LVCOLUMN,LVCOLUMNA):
		return SendMessageA(hWndListView,LVM_INSERTCOLUMNA,iCol,LPARAM(pLVCOLUMN))
	else:
		return False
		

if _WIN32_WINNT >= 0x0501 and _WIN32_IE < 0x0300 :
	class _LVITEMA(ctypes.Structure):
		_fields_ = [
					("mask",UINT),
					("iItem",INT),
					("iSubItem",INT),
					("state",UINT),
					("stateMask",UINT),
					("pszText",LPSTR),
					("cchTextMax",INT),
					("iImage",INT),
					("lParam",LPARAM),
					("iGroupId",INT),
					("cColumns",UINT),
					("puColumns",PUINT)	
					]
					
	class _LVITEMW(ctypes.Structure):
		_fields_ = [
					("mask",UINT),
					("iItem",INT),
					("iSubItem",INT),
					("state",UINT),
					("stateMask",UINT),
					("pszText",LPWSTR),
					("cchTextMax",INT),
					("iImage",INT),
					("lParam",LPARAM),
					("iGroupId",INT),
					("cColumns",UINT),
					("puColumns",PUINT)	
					]

elif _WIN32_WINNT >= 0x0501 and _WIN32_IE >= 0x0300 :
	class _LVITEMA(ctypes.Structure):
		_fields_ = [
					("mask",UINT),
					("iItem",INT),
					("iSubItem",INT),
					("state",UINT),
					("stateMask",UINT),
					("pszText",LPSTR),
					("cchTextMax",INT),
					("iImage",INT),
					("lParam",LPARAM),
					("iIndent",INT),
					("iGroupId",INT),
					("cColumns",UINT),
					("puColumns",PUINT)	
					]
					
	class _LVITEMW(ctypes.Structure):
		_fields_ = [
					("mask",UINT),
					("iItem",INT),
					("iSubItem",INT),
					("state",UINT),
					("stateMask",UINT),
					("pszText",LPWSTR),
					("cchTextMax",INT),
					("iImage",INT),
					("lParam",LPARAM),
					("iIndent",INT),
					("iGroupId",INT),
					("cColumns",UINT),
					("puColumns",PUINT)	
					]
					
elif _WIN32_WINNT >= 0x0600 and _WIN32_IE >= 0x0300 :
	class _LVITEMA(ctypes.Structure):
		_fields_ = [
					("mask",UINT),
					("iItem",INT),
					("iSubItem",INT),
					("state",UINT),
					("stateMask",UINT),
					("pszText",LPSTR),
					("cchTextMax",INT),
					("iImage",INT),
					("lParam",LPARAM),
					("iIndent",INT),
					("iGroupId",INT),
					("cColumns",UINT),
					("puColumns",PUINT)	
					("*piColFmt",INT),
					("iGroup",INT)
					]
					
	class _LVITEMW(ctypes.Structure):
		_fields_ = [
					("mask",UINT),
					("iItem",INT),
					("iSubItem",INT),
					("state",UINT),
					("stateMask",UINT),
					("pszText",LPWSTR),
					("cchTextMax",INT),
					("iImage",INT),
					("lParam",LPARAM),
					("iIndent",INT),
					("iGroupId",INT),
					("cColumns",UINT),
					("puColumns",PUINT),
					("*piColFmt",INT),
					("iGroup",INT)
					]
					
LVITEMA	= _LVITEMA				
LVITEMW	= _LVITEMW
					
LVIF_TEXT	=1
LVIF_IMAGE	=2
LVIF_PARAM	=4
LVIF_STATE	=8
if _WIN32_IE >= 0x0300:
	LVIF_INDENT =16
	LVIF_NORECOMPUTE =2048

if _WIN32_WINNT >= 0x0501:
	LVIF_GROUPID =256
	LVIF_COLUMNS =512					
					
LVM_INSERTITEMA	=(LVM_FIRST+7)
LVM_INSERTITEMW	=(LVM_FIRST+77)
LVM_DELETEITEM	=(LVM_FIRST+8)					
					
def ListView_InsertItem(hwnd,LVITEM):	
	pLVITEM = ctypes.addressof(LVITEM)
	if isinstance(LVITEM,LVITEMW):
		return SendMessageW(hwnd,LVM_INSERTITEMW,0,LPARAM(pLVITEM))
	elif isinstance(LVITEM,LVITEMA):	
		return SendMessageA(hwnd,LVM_INSERTITEMA,0,LPARAM(pLVITEM))	
	else:
		return False


LVM_SETITEMA = (LVM_FIRST+6)
LVM_SETITEMW = (LVM_FIRST+76)		
#ListView_SetItem(w,i) (BOOL)SNDMSG((w),LVM_SETITEM,0,(LPARAM)(const LV_ITEM*)(i))			
def ListView_SetItem(hwnd,LVITEM):
	pLVITEM = ctypes.addressof(LVITEM)
	if isinstance(LVITEM,LVITEMW):
		return SendMessageW(hwnd,LVM_SETITEMW,0,LPARAM(pLVITEM))		
	elif isinstance(LVITEM,LVITEMA):
		return SendMessageA(hwnd,LVM_SETITEMA,0,LPARAM(pLVITEM))		
	
	
LVM_SETITEMTEXTA=(LVM_FIRST+46)
LVM_SETITEMTEXTW=(LVM_FIRST+116)

def ListView_SetItemText(hwnd,row,col,pszText):

	
	
	if isinstance(pszText,str):
		LVITEM	= LVITEMW()
		LVITEM.iSubItem = col
		LVITEM.pszText = LPWSTR(pszText)
		pLVITEM = ctypes.addressof(LVITEM)
		return SendMessageW(hwnd,LVM_SETITEMTEXTW,row,LPARAM(pLVITEM))
	else:
		LVITEM	= LVITEMA()
		LVITEM.iSubItem = col
		LVITEM.pszText = LPSTR(pszText)
		pLVITEM	= ctypes.addressof(LVITEM)		
		return SendMessageA(hwnd,LVM_SETITEMTEXTA,row,LPARAM(pLVITEM))


		
if _WIN32_IE >= 0x0300:
	LVM_APPROXIMATEVIEWRECT =(LVM_FIRST+64)
	LVM_SETEXTENDEDLISTVIEWSTYLE =(LVM_FIRST+54)
	LVM_GETEXTENDEDLISTVIEWSTYLE =(LVM_FIRST+55)
	LVM_SETCOLUMNORDERARRAY =(LVM_FIRST+58)
	LVM_GETCOLUMNORDERARRAY =(LVM_FIRST+59)
	LVM_GETHEADER =(LVM_FIRST+31)
	LVM_GETHOTCURSOR =(LVM_FIRST+63)
	LVM_GETHOTITEM =(LVM_FIRST+61)
	LVM_GETSUBITEMRECT =(LVM_FIRST+56)
	LVM_SETHOTCURSOR =(LVM_FIRST+62)
	LVM_SETHOTITEM =(LVM_FIRST+60)
	LVM_SETICONSPACING =(LVM_FIRST+53)
	LVM_SUBITEMHITTEST =(LVM_FIRST+57)
	
LVN_FIRST	= -100
LVN_ITEMCHANGING	=LVN_FIRST
LVN_ITEMCHANGED	=(LVN_FIRST-1)
LVN_INSERTITEM	=(LVN_FIRST-2)
LVN_DELETEITEM	=(LVN_FIRST-3)
LVN_DELETEALLITEMS	=(LVN_FIRST-4)
LVN_BEGINLABELEDITA	=(LVN_FIRST-5)
LVN_BEGINLABELEDITW	=(LVN_FIRST-75)
LVN_ENDLABELEDITA	=(LVN_FIRST-6)
LVN_ENDLABELEDITW	=(LVN_FIRST-76)
LVN_COLUMNCLICK	=(LVN_FIRST-8)
LVN_BEGINDRAG	=(LVN_FIRST-9)
LVN_BEGINRDRAG	=(LVN_FIRST-11)
LVN_GETDISPINFOA	=(LVN_FIRST-50)
LVN_GETDISPINFOW	=(LVN_FIRST-77)
LVN_SETDISPINFOA	=(LVN_FIRST-51)
LVN_SETDISPINFOW	=(LVN_FIRST-78)
LVN_KEYDOWN	=(LVN_FIRST-55)
	
def ListView_SetExtendedListViewStyle(hwnd,style):
	return SendMessageW(hwnd,LVM_SETEXTENDEDLISTVIEWSTYLE,0,style)
					
					
					
					
					
					
					
					
					
					
					
					
					