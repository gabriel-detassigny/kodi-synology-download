import requests

class Communicator:
    def __init__(self, configuration):
        self.configuration = configuration
        self.api_infos = None
        self.cookies = {}
        self.authenticated = False

    def __del__(self):
        if self.authenticated:
            self.logout()

    def get_dl_task_list(self):
        if self.authenticated is False:
            self.authenticate()
        url = self.__get_base_api_url() + self.api_infos['SYNO.DownloadStation.Task']['path']
        payload = {
            'api': 'SYNO.DownloadStation.Task',
            'version': self.api_infos['SYNO.DownloadStation.Task']['maxVersion'],
            'method': 'list'
        }
        response = requests.get(url, params=payload, cookies=self.cookies)
        body = response.json()
        return body['data']

    def load_api_infos(self):
        base_url = self.__get_base_api_url()
        payload = {
            'api': 'SYNO.API.Info',
            'version': '1',
            'method': 'query',
            'query': 'SYNO.API.Auth,SYNO.DownloadStation.Task'
        }
        response = requests.get(base_url + 'query.cgi', params=payload)
        self.__check_response_for_errors(response)
        body = response.json()
        self.api_infos = body['data']

    def authenticate(self):
        if self.api_infos is None:
            self.load_api_infos()
        url = self.__get_base_api_url() + self.api_infos['SYNO.API.Auth']['path']
        payload = {
            'api': 'SYNO.API.Auth',
            'version': self.api_infos['SYNO.API.Auth']['maxVersion'],
            'method': 'login',
            'account': self.configuration.get_user(),
            'passwd': self.configuration.get_password(),
            'session': 'DownloadStation',
            'format': 'cookie'
        }
        response = requests.get(url, params=payload)
        self.__check_response_for_errors(response)
        body = response.json()
        self.authenticated = body['success']
        self.cookies = response.cookies

    def logout(self):
        if self.api_infos is None:
            self.load_api_infos()
        url = self.__get_base_api_url() + self.api_infos['SYNO.API.Auth']['path']
        payload = {
            'api': 'SYNO.API.Auth',
            'version': self.api_infos['SYNO.API.Auth']['maxVersion'],
            'method': 'logout',
            'session': 'DownloadStation'
        }
        requests.get(url, params=payload, cookies=self.cookies)

    def __get_base_api_url(self):
        return self.configuration.get_url() + '/webapi/'

    def __check_response_for_errors(self, response):
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
