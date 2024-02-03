import json


def df(lst, key):
    result = {i : [] for i in set([i[key] for i in lst])}
    for item in lst:
        num = item[key]
        #del item[key]
        result[num].append(item)
    for k, v in result.items():
        yield k, v


with open ('auchan.jsonl') as f:
    s = f.readlines()
result = [json.loads(i) for i in s]

for k, v in df(result, 'Параметр: Group'):
    print (k)