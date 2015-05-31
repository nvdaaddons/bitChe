# -*- coding: UTF-8 -*-
import appModuleHandler
import controlTypes
import api
import winUser
from NVDAObjects.IAccessible.sysListView32 import List, ListItem
from NVDAObjects.IAccessible import IAccessible

class DetailsPane(IAccessible):

	def event_gainFocus(self):
		# the real list of results
		try:
			childList = self.simpleFirstChild
		except AttributeError:
			childList = None
			return
		if isinstance(childList, List):
			childList.setFocus()

	def script_contextMenu(self, gesture):
		api.moveMouseToNVDAObject(self)
		api.setMouseObject(self)
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTDOWN,0,0,None,None)
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTUP,0,0,None,None)

	__gestures = {
		"kb:applications": "contextMenu",
		"kb:shift+F10": "contextMenu",
	}

class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.role == controlTypes.ROLE_PANE:
			clsList.insert(0, DetailsPane)
		if not isinstance(obj, ListItem) and obj.role == controlTypes.ROLE_LISTITEM:
			clsList.insert(0, ResultListItem)
