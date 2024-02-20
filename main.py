from Connection import nba_players, client
from PlayerManager import PlayerManager
from Categories import Categories

player_list = nba_players

# Create a PlayerManager object
pm = PlayerManager(player_list)

# Use the getPlayersWithCondition method to find all players with a jersey number less than 10
players_with_jersey_less_than_10 = pm.getPlayersWithCondition('jersey', 'greater than', 90)

# Now players_with_jersey_less_than_10 is a list of all NBAPlayer objects where the jersey number is less than 10
for player in players_with_jersey_less_than_10:
    print(player.player + ': ' + player.jersey.__str__())