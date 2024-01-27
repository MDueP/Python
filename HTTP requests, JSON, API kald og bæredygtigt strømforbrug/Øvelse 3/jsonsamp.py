import ujson

json_sample = """{"key1":"value1", "key2":[{"key3":"value3"}, {"wow":"something interesting here!"}]"""


ujsondata = ujson.loads(json_sample)

print(ujsondata['key2'][1]['wow'])