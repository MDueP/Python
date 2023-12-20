import ujson

data = {"key1" : "value1", "key2" : "value2"}


ujsondata = ujson.dumps(data)
print(ujsondata)