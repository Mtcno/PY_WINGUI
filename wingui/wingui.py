# -*- coding: utf-8 -*-

from wintydef import *
from winuser import *
from wingdi32 import *
from winstruct import *
from CommCtrl import *


#全局--------------------------------
wCharFlag = None
#GetLastError()
GetLastError = kernel32.GetLastError
LastError = 0

LVAllHandle = {}

#为消息机制指定function
funcMsgCall = {}

#func
def funPass():
	pass
#-----------全局结束--------------------

#窗体控件
#Wnd center
def Wndtocenter(hwnd,x=900,y=600):	#窗口居中，默认大小 900x600
	monitor_width = (GetSystemMetrics(SM_CXSCREEN) - x)/2
	monitor_height = (GetSystemMetrics(SM_CYSCREEN) - y)/2
	MoveWindow(hwnd, monitor_width, monitor_height, x, y, True)

#菜单信息
def GetMenuItemInfo(hMenu, uItem, fMask):
	if wCharFlag == True:
		mii = MENUITEMINFOW()
		mii.cbSize = sizeof(mii)
		mii.fMask = fMask 
		lpmii = getpointer(mii)
		ret =  GetMenuItemInfoW(hMenu,uItem,False,lpmii)
	else:	
		mii = MENUITEMINFOA()
		mii.cbSize = sizeof(mii)
		mii.fMask = fMask
		lpmii = getpointer(mii)
		ret =  GetMenuItemInfoA(hMenu,uItem,False,lpmii)
	
	if ret == True:
		return mii
	elif ret == 0:
		return ret


