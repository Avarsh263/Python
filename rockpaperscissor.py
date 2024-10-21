import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    rounds = 3
    
    for _ in range(rounds):
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        while user_choice not in choices:
            user_choice = input("Invalid choice! Please enter rock, paper, or scissors: ").lower()
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer\n")
    
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("Sorry, the computer won the game.")
    else:
        print("The game is a tie!")

if __name__ == "__main__":
    rock_paper_scissors()
