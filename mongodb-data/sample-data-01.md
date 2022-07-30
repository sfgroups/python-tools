** Inner join example

https://hevodata.com/learn/mongodb-inner-join/#:~:text=The%20MongoDB%20database%20is%20well,aggregation%20method%20instead%20of%20Join.

```
db.chelsea.insertMany( [
{ "playername": "Thiago Silva", "country": "Brazil" },
{ "playername" : "Anthony Rudiger", "country" : "Germany" },
{ "playername" : "Andreas Christensen", "country" : "Denmark" },
{ "playername" : "Reece James", "country" : "England" },
{ "playername" : "Ben Chilwell", "country" : "England" },
{ "playername" : "Ngolo Kante", "country" : "France" },
{ "playername" : "Jorginho", "country" : "Italy" },
{ "playername" : "Mason Mount", "country" : "England" },
{ "playername" : "Hakim Ziyech", "country" : "Morocco" },
{ "playername" : "Edouard Mendy", "country" : "Senegal" },
{ "playername" : "Romelu Lukaku", "country" : "Belgium" },
{ "playername" : "Mateo Kovacic", "country" : "Croatia" }
]);

db.worldXI.insertMany( [
{ "playername" : "Leonel Messi", "club" : "PSG", "country" : "Argentina" },
{ "playername" : "Cristiano Ronaldo", "club" : "Manchester United", "country" : "Portugal" },
{ "playername" : "Robert Lewandowski", "club" : "Bayern Munich", "country" : "Poland" },
{ "playername" : "Ruben Dias", "club" : "Manchester City", "country" : "Portugal" },
{ "playername" : "Erling Haland", "club" : "Borussia Dortmund", "country" : "Norway" },
{ "playername" : "Kevin De Bruyne", "club" : "Manchester City", "country" : "Belgium" },
{ "playername" : "David Alaba", "club" : "Real Madrid", "country" : "Austria" },
{ "playername" : "Leonardo Bonucci", "club" : "Juventus", "country" : "Italy" },
{ "playername" : "Gianluigi Donnarumma", "club" : "PSG", "country" : "Italy" },
{ "playername" : "Ngolo Kante", "club" : "Chelsea", "country" : "France" },
{ "playername" : "Jorginho", "club" : "Chelsea", "country" : "Italy" }
])

```

Query:

```
[{
 $lookup: {
  from: 'worldXI',
  localField: 'playername',
  foreignField: 'playername',
  as: 'chelseaInWorldXI'
 }
}, {
 $match: {
  chelseaInWorldXI: {
   $ne: []
  }
 }
}]
```

Python:

```
from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb+srv://XXXX/test')
result = client['appdb']['chelsea'].aggregate([
    {
        '$lookup': {
            'from': 'worldXI', 
            'localField': 'playername', 
            'foreignField': 'playername', 
            'as': 'chelseaInWorldXI'
        }
    }, {
        '$match': {
            'chelseaInWorldXI': {
                '$ne': []
            }
        }
    }
])
```