#菜单栏	
#CreateMenu
class CreateMenuBar:
	def __init__(self):
		self.hWnd = None
		self.hMenu = CreateMenu()	#由系统生成菜单句柄
		self.MenuFunc ={}			#菜单栏功能绑定 { hMenu:function } 
		self.List_BarMenuName = []
		self.List_BarMenuHandle = []
		self.List_BarMenuType = []
		self.List_ItemMenuName = []
		self.List_ItemMenuHandle = []
		self.List_ItemMenuType = []
		self.List_RemoveBarMenu = []		
		self.List_RemovePopMenuItem = []

	def setMenuBar(self,hwnd): 		#添加菜单栏到指定hwnd窗口  func: setMenuBar(hwnd)
			self.hWnd = hwnd
			self.ret = SetMenu(hwnd,self.hMenu)
			
	def addBarPopMenu(self,list_menu):  #菜单栏菜单项名称list  例如： a = ["文件","编辑"]    addBarPopMenu(a)
		for name in list_menu:
			self.List_BarMenuName.append(name)
			self.List_BarMenuHandle.append(CreateMenu())#由系统生成菜单句柄
			self.List_BarMenuType.append(MF_POPUP)
			AppendMenu(self.hMenu, MF_POPUP, self.List_BarMenuHandle[-1],self.List_BarMenuName[-1])	#按list下标添加菜单栏子项到菜单栏
			
	def insertBarMenu(self,name,pos = -1,type = MF_POPUP): #菜单栏插入菜单 pos位置（默认追加） type菜单类型
			hMenu = CreateMenu()
			if pos == -1:
				self.List_BarMenuName.append(name)			
				self.List_BarMenuHandle.append(hMenu)
				self.List_BarMenuType.append(type)
			else:
				self.List_BarMenuName.insert(pos,name)			
				self.List_BarMenuHandle.insert(pos,hMenu)
				self.List_BarMenuType.insert(pos,type)
				
			InsertMenu(self.hMenu,pos,MF_BYPOSITION | type,hMenu,name)
			
	#MF_DISABLED MF_ENABLED MF_GRAYED
	def	setBarMenuState(self,pos,state):
		EnableMenuItem(self.hMenu,self.List_BarMenuHandle[pos],state)
		
	def setBarMenuFun(self,Menu,func):
		if isinstance(Menu,str):
			if Menu in self.List_BarMenuName:
				pos = self.List_BarMenuName.index(Menu)
				
		elif isinstance(Menu,int):	
			pos = Menu
			
		self.MenuFunc[self.List_BarMenuHandle[pos]] = func
		
	def addPopMenuItem(self,Menu,list):
		if isinstance(Menu,str):
			if Menu in self.List_BarMenuName:
				pos = self.List_BarMenuName.index(Menu)
		elif isinstance(Menu,int):	
			pos = Menu
		
		type = MF_STRING
		for name in list:
			if name == "SEPARATOR" :
				self.List_ItemMenuName.append("")
				self.List_ItemMenuHandle.append(0)	
				self.List_ItemMenuType.append(MF_SEPARATOR)	
				type = MF_SEPARATOR
			else:
				self.List_ItemMenuName.append(name)
				self.List_ItemMenuHandle.append(CreateMenu())	#由系统生成菜单句柄
				self.List_ItemMenuType.append(type)	
			AppendMenu(self.List_BarMenuHandle[pos], type, self.List_ItemMenuHandle[-1],self.List_ItemMenuName[-1])	#按list下标添加菜单栏子项到菜单栏		

	def insertPopMenuItem(self,Menu,name,pos = -1,type = MF_STRING):	
		if isinstance(Menu,str):
			if Menu in self.List_BarMenuName:
				ItemMenupos = self.List_BarMenuName.index(Menu)
		elif isinstance(Menu,int):	
			ItemMenupos = Menu
	
		if pos == -1:
			if type == MF_SEPARATOR:
				hMenu = 0
			else:
				hMenu = CreateMenu()
	
			self.List_ItemMenuName.append(name)			
			self.List_ItemMenuHandle.append(hMenu)
			self.List_ItemMenuType.append(type)	
			
		else:
			if type == MF_SEPARATOR:
				hMenu = 0
			else:
				hMenu = CreateMenu()

			self.List_ItemMenuName.insert(pos,name)			
			self.List_ItemMenuHandle.insert(pos,hMenu)
			self.List_ItemMenuType.insert(pos,type)	
				
		InsertMenu(self.List_BarMenuHandle[ItemMenupos],pos,MF_BYPOSITION | type,hMenu,name)		
	
	def setPopMenuItemFun(self,Menu,func):
		if isinstance(Menu,str):
			if Menu in self.List_ItemMenuName:
				pos = self.List_ItemMenuName.index(Menu)
				
		elif isinstance(Menu,int):	
			pos = Menu
			
		self.MenuFunc[self.List_ItemMenuHandle[pos]] = func

	
	def removeBarMenu(self,barpos):	
		nBar = self.List_BarMenuName.pop(barpos)
		hBar = self.List_BarMenuHandle.pop(barpos)
		type = self.List_BarMenuType.pop(barpos)	
		self.List_RemoveBarMenu.append( {"nBarMenu":nBar,"hBarMenu":hBar,"pos":barpos,"type":type } )
		RemoveMenu(self.hMenu,barpos,MF_BYPOSITION)
	
	def removePopMenuItem(self,barpos,itempos):
		nBar = self.List_BarMenuName[barpos]
		hBar = self.List_BarMenuHandle[barpos]
		nItem =	self.List_ItemMenuName.pop(itempos)
		hItem =	self.List_ItemMenuHandle.pop(itempos)
		type = self.List_ItemMenuType.pop(itempos)	
		self.List_RemovePopMenuItem.append( {	"nBarMenu":nBar,
												"hBarMenu":hBar,
												"nItemMenu":nItem,
												"hItemMenu":hItem,
												"barpos":barpos,
												"itempos":itempos,
												"type":type
		})
								
		RemoveMenu(hBar,itempos,MF_BYPOSITION)

		
	def restoreMenu(self):
		for BarMenu in self.List_RemoveBarMenu:
			InsertMenu(self.hMenu,BarMenu["pos"],MF_BYPOSITION | BarMenu["type"],BarMenu["hBarMenu"],BarMenu["nBarMenu"])
		
		for MenuItem in self.List_RemovePopMenuItem:
			InsertMenu(MenuItem["hBarMenu"],MenuItem["itempos"],MF_BYPOSITION | MenuItem["type"],MenuItem["hItemMenu"],MenuItem["nItemMenu"])		
		
	def DestroyMenu(self):
		for MenuItem in self.List_RemovePopMenuItem:
			DestroyMenu(MenuItem["hItemMenu"])
			
		for BarMenu in self.List_RemoveBarMenu:
			DestroyMenu(BarMenu["hBarMenu"])
			
		
		


