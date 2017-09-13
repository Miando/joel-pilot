from collections import defaultdict
#
a={"category":"merc", "subcategory": "320"}
b={"category":"merc", "subcategory": "600"}
c={"category":"Tesla", "subcategory": "model C"}
d={"category":"Tesla", "subcategory": "model X"}
e={"category":"merc", "subcategory": "v12"}
# a=["merc", "320"]
# b=["merc", "600"]
# c=["Tesla", "model C"]
# d=["Tesla", "model X"]
l=[a,b,c,d,e]

d = defaultdict(list)
for s in l:
    for k, v in s.items():
        if s['subcategory'] not in d[s['category']]:
            d[s['category']].append(s['subcategory'])
print (dict(d))
