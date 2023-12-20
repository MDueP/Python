import ujson
#vi får at vide det er en array, hvilket betyder en liste eller tuple. Man kan også se det ved [] der er i starten og slutningen
sampleJson = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""


dataliste = []
#Vi tager vores array og putter ind i en liste, som vi kalder dataliste
dataliste = ujson.loads(sampleJson)
# vi laver en item get, for at få de values fra keys med navnet name i den liste vi har loadet arrayen ind i
datalisteoutput = [item.get('name') for item in dataliste]

print(datalisteoutput)