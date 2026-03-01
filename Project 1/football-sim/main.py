from random import randint

def calculate_ball_position(force, direction):
    pass

def check_goal(pos):
    pass

def game_end(score):
    print(f"Game ended. Final score: {score}")

def game_loop():
    net_columns = 10
    net_rows = 7
    
    remaining_shots = 3
    score = 0
    
    while remaining_shots > 0:
        force = input("Enter the force of the kick (1-10): ")
        direction = input("Enter the direction of the kick (left, center, right): ").lower()
        # Validate force and direction
        
        remaining_shots -= 1
        
        # Calculate the position of the kick based on the force and direction
        pos = calculate_ball_position(force, direction)
        is_goal = check_goal(pos)
        if is_goal:
            print("Goal scored!")
        else:
            print("Kick missed the goal.")
            
    print(f"Game over! Your final score is: {score}")
    game_end(score)
    

def main():
    print("Welcome to the Football Simulator - Penalty Shots!")
    print("1. Start")
    print("2. Exit")

    while True:
        choice = input("Enter your choice: ").lower()
        if choice == '1' or choice == 'start':
            game_loop()
        elif choice == '2' or choice == 'exit':
            print("Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")
        
main()
