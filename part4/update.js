/*
4. Find out how to update your document and implement an update (2 marks).
*/

db.characters.update({name:"Mewtwo"}, {$set:{strongest:'True'}});
db.characters.find({name:"Mewtwo"}); // setting mewtwo to the stongest pokemon
db.characters.update({name:"Mewtwo"}, {$set:{"types.1.type 2": "Fighting" }} ) // set type 2 to figting
db.characters.update({name:"Mewtwo"}, {$inc:{"attributes.0.total": 100 }} ) // increment the total by 100
