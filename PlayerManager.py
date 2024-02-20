from NBAPlayer import NBAPlayer
from Conditions import Conditions
from typing import List

class PlayerManager:
    def __init__(self, players: List[NBAPlayer]):
        self.players = players

    def getPlayer(self, category, search):
        # Use Python's built-in filter function to find matching players
        matching_players = list(filter(lambda player: getattr(player, category) == search, self.players))
        # Convert the filter object to a list and return it
        return list(matching_players)
    
    def getPlayersWithCondition(self, category, condition, search):
        # Get the appropriate comparison function based on the condition
        compare = Conditions.conditions[condition]

        # Use Python's built-in filter function to find matching players
        matching_players = list(filter(lambda player: getattr(player, category) is not None and compare(getattr(player, category), search), self.players))

        # Return the list of matching players
        return matching_players
    