#Create a List-View Control
ListViewError = None
ListViewControlId = []

def CreateListView( hwndParent,
					name = "",
					x=0,
					y=0,
					width = CW_USEDEFAULT,
					height =CW_USEDEFAULT,
					style = WS_CHILD | WS_BORDER | WS_HSCROLL | WS_VSCROLL | WS_VISIBLE | LVS_REPORT | LVS_EDITLABELS,
					id = 100,
					g_hInst = win32.kernel32.GetModuleHandleW(0),
					margin = 3
					):
					
	if id in ListViewControlId:
		ListViewID = ListViewControlId[-1] + 1 
	else:
		ListViewID = id
		
	ListViewControlId.append(ListViewID)		
		
	icex = INITCOMMONCONTROLSEX()
	icex.dwICC = ICC_LISTVIEW_CLASSES
	icex.dwSize = sizeof(icex)
			
	rcClient = 	RECT()	
	GetClientRect(hwndParent,rcClient)
	
	bInit = InitCommonControlsEx(getpointer(icex))
		
	if (width ==0 and height ==0):
		width =	rcClient.right - rcClient.left
		height = rcClient.bottom - rcClient.top
				
	if isinstance(name,str):
		cwListView = CWindowExW()
		WC_LISTVIEW = LPWSTR(WC_LISTVIEWW)
		tname = LPWSTR(name)
	
	else:
		cwListView = CWindowExA()
		WC_LISTVIEW = LPSTR(WC_LISTVIEWA)
		tname = LPSTR(name)

		
	cwListView.dwExStyle    = 0
	cwListView.lpClassName  = WC_LISTVIEW
	cwListView.lpWindowName = tname
	cwListView.dwStyle = style
	cwListView.x = margin
	cwListView.y = margin
	cwListView.nWidth     = width - margin*2
	cwListView.nHeight    = height - margin*2
	cwListView.hWndParent = hwndParent
	cwListView.hMenu 	  = HMENU(ListViewID)
	cwListView.hInstance  = g_hInst	
	cwListView.lpParam 	  = NULL
		
	hWndListView = CreateWindow(cwListView); 
	
	LastError = GetLastError()
	
	tagName = "ListView%d"%ListViewID
	
	LVAllHandle[tagName] = hWndListView  #可注释
		
	return hWndListView;

#返回列号 0 开始	
def InsertListViewColumns(	hWndListView,pszText,iCol,
							mask = LVCF_FMT | LVCF_WIDTH | LVCF_TEXT | LVCF_SUBITEM ,
							align = LVCFMT_LEFT,
							width = 300,
							iSubItem = 0,
							iImage = 0,
							iOrder = 0
						 ):
	if isinstance(pszText,str):
		LVCOLUMN = LVCOLUMNW()
		ListView_InsertColumn = ListView_InsertColumnW
		LVCOLUMN.pszText = LPWSTR(pszText)
	else: 
		LVCOLUMN = LVCOLUMNA()
		ListView_InsertColumn = ListView_InsertColumnA
		LVCOLUMN.pszText = LPSTR(pszText)
	
	LVCOLUMN.mask = mask
	LVCOLUMN.fmt = align
	LVCOLUMN.cx = width
	LVCOLUMN.iSubItem = iSubItem
	LVCOLUMN.iImage = iImage
	LVCOLUMN.iOrder = iOrder

	numCol = ListView_InsertColumn(hWndListView,iCol,LVCOLUMN)
	if numCol== -1:
		return False
	return numCol
	
