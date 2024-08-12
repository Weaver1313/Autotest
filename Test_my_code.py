import requests
import pytest
from Repository.basic import Api


class Test_internal_CommentTask:

    def test_taskComment_front_Create(self, api):
        """
        Наименование тест-кейса
        """
        json_post = {
            "externalId": "0d759f6f-b886-410b-a782-66957d02647b",
            "partner": {
                "partnerBusinessId": "a8490f4d-b1c2-4f23-af3f-22ac6f4ac54d",
                "partnerInn": "7989869691",
                "partnerKpp": "79789798"
            }
        }
        response_post = api.post(url=f'{api.url}/../..', json_body=json_post)
        data = response_post.json()
        requests_id = {
            "key": data['id']
        }

        body = {
            "text": "AQA test",
            "authorId": "4b3969bf-e0e9-43ab-a153-8d751e5f6a4d",
            "attachments": []
        }
        response = api.post(url=f'{api.url}/../../{data['id']}/comments', json_body=body)
        assert response.status_code == 200, f'Received "Bug" status code {response.status_code}. Is not to expected.'

    def test_taskComment_front_Read(self, api):
        """
       Наименование тест-кейса
        """
        json_post = {
            "externalId": "0d759f6f-b886-410b-a782-66957d02647b",
            "partner": {
                "partnerBusinessId": "a8490f4d-b1c2-4f23-af3f-22ac6f4ac54d",
                "partnerInn": "7989869691",
                "partnerKpp": "79789798"
            }
        }
        response_post = api.post(url=f'{api.url}/../..', json_body=json_post)
        data = response_post.json()
        requests_id = {
            "key": data['id']
        }

        body = {
            "text": "AQA test",
            "authorId": "4b3969bf-e0e9-43ab-a153-8d751e5f6a4d",
            "attachments": []
        }
        response_post2 = api.post(url=f'{api.url}/../../{data['id']}/comments', json_body=body)

        query = {
            "userId": "4b3969bf-e0e9-43ab-a153-8d751e5f6a4d"
        }
        response = api.get(url=f'{api.url}/../../{data['id']}/comments', params=query)
        assert response.status_code == 200, f'Received "Bug" status code {response.status_code}. Is not to expected.'

