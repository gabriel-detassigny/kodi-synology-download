import xbmcgui

class TaskListWindow(xbmcgui.Window):
    def add_headers(self):
        self.addControl(xbmcgui.ControlLabel(x=190, y=25, width=600, height=50, label='Title'))
        self.addControl(xbmcgui.ControlLabel(x=800, y=25, width=100, height=50, label='Status'))
        self.addControl(xbmcgui.ControlLabel(x=920, y=25, width=150, height=50, label='Percentage'));

    def add_tasks(self, taskList):
        y = 75
        for task in taskList:
            y += 30
            self.addControl(xbmcgui.ControlLabel(x=190, y=y, width=600, height=25, label=task['title']))
            self.addControl(xbmcgui.ControlLabel(x=800, y=y, width=100, height=25, label=task['status']))
            percent = self.__get_download_percent_label(task)
            self.addControl(xbmcgui.ControlLabel(x=920, y=y, width=150, height=25, label=percent))

    def __get_download_percent_label(self, task):
        if task['size'] == 0:
            return '0%'
        downloaded = task['additional']['transfer']['size_downloaded']
        percent = 100 * float(downloaded) / float(task['size'])
        return "%.2f" % percent + '%'
