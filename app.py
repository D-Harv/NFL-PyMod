import csv
from Team import Team
from Hashmap import HashTable
from Overwriter import Overwriter


def load_csv_data(filename):  # Define method for loading csv files for scalability
    with open(filename) as file:
        return list(csv.reader(file))


w = input("What week are we looking at? ")

Overwriter.go(w)

CSV_Team = load_csv_data(f"./Week{w}.csv")


# Define method for assigning loaded package data into package object
def load_team_data(team_hash_table):
    for team in CSV_Team:
        ID = int(team[0])
        Name = team[1]
        WR = team[2]
        RB = team[3]

        tm = Team(ID, WR, RB)

        team_hash_table.insert(ID, tm)  # Insert package data into hash table with package ID as key


team_hash = HashTable()

load_team_data(team_hash)

bet1 = [0, 3, 4, 7, 8, 11, 12, 15, 16, 19, 20, 23, 24]
bet2 = [1, 2, 5, 6, 9, 10, 13, 14, 17, 18, 21, 22, 25]


def parse(hash_table, z):

    writer(file1, "Bet on touchdowns from:\n\n")

    if z == 0:
        for id in range(0, len(CSV_Team)):
            team = hash_table.lookup(id)
            if bet1.count(id) != 0:
                if team.id % 2 == 0:
                    writer(file1, team.wr + "\n")
                else:
                    writer(file1, team.rb + "\n")
    else:
        for id in range(0, len(CSV_Team)):
            team = hash_table.lookup(id)
            if bet2.count(id) != 0:
                if team.id % 2 == 0:
                    writer(file1, team.wr + "\n")
                else:
                    writer(file1, team.rb + "\n")


file1 = f"./Bets{w}.txt"


def writer(filename, str):
    file = open(filename, "a")
    file.write(str)
    print(str)
    file.close()


def ui():
    print(file1, "\n\nWelcome to the Bettinator!\n\n"
                 "We're going to jump right in and\n"
                 "print out all the team data.\n\n")

    text = input("Do you want bet 1 or bet 2?\n\n"
                 "(Note: Entering anything other than\n"
                 "'1' or '2' will quit the program.)\n")

    if text == "1":
        try:
            writer(file1, "Available Teams and Players:\n\n")

            for id in range(0, len(CSV_Team)):
                team = team_hash.lookup(id)
                writer(file1, str(team) + "\n")

            parse(team_hash, 0)
            ui()

        except ValueError:
            print("Invalid Entry, Please Restart.\n")
            ui()

    elif text == "2":
        try:
            writer(file1, "\nAvailable Teams and Players:\n\n")

            for id in range(0, len(CSV_Team)):
                team = team_hash.lookup(id)
                writer(file1, str(team) + "\n")

            parse(team_hash, 1)
            ui()

        except ValueError:
            print("Invalid Entry, Please Restart.\n")
            ui()

    else:
        print("Invalid Entry, Quitting Program...\n")
        return


class Main():
    ui()