def ListViewSetExtendedListViewStyle(hWndListView,style):
	return ListView_SetExtendedListViewStyle(hWndListView,style)

	
#返回行子项号 0 开始		
def InsertListViewItems(hWndListView,list,nuItem,
						mask = LVIF_TEXT | LVIF_IMAGE |LVIF_STATE,
						stateMask = 0,
						iSubItem = 0,
						state = 0,
						iImage = 0
						):
						
	if len(list) != 0 :
		if isinstance(list[0],str):
			LVITEM = LVITEMW()
		else:
			LVITEM = LVITEMA()	
		
	LVITEM.mask= mask
	LVITEM.stateMask= stateMask
	LVITEM.state=state	
	LVITEM.iItem  = nuItem
	LVITEM.iImage = iImage
	LVITEM.iSubItem= iSubItem
	LVITEM.cchTextMax = 256
		
	for subText in list:	
		LVITEM.pszText= subText
		
		if LVITEM.iSubItem == 0:
			numItem = ListView_InsertItem(hWndListView, LVITEM)
		else:
			ListView_SetItem(hWndListView, LVITEM)

		LVITEM.iSubItem +=1
		
	if numItem == -1:
		return False	
	return numItem		
	
def ListViewSetItemText(hwnd,row,col,pszText):
	return ListView_SetItemText(hwnd,row,col,pszText)
	
class ListView:
	def __init__(self):
		self.hwnd = None
		self.hListView = None
		self.List_iSubItem = 0
		self.fixedSize = False
	
	def createListView(self,hwnd):
		self.hwnd = hwnd
		self.hListView = CreateListView(hwnd)
		self.WNDRECT = RECT()	
		
		if self.hListView:
			GetClientRect(hwnd,self.WNDRECT) 	#窗口客户区大小
			MoveWindow(self.hListView,
						self.WNDRECT.left+3,
						self.WNDRECT.top,
						self.WNDRECT.right-6,
						self.WNDRECT.bottom-3,
						True) 			#设置ListView大小，位置
						
			ListViewSetExtendedListViewStyle(self.hListView,
											LVS_EX_GRIDLINES 
											| LVS_EX_FULLROWSELECT
											| LVS_EX_HEADERDRAGDROP)
				
	def insertColumns(self,name,count,width):		
		InsertListViewColumns(self.hListView,name,count,width = width)

	def insertItems(self,list,num):
		InsertListViewItems(self.hListView,list,num)

	def setItemText(self,row,col,pszText):
		ListViewSetItemText(self.hListView,row,col,pszText)
					
	def setSize(self,x,y,width,height):	
		if self.fixedSize != True:
			MoveWindow( self.hListView,
						x,
						y,
						width,
						height,
						True) 			#设置ListView大小，位置							

						
						
						
						
						
#---------------------------------------------					
# windows funtion define	

