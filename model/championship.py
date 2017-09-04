from typing import List
import datetime

class Team:
    def __init__(self, name : str):
        self.__name = name
    
    def __str__(self):
        return self.__name

    def __eq__(self, other):
        return self.name == other.name

    @property
    def name(self):
        return self.__name

class Championship:

    def __init__(self, name : str, season : str, teams : List[Team]):
        self.__name = name
        self.__season = season
        self.__teams = teams
        
    @property
    def teams(self):
        return list(self.__teams)

    def __str__(self):
        return self.__name
    # def get_team_by_name(self, team_name: str):
        # return self.teams_by_name.get(team_name)
        