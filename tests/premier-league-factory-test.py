from nose import with_setup
from model.premier_league import PremierLeagueFactory
from model.championship import Team

class TestPremierLeagueFactory:
    premier_league = None

    def setup(self):
        if not self.premier_league:
            self.premier_league = PremierLeagueFactory().create('2013-14')

    def team_down(self):
        pass

    def test_teams_count(self):
        assert len(self.premier_league.teams) == 20 

    def test_team_exists(self):
        assert Team('Arsenal') in self.premier_league.teams
    
    def test_team_does_not_exist(self):
        assert Team('Corinthians') not in self.premier_league.teams
    
