empty = {}
print(type(empty))
print(empty == dict())
a= dict(one =1 , two=2, three=3)
b= {"one": 1, "two":2, "three": 3}
print(a==b)

print(b['one'])
b['two']=22

b['four']=4
#del b["one"]
#b.pop("three")
#b.popitem()
print(b.keys())
print(b.values())
print(b.items())
print(len(b.keys()))
for value in b.values():
    print(value)

print(b.copy())
print(b.clear())


d ={"CS":[106,107,110], "Math": [50,110]} #dictionary using list

print(d.get("CS"))
print(d.get("PHIL"))
english_classes = d.get("ENGLISH",[])



about_me = {"Name": "sandeep", "Class": "MCA"}
print(about_me["Name"])
print(about_me["Class"])

