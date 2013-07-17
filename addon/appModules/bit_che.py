# -*- coding: UTF-8 -*-

import appModuleHandler
import controlTypes
import api
#import ui
import winUser
from NVDAObjects.IAccessible.sysListView32 import ListItem

class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.role == controlTypes.ROLE_LISTITEM:
			clsList.insert(0, ResultsItem)

	def event_gainFocus(self, obj, nextHandler):
		if obj.windowClassName == 'ThunderRT6UserControl' and len(obj.children) > 0 and obj.children[0].role == controlTypes.ROLE_LIST:
			obj.name = obj.children[0].name
			obj.role = obj.children[0].role
			obj.children[0].setFocus()
		nextHandler()

class ResultsItem(ListItem):

	def script_contextMenu(self, gesture):
		api.moveMouseToNVDAObject(self)
		api.setMouseObject(self)
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTDOWN,0,0,None,None)
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTUP,0,0,None,None)

	__gestures = {
		"kb:applications": "contextMenu",
	}
