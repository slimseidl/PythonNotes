class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    def get_win_percentage(self):
        win_pct = self.wins / (self.wins + self.losses)
        return win_pct
    
    # Good example of calling a method within another method
    # uses the self.get_win_percentage to call a method using parameters from within the class 
    def print_standing(self):
        print(f'Win percentage: {self.get_win_percentage():.2f}')
        if self.get_win_percentage() >= 0.50:
            print(f'Congratulations, the {self.name} have a winning average!')
        else:
            print(f'The {self.name} have a losing average.')


if __name__ == "__main__":
    team = Team()
   
    user_name = input("Enter Team Name:\n")
    user_wins = int(input("Enter Number of Wins:\n"))
    user_losses = int(input("Enter Number of Losses:\n"))
    
    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses
    
    team.print_standing()