def printSTARTUPINFO(STARTUPINFO):
	info = {}
	info['cb'] = STARTUPINFO.cb
	info['lpReserved'] = STARTUPINFO.lpReserved
	info['lpDesktop'] = STARTUPINFO.lpDesktop
	info['lpTitle'] = STARTUPINFO.lpTitle
	info['dwX'] = STARTUPINFO.dwX
	info['dwY'] = STARTUPINFO.dwY
	info['dwXSize'] = STARTUPINFO.dwXSize
	info['dwYSize'] = STARTUPINFO.dwYSize
	info['dwXCountChars'] = STARTUPINFO.dwXCountChars
	info['dwYCountChars'] = STARTUPINFO.dwYCountChars
	info['dwFillAttribute'] = STARTUPINFO.dwFillAttribute
	info['dwFlags'] = STARTUPINFO.dwFlags
	info['wShowWindow'] = STARTUPINFO.wShowWindow
	info['cbReserved2'] = STARTUPINFO.cbReserved2
	info['lpReserved2'] = STARTUPINFO.lpReserved2
	info['hStdInput'] = STARTUPINFO.hStdInput
	info['hStdOutput'] = STARTUPINFO.hStdOutput
	info['hStdError'] = STARTUPINFO.hStdError
	
	print("STARTUPINFO:")
	for (k,v) in info.items():
		print('\t%-20s'%k,'\t',v)

#retrun StartupInfo*
def GetStartupInfo(StartupInfo):
	if isinstance(StartupInfo,StartupInfoA):
		pStartupInfo = getpointer(StartupInfo)			
		kernel32.GetStartupInfoA(pStartupInfo)
		return pStartupInfo
		
	if isinstance(StartupInfo,StartupInfoW):	
		pStartupInfo = getpointer(StartupInfo)		
		kernel32.GetStartupInfoW(pStartupInfo)					
						
						

	
# WinMain	Param class
class WinMainParam:				
	def Param(self):
		self.hInstance = win32.kernel32.GetModuleHandleA(0)		
		self.lpCmdLine = win32.kernel32.GetCommandLineA()
		return self
	
	def wParam(self):
		self.hInstance = win32.kernel32.GetModuleHandleW(0)				
		self.lpCmdLine = win32.kernel32.GetCommandLineW()	
		return self

#CALLBACK		
CWndProc = CWINFUNC(LRESULT,HWND,UINT,WPARAM,LPARAM)
#用作传参
class wndargs:
	_fields_ = [
			("hwnd",HWND),
			("message",UINT),
			("wParam",WPARAM),
			("lParam",LPARAM)
			]

def WndProcArgs(hwnd,message,wParam,lParam):

	WndProcArgs = wndargs()
	
	WndProcArgs.hwnd = hwnd
	WndProcArgs.message = message	
	WndProcArgs.wParam = wParam	
	WndProcArgs.lParam = lParam
	
	return WndProcArgs


	
	
#消息机制回调函数
ShowMessage = 0
Msg_recive = {}
def _WndProc(hwnd,message,wParam,lParam):
	if ShowMessage == 1:
		print("hwnd: %d, message: %d, wParam: %d, lParam: %d"%(hwnd,message,wParam,lParam))
	Msg_recive["hwnd"]=hwnd
	Msg_recive["message"]=message
	Msg_recive["wParam"]=wParam
	Msg_recive["lParam"]=lParam
	if message in funcMsgCall:
		funcMsgCall[message](Msg_recive)
		LastError = GetLastError()
		return 0	
		
	else:		
		return DefWindowProcA(hwnd,message,wParam,lParam)	
			
#消息机制回调函数	宽字符		
def _wWndProc(hwnd,message,wParam,lParam):	
	if ShowMessage == 1:
		print("hwnd: %d, message: %d, wParam: %d, lParam: %d"%(hwnd,message,wParam,lParam))
	Msg_recive["hwnd"]=hwnd
	Msg_recive["message"]=message
	Msg_recive["wParam"]=wParam
	Msg_recive["lParam"]=lParam
	if message in funcMsgCall:
		funcMsgCall[message](Msg_recive)
		LastError = GetLastError()
		return 0
		
	else:		
		return DefWindowProcW(hwnd,message,wParam,lParam)	

def setWndProc(WndProc):	
	funWndProc = CWndProc(WndProc)
	pWndProc = tofuncp(funWndProc,HANDLE)
	return pWndProc
	
