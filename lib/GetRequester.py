import requests
import json

class GetRequester:

    def __init__(self, url):
        url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        self.url = url

    def get_response_body(self):
        response = requests.get(url="https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
        return response.content
        

    def load_json(self):
        json_list = []
        json_list = json.loads(self.get_response_body)
        for json_list in json_list:
            json_list.append()
        return json_list
    

    load_json = json_list.loadjson()
    for list in set (load_json):
        print (json_list)
    