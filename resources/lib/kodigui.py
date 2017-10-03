import xbmcgui

class Sizes:
    X_TITLE = 100
    X_STATUS = 700
    X_PERCENT = 840

    Y_HEADER = 25
    Y_HEADER_MARGIN = 75
    Y_TASK_MARGIN = 35

    WIDTH_TITLE = 600
    WIDTH_STATUS = 180
    WIDTH_PERCENT = 150

    HEIGHT_HEADER = 50
    HEIGHT_TASK = 25

class TaskListWindow(xbmcgui.Window):

    def add_headers(self):
        self.addControl(xbmcgui.ControlLabel(
            x=Sizes.X_TITLE, y=Sizes.Y_HEADER, width=Sizes.WIDTH_TITLE, height=Sizes.HEIGHT_HEADER, label='Title'))
        self.addControl(xbmcgui.ControlLabel(
            x=Sizes.X_STATUS, y=Sizes.Y_HEADER, width=Sizes.WIDTH_STATUS, height=Sizes.HEIGHT_HEADER, label='Status'))
        self.addControl(xbmcgui.ControlLabel(
            x=Sizes.X_PERCENT, y=Sizes.Y_HEADER, width=Sizes.WIDTH_PERCENT, height=Sizes.HEIGHT_HEADER, label='Percentage'))

    def add_tasks(self, taskList):
        y = Sizes.Y_HEADER_MARGIN
        for task in taskList:
            y += Sizes.Y_TASK_MARGIN
            self.__add_task(task, y)

    def __add_task(self, task, y):
        percent = self.__get_download_percent_label(task)
        self.addControl(xbmcgui.ControlLabel(
            x=Sizes.X_TITLE, y=y, width=Sizes.WIDTH_TITLE, height=Sizes.HEIGHT_TASK, label=task['title']))
        self.addControl(xbmcgui.ControlLabel(
            x=Sizes.X_STATUS, y=y, width=Sizes.WIDTH_STATUS, height=Sizes.HEIGHT_TASK, label=task['status']))
        self.addControl(xbmcgui.ControlLabel(
            x=Sizes.X_PERCENT, y=y, width=Sizes.WIDTH_PERCENT, height=Sizes.HEIGHT_TASK, label=percent))

    def __get_download_percent_label(self, task):
        if task['size'] == 0:
            return '0%'
        downloaded = task['additional']['transfer']['size_downloaded']
        percent = 100 * float(downloaded) / float(task['size'])
        return "%.2f" % percent + '%'
