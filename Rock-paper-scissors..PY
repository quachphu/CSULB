rock = '''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
rock ="🪨"
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
paper="📄"
scissors = '''
    ______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
scissors = "✂️"
#rock = 999
'''Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.'''
import random
class RPS:
    def __init__(self):
        self.figure = [rock, paper, scissors]
        print("I am the constructor or the init method")

    def palyGame(self):
        again = True
        while again:
            uChoice = int (input ("Enter 0 Rock, 1, papaer, 2 Scissors ... "))

            while uChoice> 2 or uChoice<0:
                print("Wrong entry try again... ")
                uChoice = int(input("Enter 0 Rock, 1, papaer, 2 Scissors ... "))
            print(uChoice, self.figure[uChoice])

            cChoice = random.randint(0,2)
            print(cChoice, self.figure[cChoice])
            '''cChoice = random.choice(self.figure)
            print("This is using choice", cChoice)'''
            '''Rock 0 wins against scissors. 0 wins 2
            Scissors win against paper.   2 wins 1
            Paper wins against rock.       1, 0'''
            if uChoice == 0 and cChoice==2:
                print("I win :-)")
            elif cChoice == 0 and uChoice==2:
                print("AI  :-(")
            elif uChoice> cChoice:
                print("I win :-)")
            elif uChoice< cChoice:
                print("AI wins :-(")
            else:   # tie
                print("It is a tie   :-|")
            rep = input("Do you want to play again enter Y or any char otherwise ")
            if rep.lower()!="y":
                print("You want to exit ..Goodbye   ")
                again = False


g1 = RPS()
game2 = RPS()
g1.palyGame()


# WAY 2 
import random 
class RPS:
    def __init__(self):
        self.figure = ["🪨", "📄", "✂️"]
        self.games_played = 0
        self.user_wins = 0
        self.user_losses = 0
        self.user_ties = 0

    def playGame(self):
        again = True
        while again:
            uChoice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
            while uChoice > 2 or uChoice < 0:
                print("Wrong entry, try again.")
                uChoice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))

            print("Your choice:", self.figure[uChoice])

            cChoice = random.randint(0, 2)
            print("AI's choice:", self.figure[cChoice])

            self.games_played += 1

            if uChoice == cChoice:
                print("It's a tie!")
                self.user_ties += 1
            elif (uChoice == 0 and cChoice == 2) or (uChoice == 1 and cChoice == 0) or (uChoice == 2 and cChoice == 1):
                print("You win!")
                self.user_wins += 1
            else:
                print("AI wins!")
                self.user_losses += 1

            rep = input("Do you want to play again? (Y/N): ")
            if rep.lower() != "y":
                print("Exiting game. Goodbye!")
                again = False

    def calculate_ratio(self):
        if self.games_played == 0:
            print("No games played yet.")
            return
        win_ratio = self.user_wins / self.games_played
        loss_ratio = self.user_losses / self.games_played
        tie_ratio = self.user_ties / self.games_played
        print(f"Number of games played: {self.games_played}")
        print(f"Number of user wins: {self.user_wins}")
        print(f"Number of user losses: {self.user_losses}")
        print(f"Number of user ties: {self.user_ties}")
        print(f"Win ratio: {win_ratio:.2f}")
        print(f"Loss ratio: {loss_ratio:.2f}")
        print(f"Tie ratio: {tie_ratio:.2f}")


# Usage:
game = RPS()
game.playGame()
game.calculate_ratio()
