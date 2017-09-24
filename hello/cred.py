import requests
import json

name="Team 016"
url="https://thawing-springs-45718.herokuapp.com/"
members=["Rohak Singhal","Sagar Gupta","Ramanujam Kamaraj"]


#data={"name":name,"url":url,"members":members}

data=(("name",name),("url",url),("members",members))

headers = {'user-agent': 'my-app/0.0.1'}

req=requests.post("http://cis2017-coordinator-demo.herokuapp.com/api/teams",data=json.dumps(data),headers=headers)

print(req)





#curl -d 'name=Team016&url=https://thawing-springs-45718.herokuapp.com/&members=["Rohak Singhal","Sagar Gupta","Ramanujam Kamaraj"]' -X POST http://cis2017-coordinator-demo.herokuapp.com/
#api/teams
