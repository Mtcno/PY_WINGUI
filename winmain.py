# -*- coding: utf-8 -*-

import sys
sys.path.append('./wingui')
import wingui




#测试用
#def showarg(args):
#		print("hwnd: %x msg: %x wP: %x lP: %x" %(args["hwnd"],args["message"],args["wParam"],args["lParam"]))
	
#wingui.ShowMessage = 1

def Refresh(args):
	print(Refresh.__name__)
	
#WM_CREATE	
def funCREATE(args):
	#窗口居中
	wingui.Wndtocenter(args["hwnd"])
	#菜单
	wndmenu = wingui.CreateMenuBar()					#菜单类	
	wndmenu.insertBarMenu("文件")						# addBarPopMenu(list) 用列表创建菜单
	wndmenu.insertBarMenu("刷新",type=0)
	wndmenu.insertPopMenuItem('文件',"退出")			#菜单子项
	wndmenu.setMenuBar(args["hwnd"])					#添加到窗口
	#菜单功能	
	wndmenu.setBarMenuFun("刷新",Refresh)				#绑定菜单功能，也可以用序号，由0开始，例如：wndmenu.setBarMenuFun(1,Refresh)
	wndmenu.setPopMenuItemFun('退出',wingui.funDESTROY)	#菜单项名，对应功能
	args["MenuFunc"] = wndmenu.MenuFunc					#wndmenu.MenuFunc[菜单句柄]() 对应功能

	ListViewli = ["名称","网址"]
	ListView = wingui.ListView()
	ListView.createListView(args["hwnd"])
	ListView.insertColumns("序号",0,50)
	ListView.insertColumns("名称",1,400)
	ListView.insertColumns("网址",2,400)

	args["ListView"] = ListView
			
def funCOMMAND(args):
	#菜单触发
	if args["wParam"] in args["MenuFunc"]:
		#菜单功能，菜单句柄 args["wParam"]，菜单字典:{句柄:功能} args["MenuFunc"]  
		args["MenuFunc"][args["wParam"]](args)
	
def funMENUSELECT(args):
	pass


def funMOUSEMOVE(args):	
	pass
	
	
def funSIZE(args):
	width = args["lParam"] & 0xFFFF
	height = args["lParam"] >> 16
	if "ListView" in args:
		args["ListView"].setSize(3,0,width-6,height-3)
	
def funNOTIFY(args):
	pass

#消息机制绑定功能
funcMsgCall = wingui.funcMsgCall
funcMsgCall[wingui.WM_SIZE] = funSIZE
funcMsgCall[wingui.WM_CREATE] = funCREATE	
funcMsgCall[wingui.WM_COMMAND] = funCOMMAND
funcMsgCall[wingui.WM_MOUSEMOVE] = funMOUSEMOVE
funcMsgCall[wingui.WM_MENUSELECT] = funMENUSELECT
funcMsgCall[wingui.WM_NOTIFY] = funNOTIFY
#主函数
Main = wingui.WinMain
Main()



















