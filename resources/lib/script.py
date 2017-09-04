# -*- coding: utf-8 -*-

from resources.lib import kodiutils
from resources.lib import kodilogging
from resources.lib import communicator
from resources.lib import kodisettings
from resources.lib import kodigui
import logging
import xbmcaddon
import xbmcgui
import requests

ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))

def run():
    addon_name = ADDON.getAddonInfo('name')
    config = kodisettings.Configuration(ADDON)
    comm = communicator.Communicator(config)

    try:
        comm.authenticate()
    except requests.exceptions.HTTPError:
        msg = "Error! Could not connect to Synology\n"
        msg += "Please verify your connection settings are correctly set.\n"
        xbmcgui.Dialog().ok(addon_name, msg)
    else:
        if comm.authenticated:
            taskList = comm.get_dl_task_list()
            window = kodigui.TaskListWindow()
            window.add_headers()
            window.add_tasks(taskList['tasks'])
            window.doModal()
        else:
            msg = "Error! Authentication failed\n"
            msg += "Please verify your username/password in your settings"
            xbmcgui.Dialog().ok(addon_name, msg)
