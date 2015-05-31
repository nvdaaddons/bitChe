# -*- coding: UTF-8 -*-
import appModuleHandler
import controlTypes
import api
import winUser
import windowUtils
import eventHandler
import NVDAObjects.IAccessible
from NVDAObjects.IAccessible.sysListView32 import ListItem
from NVDAObjects.IAccessible import IAccessible

class DetailsPane(IAccessible):

	def event_gainFocus(self):
		# the real list of results
		try:
			childList = NVDAObjects.IAccessible.getNVDAObjectFromEvent(
			windowUtils.findDescendantWindow(api.getForegroundObject().windowHandle, visible=True, className="SysListView32"),
			winUser.OBJID_CLIENT, 0)
			childList.setFocus()
			eventHandler.queueEvent("gainFocus", childList)
		except AttributeError:
			super(DetailsPane, self).event_gainFocus()

class ResultListItem(ListItem):

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