#消息
#funPAINT	
PS = PAINTSTRUCT()
pPS = getpointer(PS)	
def funPAINT(args):
	hdc = BeginPaint(args["hwnd"],pPS)
	EndPaint(args["hwnd"],pPS)	

def funDESTROY(args):
	PostQuitMessage(0)
	
funcMsgCall[WM_PAINT] = funPAINT
funcMsgCall[WM_DESTROY] = funDESTROY
	
#main
def WinMain(ClassName = u'pywnd',WndName = u'pywin',wclsStyle = CS_HREDRAW | CS_VREDRAW ,bkColor = 15 ):
	
	wCharFlag = isinstance(ClassName,str)

	if wCharFlag:
		ClassName = LPCWSTR(ClassName)
		WndName = LPCWSTR(WndName)
		MainParam = WinMainParam().wParam()
		wndcx = WNDCLASSEXW()	
		wndcx.cbSize = sizeof(WNDCLASSEXW)	
		wndcx.hIcon = LoadIconW(NULL,IDI_APPLICATION)
		wndcx.hCursor = LoadCursorW(NULL,IDC_ARROW)
		wndcx.hIconSm = LoadIconW(NULL,IDI_APPLICATION)	
		wndcx.lpfnWndProc = setWndProc(_wWndProc)
	else:
		ClassName = LPCSTR(ClassName)
		WndName = LPCSTR(WndName)	
		MainParam = WinMainParam().Param()
		wndcx = WNDCLASSEXA()	
		wndcx.cbSize = sizeof(WNDCLASSEXA)
		wndcx.hIcon = LoadIconA(NULL,IDI_APPLICATION)
		wndcx.hCursor = LoadCursorA(NULL,IDC_ARROW)
		wndcx.hIconSm = LoadIconA(NULL,IDI_APPLICATION)	
		wndcx.lpfnWndProc = setWndProc(_WndProc)

	wndcx.style = wclsStyle
	wndcx.cbClsExtra = 0
	wndcx.cbWndExtra = 0
	wndcx.hInstance = MainParam.hInstance

	wndcx.hbrBackground = GetSysColorBrush(bkColor)
	wndcx.lpszMenuName = NULL
	wndcx.lpszClassName = ClassName
	
	if wCharFlag:
		regClass = RegisterClassExW(getpointer(wndcx))
	else:
		regClass = RegisterClassExA(getpointer(wndcx))		
	
	LastError = GetLastError()
	
	if regClass == 0:
		LastError = GetLastError()
	
	if wCharFlag:	
		cwndex = CWindowExW()
	else:
		cwndex = CWindowExA()
		
	cwndex.dwExStyle = WS_EX_ACCEPTFILES
	cwndex.lpClassName = ClassName
	cwndex.lpWindowName = WndName
	cwndex.dwStyle = WS_OVERLAPPEDWINDOW
	cwndex.x = CW_USEDEFAULT
	cwndex.y = CW_USEDEFAULT
	cwndex.nWidth = CW_USEDEFAULT
	cwndex.nHeight = CW_USEDEFAULT
	cwndex.hWndParent = NULL
	cwndex.hMenu = NULL
	cwndex.hInstance = MainParam.hInstance
	cwndex.lpParam = NULL

	hwnd = CreateWindow(cwndex)

	if hwnd == NULL:
		LastError = GetLastError()

	else:
		
		ShowWindow(hwnd,SW_SHOWDEFAULT)	
		UpdateWindow(hwnd)		
					
		cMSG = MSG()
		pMSG = getpointer(cMSG)
		
		if wCharFlag:			
			while user32.GetMessageW(pMSG,NULL,0,0):			
				TranslateMessage(pMSG)
				user32.DispatchMessageW(pMSG)
		else:				
			while user32.GetMessageA(pMSG,NULL,0,0):			
				TranslateMessage(pMSG)
				user32.DispatchMessageA(pMSG)				
	
		return cMSG.wParam 
		
#main开始			
if __name__ =="__main__":
	WinMain()












