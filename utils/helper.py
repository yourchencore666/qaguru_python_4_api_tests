import logging
import curlify
from requests import Session
from allure import step
import allure
from allure_commons.types import AttachmentType


def console_logger(function):
    def wrapper(*args, **kwargs):
        response = function(*args, **kwargs)
        curl_log = f'CODE: {response.status_code} {curlify.to_curl(response.request)}'

        logging.info(curl_log)
        if response.json() == {}:
            logging.info(response.json())
        else:
            logging.info(response.text)

        allure.attach(curl_log, 'curl_logs', AttachmentType.TEXT, '.log')
        allure.attach(str(response.json()), 'response_log', AttachmentType.TEXT, '.log')
        return response

    return wrapper


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    @console_logger
    def request(self, method, url, **kwargs):
        with step(f'{method} {url}'):
            response = super().request(method, url=f'{self.base_url}{url}', **kwargs)

            # curl_log = f'CODE: {response.status_code} {curlify.to_curl(response.request)}'
            #
            # logging.info(curl_log)
            # if response.json() == {}:
            #     logging.info(response.json())
            # else:
            #     logging.info(response.text)
            #
            # allure.attach(curl_log, 'curl_logs', AttachmentType.TEXT, '.log')
            # allure.attach(str(response.json()), 'response_log', AttachmentType.TEXT, '.log')

        return response
