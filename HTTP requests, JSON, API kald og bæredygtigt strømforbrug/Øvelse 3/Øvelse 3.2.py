import ujson

sampleJson = """{"key1" : "value1", "key2" : "value2"}"""


ujsondata = ujson.loads(sampleJson)
print(ujsondata['key2'])