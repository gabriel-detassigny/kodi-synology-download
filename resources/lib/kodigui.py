import xbmcgui

class TaskListWindow(xbmcgui.Window):
    def add_headers(self):
        self.addControl(xbmcgui.ControlLabel(x=190, y=25, width=600, height=50, label='Title'))
        self.addControl(xbmcgui.ControlLabel(x=800, y=25, width=100, height=50, label='Status'))

    def add_tasks(self, taskList):
        y = 75
        for task in taskList:
            y += 30
            self.addControl(xbmcgui.ControlLabel(x=190, y=y, width=600, height=25, label=task['title']))
            self.addControl(xbmcgui.ControlLabel(x=800, y=y, width=200, height=25, label=task['status']))
