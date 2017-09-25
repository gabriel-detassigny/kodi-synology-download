import xbmcgui

class TaskListWindow(xbmcgui.Window):
    X_TITLE = 190
    X_STATUS = 800
    X_PERCENT = 980

    def add_headers(self):
        self.addControl(xbmcgui.ControlLabel(
            x=TaskListWindow.X_TITLE, y=25, width=600, height=50, label='Title'))
        self.addControl(xbmcgui.ControlLabel(
            x=TaskListWindow.X_STATUS, y=25, width=150, height=50, label='Status'))
        self.addControl(xbmcgui.ControlLabel(
            x=TaskListWindow.X_PERCENT, y=25, width=150, height=50, label='Percentage'))

    def add_tasks(self, taskList):
        y = 75
        for task in taskList:
            y += 30
            percent = self.__get_download_percent_label(task)
            self.addControl(xbmcgui.ControlLabel(
                x=TaskListWindow.X_TITLE, y=y, width=600, height=25, label=task['title']))
            self.addControl(xbmcgui.ControlLabel(
                x=TaskListWindow.X_STATUS, y=y, width=150, height=25, label=task['status']))
            self.addControl(xbmcgui.ControlLabel(
                x=TaskListWindow.X_PERCENT, y=y, width=150, height=25, label=percent))

    def __get_download_percent_label(self, task):
        if task['size'] == 0:
            return '0%'
        downloaded = task['additional']['transfer']['size_downloaded']
        percent = 100 * float(downloaded) / float(task['size'])
        return "%.2f" % percent + '%'
