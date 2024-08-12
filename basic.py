import requests
from loguru import logger


class Api:
    _TIMEOUT = 5
    _HEADERS = {}

    def __init__(self, url: str):
        self.response = None
        self.url = url

    def post(self, url: str, params: dict = None, json_body: dict = None, headers: dict = None):
        """
        Basic POST-request
        :param headers:
        :param url:
        :param params:
        :param json_body:
        :return:
        """
        self.response = requests.post(url=url,
                                      headers=headers,
                                      params=params,
                                      json=json_body,
                                      timeout=self._TIMEOUT)

        logger.info(f'REQUEST PARAMS: {params}')
        logger.info(f'REQUEST BODY: {json_body}')
        logger.info(f'RESPONSE TEXT: {self.response.text}')
        return self.response

    def get(self, url: str, params: dict = None):
        """
        Basic GET-request
        :param url:
        :param params:
        :return:
        """
        self.response = requests.get(url=url,
                                     params=params,
                                     timeout=self._TIMEOUT)

        logger.info(f'REQUEST PARAMS: {params}')
        logger.info(f'RESPONSE TEXT: {self.response.text}')
        return self.response


    def put(self, url: str, params: dict = None, json_body = dict):
        """
        Basic put request
        :param url:
        :param params:
        :param json_body:
        :return:
        """
        self.response = requests.put(url=url,
                                     params=params,
                                     json=json_body,
                                     timeout=self._TIMEOUT)

        logger.info(f'REQUEST PARAMS: {params}')
        logger.info(f'RESPONSE TEXT: {self.response.text}')
        return self.response


    def delete(self, url: str, params: dict = None, json_body: dict = None):
        """
        Basic delete request
        :param url:
        :param params:
        :param json_body:
        :return:
        """
        self.response = requests.delete(url=url,
                                        params=params,
                                        json=json_body,
                                        timeout=self._TIMEOUT)

        logger.info(f'REQUEST PARAMS: {params}')
        logger.info(f'RESPONSE TEXT: {self.response.text}')
        return self.response
