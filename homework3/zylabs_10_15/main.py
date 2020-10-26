# Joseph Chetta 1640405

class Team:
    def __init__(self, teamname='none', teamwins=0, teamlosses=0):
        self.teamname = teamname
        self.team_wins = teamwins
        self.team_losses = teamlosses

    def get_win_percentage(self):
        percentage = self.team_wins / (self.team_wins + self.team_losses)
        return percentage

    def print_team_results(self):
        percentage = self.get_win_percentage()
        if percentage > .5:
            print('Congratulations, Team {} has a winning average!'.format(self.teamname))
        else:
            print('Team {} has a losing average.'.format(self.teamname))

if __name__ == '__main__':
    teamname = input()
    teamwins = int(input())
    teamlosses = int(input())

    team = Team(teamname, teamwins, teamlosses)
    team.print_team_results()