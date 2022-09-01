#######################################################
# Challenge 1: Update the Constructor

class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.age = player_dict['age']
        self.position = player_dict['position']
        self.team = player_dict['team']

    # bonus from solution
    def __repr__(self):
        display = f"Player: {self.name}, {self.age} y/o, pos: {self.position}, team: {self.team}"
        return display

    @classmethod
    def get_team(cls,team_list):
        team_players = []
        for player in team_list:
            team_players.append(cls(player))
        return team_players

#######################################################
# Challenge 2: Create instances using individual player dictionaries
print('----------------- Challenge 2 -----------------')
kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, 
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
}

# Create your Player instances here!
player_jason = Player(jason)
player_kevin = Player(kevin)
player_kyrie = Player(kyrie)

print(player_jason)
print(player_kevin)
print(player_kyrie)


#######################################################
# Challenge 3: Make a list of Player instances from a list of dictionaries
print('----------------- Challenge 3 -----------------')
players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]

new_team = []

for player in players:
    new_team.append(Player(player))

for i in new_team:
    print(i)

#######################################################
# Ninja Bonus
print('----------------- Ninja Bonus -----------------')
test = Player.get_team(players)
print(test)
