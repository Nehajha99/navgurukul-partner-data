import requests
import json
import pprint
url=requests.get("http://join.navgurukul.org/api/partners")
data=url.json()
with open("data12.json","w") as f:
    json.dump(data,f,indent=2)
list1=[]
dic1={}
for index1 in data["data"]:
    # print["name"],"--",index1["id"])
    list1.append((index1["name"],index1["id"]))
    dic1.update(list1)    
def sort():
    user=input("what you want assending data or dessending data")
    if user=="a":
        dic2={}
        for index1 in dic1:
            s=dic1[index1]
            for j in dic1:
                a=dic1[j]
                if s>a:
                    dic2[j]=a
        for index1 in dic1:
            s=dic1[index1]
            for j in dic1:
                a=dic1[j]
                if s<a:
                    dic2[j]=a
        for index1 in dic2:
            print(dic2[index1],index1) 
        with open ("data12.json",'w') as j:
            json.dump(dic1,j,indent=2) 
    if user=="d":
        dic3={}
        for i in range(len(dic1)):
            w=0
            for value in dic1:
                if w<dic1[value]:
                    w=dic1[value]
                    key=value        
            dic3.update({key:w})
            dic1.pop(key)
        for h in dic3:
            print(dic3[h],h)
        with open("data12.json","w") as j:
            json.dump(dic3,j,indent=2)    
sort()




