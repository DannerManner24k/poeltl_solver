from pymongo import MongoClient
from NBAPlayer import NBAPlayer

client = MongoClient('mongodb://localhost:27017/')
db = client.NBA_Players
collection = db.Player

mongo_players = collection.find()

nba_players = [NBAPlayer(
        player.get('player'), 
        player.get('playerId'), 
        player.get('team'), 
        player.get('teamId'), 
        player.get('conference'), 
        player.get('division'), 
        player.get('age'), 
        player.get('position'), 
        player.get('jersey'), 
        player.get('height'), 
        player.get('teams')) for player in mongo_players]
