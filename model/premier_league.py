import requests
from model.championship import Championship
from model.championship import Team

class SeasonNotFountException(Exception):
    pass

class PremierLeagueFactory:

    seasons = {
        '2013-14' : 'https://raw.githubusercontent.com/footballcsv/eng-england/master/2010s/2013-14/1-premierleague.csv'
    }

    def create(self, season : str):
        if season not in self.seasons:
            raise SeasonNotFountException("Season not found")

        data_url = self.seasons[season]
        response = requests.get(data_url, stream=True)
        return Championship("Premier League", season, self.extract_teams(response.text))

    # Extract all the teams in the championship
    def extract_teams(self, csv_data: str):
        games_data = csv_data.splitlines()
        teams_names = set([team_name for game_data in self.all_games(games_data) for team_name in self.team_names(game_data)])
        return [Team(team_name) for team_name in teams_names]

    # Return a list with all the games (excluding the csv header)
    def all_games(self, games_data: tuple):
        return games_data[2:]

    ## Return the team names in a game line
    def team_names(self, game_data : str):
        return game_data.split(',')[1:2]