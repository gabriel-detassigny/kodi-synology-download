# -*- coding: utf-8 -*-

from resources.lib import kodiutils
from resources.lib import kodilogging
from resources.lib import communicator
from resources.lib import kodisettings
import logging
import xbmcaddon
import xbmcgui

ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))

def run():
    addon_name = ADDON.getAddonInfo('name')

    config = kodisettings.Configuration(ADDON)
    comm = communicator.Communicator(config)

    taskList = comm.get_dl_task_list()

    xbmcgui.Dialog().ok(addon_name, taskList['tasks'][0]['title'])
