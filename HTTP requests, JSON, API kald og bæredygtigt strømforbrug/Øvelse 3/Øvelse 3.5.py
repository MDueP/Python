import ujson

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

ujsondata = ujson.loads(sampleJson)
print(ujsondata['company']['employee']['payble']['salary'])
#forskellen fra før er at, man skal gå ind i hvert navn, som er repræsenteret med :