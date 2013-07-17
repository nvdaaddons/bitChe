import appModuleHandler
import controlTypes
import api
#import ui
import winUser

class AppModule(appModuleHandler.AppModule):

	def event_gainFocus(self, obj, nextHandler):
		if obj.windowClassName == 'ThunderRT6UserControl' and len(obj.children) > 0 and obj.children[0].role == controlTypes.ROLE_LIST:
			obj.name = obj.children[0].name
			obj.role = obj.children[0].role
			obj.children[0].setFocus()
		nextHandler()

	def script_contextMenu(self, gesture):
		obj=api.getFocusObject()
		api.moveMouseToNVDAObject(obj)
		api.setMouseObject(obj)
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTDOWN,0,0,None,None)
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTUP,0,0,None,None)

	__gestures = {
		"kb:applications": "contextMenu",
	}
