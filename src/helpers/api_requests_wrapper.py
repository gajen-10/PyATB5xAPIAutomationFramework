# It is a pre built method fr the GET, POST, PUT, PATCH, DELETE Request

import json
import requests

def get_request(url, auth):
    response=requests.get(url=url,auth=auth)
    return  response.json()


def post_request(url,auth,headers,payload,in_json):
    post_response=requests.post(url=url, headers=headers,auth=auth,data=json.dumps(payload))
    if in_json == True:
        return post_response.json()
    return post_response

def patch_request(url,auth,headers,payload,in_json):
    patch_response=requests.patch(url=url,headers=headers,auth=auth,data=json.dumps(payload))
    if in_json == True:
        return patch_response.json()
    return patch_response

def put_request(url,auth,headers,payload,in_json):
    put_response=requests.put(url=url,headers=headers,auth=auth,data=json.dumps(payload))
    if in_json == True:
        return put_response.json()
    return put_response