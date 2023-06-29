import requests
import json
import pandas as pd

token_dict = {'url':'https://login.microsoftonline.com/its.jnj.com/oauth2/token?api-version=1.0',
              'head_obj':{'Content-Type': 'application/x-www-form-urlencoded'},
              'data_obj': {'grant_type': 'client_credentials', 
                           'client_id' : '532d186f-739b-4524-a0c5-87bcbc9117c2',
                           'client_secret' : 'TCi7Q~cPO3lpT.yTi4UCTZ.QPCiS6~9q6TkT_',
                           'resource': 'https://ITS-APP-ISM-IRIS-Dev.jnj.com'
                           }
              }
url = token_dict['url']
head_obj = token_dict['head_obj']
data_obj = token_dict['data_obj']
x = requests.get(url, headers=head_obj, data=data_obj).json()
y = x['access_token']
print ('Access token-'+ y)

url2 = "https://jnj-internal-Development.apigee.net/apg-001-servicenow/v1/now/table/incident?sysparm_query=assignment_group=632dc9f1dbfc2f005f83443039961986^ORassignment_group=fd496678db5f28d06c39158239961949^active=true&sysparm_exclude_reference_link=True&sysparm_display_value=True"
auth_token = y
payload = {}
headers = {
    'Authorization': 'Bearer ' + auth_token
}
response = requests.get(url2, headers=headers, data=payload)
print(response.text)
'''
#save the text file to json format
with open("sample.json", "w") as outfile:
    json.dump(response.text, outfile, indent=4, separators=(". ", " = "))


#used to display json in table format
pd_object = pd.read_json('sample.json', typ='series')
df = pd.DataFrame(pd_object)
print(df)
'''
'''
with open('sample.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
print(data["result"][incident])
'''
