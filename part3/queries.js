/*
3. Write MongoDB queries to query your collections (3 marks).
Your queries should show:
*/


//show All documents in the collection;
use assignment;

show collections;

db.Pokemon.find({}).pretty(); //shows all of the flat file data
db.characters.find({}).pretty(); //shows all of the data in a one:few collection I made
db.poketypes.find({}).pretty(); //shows all data in a one:many collections I made using python
db.generations.find({}).pretty(); // shows all data in a one:squillions collection

//show embedded array data,
db.poketypes.find({type:'grass'},{'pokemon.name':1}).pretty(); // returns all the grass type pokemons names
db.generations.find({generation:1},{'pokemon.name':1}).pretty(); // returns all gen 1 pokemon


//show based on selected criteria
db.generations.find({$or:[{generation:1},{generation:2}]}).pretty();// returns all gen 1 or gen 2 pokemon
db.poketypes.find({$or:[{type:"water"},{type:"ice"}]}).pretty();// returns all pokemon who are water and ice type
db.characters.find({"attributes.total":{$gt:750}}).pretty(); //returns the most powerful pokemon
db.characters.find({legendary:"True",generation:1}).pretty(); //returns all legendary, generation 1 pokemon


//show projection;
db.characters.find({legendary:"True",generation:2},{_id:0,name:1,types:1}).pretty(); //returns all gen 2 legendary pokemon, but only their name and type
db.poketypes.find({$or:[{type:"grass"},{type:"fire"}, {type:"water"}]}, {_id:0, "pokemon.number":0}).pretty(); // returns all grass, fire and water pokemon


//show sorted output
db.characters.find({legendary:"True",generation:1}, {_id:0,name:1}).sort({"name":1});  // sorts all gen 1 legends by name
db.characters.find({"attributes.total":{$gt:500}}).sort({name:-1}); // sorts all pokemon who are more powerful than 500 in reverse orde by name
db.characters.find({"attributes.total":{$lt:250}},{_id:0,name:1,"attributes.total":1}).sort({"attributes.total":1}); // sorts the weakest pokemon by total power. from weakest to strongest


//show aggregation.
//counts the number of pokemon per generation
db.characters.aggregate({
 	$group: {
 	  	_id: "$generation",
 	  	total: {$sum : 1}
 	}
});

//counts the number of legendary pokemon
db.characters.aggregate({
 	$group: {
 	  	_id: "$legendary",
 	  	total: {$sum : 1}
 	}
});


//groups all the pokemon by type
db.poketypes.aggregate({
 	$group: {
 	  	_id: "$type",
 	  	total: {$sum : 1}
 	}
});

//strongest pokemon in each generation
db.generations.aggregate([
       {$unwind: '$pokemon' },
       {$group: { _id: { name : "$pokemon.name", generation: "$generation" },
     strongest:{$max:"$pokemon.power"}
                }
       }]);
