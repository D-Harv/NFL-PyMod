class Team:
    def __init__(self, name, wr, rb):
        self.id = id
        self.name = name
        self.wr = wr
        self.rb = rb

    def __str__(self):
        teamer = "A" if int(self.id) % 2 == 0 else "B"

        return(f"Team {teamer} is the "
               f"{self.name} their top Wide Receiver is \n"
               f"{self.wr}, and their top Running Back is \n{self.rb}.\n")
