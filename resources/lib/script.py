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
    progress = xbmcgui.DialogProgress()
    progress.create('Synology Download', 'Connecting to Synology...')
    comm = communicator.Communicator(config)

    try:
        comm.load_api_infos()
        progress.update(25, 'Connection established!', 'Authenticating...')
        comm.authenticate()
    except requests.exceptions.HTTPError:
        progress.close()
        msg = "Error! Could not connect to Synology\n"
        msg += "Please verify your connection settings are correctly set.\n"
        xbmcgui.Dialog().ok(addon_name, msg)
    else:
        if comm.authenticated:
            progress.update(50, 'Successfully authenticated!', 'Retrieving download list...')
            taskList = comm.get_dl_task_list()
            progress.update(75, 'Download list retrieved!', 'Preparing UI...')
            window = kodigui.TaskListWindow()
            window.add_headers()
            window.add_tasks(taskList['tasks'])
            progress.close()
            window.doModal()
        else:
            progress.close()
            msg = "Error! Authentication failed\n"
            msg += "Please verify your username/password in your settings"
            xbmcgui.Dialog().ok(addon_name, msg)
