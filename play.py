from random import randint

# Funktion för att skapa slump till datorn
def klunsa():
    return randint(1,3)

# Lista att använda för att skriva ut resultat i text per omgång
val = ["Sten", "Sax", "Påse"]

# Initiera antal vinster per user / computer
computer_wins = 0
user_wins = 0

print("Sten, Sax, Påse. Först till 3 vinster!")

# Loopa tills nån vinner 3 gånger eller väljer att avsluta med 0.
while True:

    print(f'Ställning användaren: {user_wins}, dator: {computer_wins}')

    # Användarens val samt datorns slumpade val
    user = int(input("Välj 1=Sten, 2=Sax, 3=Påse, 0 för att avsluta: "))
    computer = klunsa()

    print(f'Resultat användare: {val[user-1]}, dator: {val[computer-1]}')

    # Oavgjort
    if user == computer:
        print("Oavgjort!")

    # Användaren vinner
    elif user == 1 and computer == 2:
        print("Du vann")
        user_wins += 1
    elif user == 2 and computer == 3:
        print("Du vann")
        user_wins += 1
    elif user == 3 and computer == 1:
        print("Du vann")
        user_wins += 1

    # Datorn vinner
    elif computer == 1 and user == 2:
        print("Datorn vann")
        user_wins += 1
    elif computer == 2 and user == 3:
        print("Datorn vann")
        user_wins += 1
    elif computer == 3 and user == 1:
        print("Datorn vann")
        user_wins += 1

    print("#################################################")

    # När någon kommer till 3 vinster så avslutas spelet
    if user_wins == 3 or computer_wins == 3:
        if user_wins == 3:
            print(f'Användaren fick 3 vinster först!')
        elif computer_wins == 3:
            print(f'Datorn fick 3 vinster först!')
        break
    
    # Avsluta spelet om användaren väljer 0 istället för sten sax påse.
    if user == 0:
        print("Användaren avslutade spelet!")
        break