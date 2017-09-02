class Configuration:
    def __init__(self, addon):
        self.addon = addon

    def get_user(self):
        return self.addon.getSetting('user')

    def get_password(self):
        return self.addon.getSetting('password')

    def get_url(self):
        url = self.addon.getSetting('protocol') + '://'
        url += self.addon.getSetting('ip_address')
        url += ':' + self.addon.getSetting('port')
        return url
