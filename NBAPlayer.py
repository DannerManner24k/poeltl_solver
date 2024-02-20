class NBAPlayer:
    def __init__(self, player, playerId, team, teamId, conference, division, age, position, jersey, height, teams):
        self.player = player
        self.playerId = playerId
        self.team = team
        self.teamId = teamId
        self.conference = conference
        self.division = division
        self.age = age
        self.position = position
        self.jersey = jersey
        self.height = height
        self.teams = teams
    
    def __str__(self):
        return f"player = {self.player},\nplayerId = {self.playerId},\nteam = {self.team},\nteamId = {self.teamId},\nconference = {self.conference},\ndivision = {self.division},\nage = {self.age},\nposition = {self.position},\njersey = {self.jersey},\nheight = {self.height},\nteams = {self.teams}"
    
    