import json
dict={"id":100,
      "name":"Justin",
      "campus":"davis",
      "skills":["python","java"]}
#convert dictionaty to json string
json_data=json.dumps(dict,indent=4)
print("Json Payload")
print(json_data)
#Load json from api response
api_response='{"id":"100","name":"Jayanta","campus":"davis","skills":["python"]}'
parsed_data=json.loads(api_response)
print(parsed_data)
print("name:",parsed_data["name"])
print("Skills:", parsed_data["skills"][0])
#Modify
parsed_data["skills"].append("java")
print(parsed_data)
parsed_data["id"]=102
print(parsed_data)
print(json.dumps(parsed_data,indent=4))