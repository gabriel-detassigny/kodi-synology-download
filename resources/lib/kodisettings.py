class Configuration:
    def __init__(self, addon):
        self.addon = addon

    def get_user(self):
        return self.addon.getSetting('user')

    def get_password(self):
        return self.addon.getSetting('password')

    def get_url(self):
        return self.addon.getSetting('protocol') + '://' + self.addon.getSetting('ip_address') + ':' + self.addon.getSetting('port')
