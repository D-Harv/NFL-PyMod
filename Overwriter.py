import csv
from Hashmap import HashTable
from Team import Team


class Overwriter:

    def go(x):
        def read_csv(filename):
            with open(filename, 'r+') as file:
                return list(csv.reader(file))

        def write_csv_data(filename, data):
            with open(filename, 'w+', newline='') as file:
                writer = csv.writer(file)
                # Write the list of lists directly, which contains unpacked values
                for row in data:
                    writer.writerow(row)  # Ensure each row has individual elements, no brackets

        def load_roster(hash_table):
            for team in read_csv("./Roster.csv"):
                ID = team[0]
                Name = team[1]
                WR = team[2]
                RB = team[3]

                tm = Team(ID, Name, WR, RB)

                hash_table.insert(ID, tm)

        def drop_index(li, hsh):
            for i in range(len(li)):
                name = li[i][1]
                recv = li[i][2]
                hb = li[i][3]

                hsh.insert(name, [recv, hb])

        roster = HashTable()
        load_roster(roster)

        teams = HashTable()
        drop_index(roster.to_list(), teams)

        def writin():
            team = HashTable()
            num = int(input("\nHow many games are happening this week? "))
            print("When entering the team, skip the city.\n")

            for i in range(num * 2):  # Each game has 2 teams
                team_name = input(f"Team {i + 1}? ")
                guys = teams.lookup(team_name)
                wr = input(f"WR for Team {i + 1}? ") if
                input(f"Is {guys[1]} injured?") == "Yes" else
                guys[1]
                rb = input(f"RB for Team {i + 1}? ") if
                input(f"Is {guys[2]} injured?") == "Yes" else
                guys[2]
                team.insert(num, [team_name, wr, rb])

            return team.to_list()

        CSV_Teams = writin()
        write_csv_data(f"Week{x}.csv", CSV_Teams)
        print(f"Data successfully written to Week{x}.csv")