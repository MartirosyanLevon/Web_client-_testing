from datetime import datetime
import requests
import json


class SomeResourceClient:
    def __init__(self, url):
        self.url = url

    def __user_get_status(self, user_id):
        resp = requests.get(f'{self.url}/web/user/get-status/{user_id}')
        json_data = json.loads(resp.text)
        return json_data

    def get_user_last_action_time(self, user_id):
        json_data = self.__user_get_status(user_id)
        last_action_time = json_data['lastActionTime']
        time_diff = json_data['timeDiff']
        return datetime.fromtimestamp(last_action_time - time_diff)

if __name__ == '__main__':
    some_resource_client = SomeResourceClient('https://www.avito.ru')
    print(some_resource_client.user_get_status(177061452))
    #print(some_resource_client.get_user_last_action_time(177061452))
