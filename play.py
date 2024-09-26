from random import randint

class TheGame:

    def __init__(self):
        self.val = ["Sten", "Sax", "Påse"]
        self.computer_wins = 0
        self.user_wins = 0
        self.rounds = 0

    def klunsa(self):
        return randint(1,3)

    def play(self, user):
        computer = self.klunsa()

        if user not in range(0,4):
            print("Ej korrekt val! Försök igen!")
            return None

        # Avsluta om användaren skriver in 0
        if user == 0:
            print("#################################################")
            print("Användaren avslutade spelet!")
            return 'exit'

        # Skriva ut omgångens resultat
        print(f'Resultat användare: {self.val[user-1]}, dator: {self.val[computer-1]}')

        # Kolla vem som vann omgången
        if user == computer:
            print("Oavgjort!")
        elif user == 1 and computer == 2:
            print("Du vann")
            self.user_wins += 1
        elif user == 2 and computer == 3:
            print("Du vann")
            self.user_wins += 1
        elif user == 3 and computer == 1:
            print("Du vann")
            self.user_wins += 1
        elif computer == 1 and user == 2:
            print("Datorn vann")
            self.computer_wins += 1
        elif computer == 2 and user == 3:
            print("Datorn vann")
            self.computer_wins += 1
        elif computer == 3 and user == 1:
            print("Datorn vann")
            self.computer_wins += 1

        print("#################################################")
        self.rounds += 1
        return self.winner_game()

    def winner_game(self):
        # När någon kommer till 3 vinster så avslutas spelet
        if self.user_wins == 3 or self.computer_wins == 3:
            if self.user_wins == 3:
                print(f'Användaren fick 3 vinster först och vann!')
            elif self.computer_wins == 3:
                print(f'Datorn fick 3 vinster först och vann!')
            return 'exit'

    def game_score(self):
        print(f'Ställning användaren: {self.user_wins}, dator: {self.computer_wins}')       


def main():
    
    game = TheGame()

    print("Sten, Sax, Påse. Först till 3 vinster!")
    print("#################################################")

    while True:

        if game.rounds > 0:
            game.game_score()
        
        try:
            user = int(input("Välj 1=Sten, 2=Sax, 3=Påse, 0 för att avsluta: "))
        except ValueError:
            print("Ej korrekt val! Försök igen!")
            continue

        result = game.play(user)

        if result == 'exit':
            break
  
    
if __name__ == "__main__":
    main()