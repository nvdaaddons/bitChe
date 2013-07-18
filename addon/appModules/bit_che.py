# -*- coding: UTF-8 -*-
import appModuleHandler
import controlTypes
import api
import winUser
from NVDAObjects.IAccessible.sysListView32 import List, ListItem

class ResultsList(List):

	def event_gainFocus(self):
		# the real list of results
		childList=self.children[0]
		# adjust the object properties
		self.name=childList.name
		self.role=childList.role
		self.children=childList
		# move the focus on the real list
		childList.setFocus()

class ResultListItem(ListItem):

	def event_gainFocus(self):
		super(ResultListItem, self).event_gainFocus()

	def script_contextMenu(self, gesture):
		api.moveMouseToNVDAObject(self)
		api.setMouseObject(self)
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTDOWN,0,0,None,None)
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTUP,0,0,None,None)

	__gestures = {
		"kb:applications": "contextMenu",
	}

class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.windowClassName == 'ThunderRT6UserControl' and len(obj.children) > 0 and obj.children[0].role == controlTypes.ROLE_LIST:
			clsList.insert(0, ResultsList)
		if not isinstance(obj, ListItem) and obj.role == controlTypes.ROLE_LISTITEM:
			clsList.insert(0, ResultListItem)
