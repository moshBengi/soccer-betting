import pandas as pd
import time
FILE_NAME = "betting.csv"


class Bet:  # class for the bet of every person

    def __init__(self, first_team, second_team, winner, name):
        self.first_team = first_team
        self.second_team = second_team
        self.diff = first_team - second_team
        self.winner = winner
        self.name = name
        self.points = 0

    def __gt__(self, other):
        return other.points < self.points

    # the calculating algorithm, can be changed
    def calculate_grade(self, actual):
        diff_f = abs(self.first_team - actual.first_team) * 5
        diff_s = abs(self.second_team - actual.second_team) * 5
        winner = 0 if self.winner == actual.winner else 19
        diff_diff = abs(self.diff - actual.diff) * 4
        points = 100 - diff_diff - diff_f - diff_s - winner
        self.points = points


if __name__ == '__main__':
    betting = []
    df = pd.read_csv(FILE_NAME)
    first_team_name = df.columns[1]
    second_team_name = df.columns[2]
    for index, row in df.iterrows():
        if row[first_team_name] != row[second_team_name]:
            winner = first_team_name if row[first_team_name] > row[second_team_name] else second_team_name
        else:
            winner = row['winner']
        betting.append(Bet(row[first_team_name], row[second_team_name], winner, row['name']))
    print("GAME IS OVER!")
    time.sleep(2)
    first_score = int(input("how many " + first_team_name + " scored?\n"))
    second_score = int(input("how many " + second_team_name + " scored?\n"))
    if first_score == second_score:
        winner = input("who won? 1 is " + first_team_name + " 2 is " + second_team_name + "\n")
        winner = first_team_name if winner == '1' else second_team_name
    else:
        winner = first_team_name if first_score > second_score else second_team_name
    actual = Bet(first_score, second_score, winner, "actual")

    print("the grades are:")
    time.sleep(2)

    for b in betting:
        b.calculate_grade(actual)

    betting.sort()
    for b in betting:
        print(b.name + " got " + str(b.points) + " points")
        time.sleep(2)

    print("nice job " + betting[-1].name + " you won")
    time.sleep(2)
