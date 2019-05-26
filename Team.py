from typing import Any


class Team:

    def __init__(self, name, stadium, coach):
        self._name = name
        self._stadium = stadium
        self.coach = coach
        self.nb_win = 0
        self.nb_draw = 0
        self.nb_loose = 0
        self.tot_points = 0
        self.tot_goals_for = 0
        self.tot_goals_againt = 0
        self.ratio = 0
        self.nb_yellow = 0
        self.nb_red = 0

    def _get_name(self):
        return self._name

    def _set_name(self, name):
        self._name = name

    def _get_stadium(self):
        return self._stadium

    def _set_stadium(self, stadium):
        self._stadium = stadium

    name = property(_get_name, _set_name)
    stadium = property(_get_stadium, _set_stadium)

    def __repr__(self):
        print("{}: coached by {} in {}".format(self.name, self.coach, self.stadium))



    def match(self, goals_for, goals_against):
        result = self.result_match(goals_for, goals_against)
        print("BIIIIIIIM tu t'es fais ken" + str(goals_against))
        #self.tot_points = self.tot_points + self.calcul_points(result)

    def result_match(self, goals_for, goals_against):
        if(goals_for > goals_against):
            result = "V"
        elif(goals_for < goals_against):
            result = "D"
        else:
            result = "N"
        return result

    print("bllalba")