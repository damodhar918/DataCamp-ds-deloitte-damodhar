import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'userID': "U1001",   
                            'latitude': "22.139997",   
                            'longitude': "-100.978803",   
                            'smoker': "false",   
                            'drink_level': "abstemious",   
                            'dress_preference': "informal",   
                            'ambience': "family",   
                            'transport': "on foot",   
                            'marital_status': "single",   
                            'hijos': "independent",   
                            'birth_year': "1989",   
                            'interest': "variety",   
                            'personality': "thrifty-protector",   
                            'religion': "none",   
                            'activity': "student",   
                            'color': "black",   
                            'weight': "69",   
                            'budget': "medium",   
                            'height': "1.77",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/ebbb3f32f44f49c98efb65ade024e020/services/49b72de2d1fb4c868158ce6d17e79f01/execute?api-version=2.0&format=swagger'
api_key = '86mUPwJ2o2C8c49Om1W7d4XGkDP2AkSDPiPbyZTznwGWFOEUKYGcCCRL+EUHDBz96iu8ZtMopQga+D0K9MjUlA==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}


req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
