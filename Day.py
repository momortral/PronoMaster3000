import Team

class Day:

    def __init__(self, num):
        self.num = num

    def match(self, team_home, team_ext, result):
        goal_home = result[0]
        goal_ext = result[1]
        #marche pas comme ca :(
        team_home.match(goal_home, goal_ext)
        team_ext.match(goal_ext, goal_home)