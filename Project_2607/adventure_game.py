import json
import os

# Game state
state = {
    "location": "Start",
    "inventory": [],
    "game_over": False
}

# Game map and options
locations = {
    "Start": {
        "description": "You are in a dark cave with two paths.",
        "options": {
            "left": "Forest",
            "right": "Castle"
        }
    },
    "Forest": {
        "description": "You find a peaceful forest with a shiny sword on the ground.",
        "options": {
            "take sword": "Forest",
            "go back": "Start",
            "forward": "River"
        }
    },
    "Castle": {
        "description": "You enter a ruined castle and see a healing potion.",
        "options": {
            "take potion": "Castle",
            "go back": "Start",
            "forward": "Throne Room"
        }
    },
    "River": {
        "description": "You face a troll! Fight or run?",
        "options": {
            "fight": "Win",
            "run": "Forest"
        }
    },
    "Throne Room": {
        "description": "You find the final treasure guarded by a riddle master.",
        "options": {
            "solve riddle": "Riddle",
            "run": "Castle"
        }
    },
    "Riddle": {
        "description": "Riddle: What has keys but can't open locks?",
        "options": {}  # Input expected
    },
    "Win": {
        "description": "You defeated the troll with your sword and found the treasure!",
        "options": {}
    },
    "Lose": {
        "description": "The riddle master banishes you. Game over.",
        "options": {}
    }
}

def show_location():
    loc = state["location"]
    print(f"\nLocation: {loc}")
    print(locations[loc]["description"])
    if locations[loc]["options"]:
        print("Options:", ', '.join(locations[loc]["options"].keys()))
    else:
        state["game_over"] = True

def save_game():
    with open("game_save.json", "w") as f:
        json.dump(state, f)
    print("Game saved.")

def load_game():
    global state
    if os.path.exists("game_save.json"):
        with open("game_save.json", "r") as f:
            state = json.load(f)
        print("Game loaded.")
    else:
        print("No saved game found.")

def process_input(command):
    current = state["location"]

    # Custom logic for inventory and riddles
    if current == "Forest" and command == "take sword":
        if "sword" not in state["inventory"]:
            state["inventory"].append("sword")
            print("You picked up the sword.")
        else:
            print("You already have the sword.")
        return

    if current == "Castle" and command == "take potion":
        if "potion" not in state["inventory"]:
            state["inventory"].append("potion")
            print("You picked up the potion.")
        else:
            print("You already have the potion.")
        return

    if current == "Riddle":
        if command.lower().strip() in ["piano", "keyboard"]:
            print("Correct! You win the treasure!")
            state["location"] = "Win"
        else:
            print("Wrong answer!")
            state["location"] = "Lose"
        return

    # Built-in commands
    if command == "inventory":
        print("Inventory:", state["inventory"] if state["inventory"] else "Empty")
    elif command == "save":
        save_game()
    elif command == "load":
        load_game()
    elif command == "exit":
        print("Exiting game.")
        state["game_over"] = True
    elif command in locations[current]["options"]:
        state["location"] = locations[current]["options"][command]
    else:
        print("Unknown command.")

def main():
    print("===== Text Adventure Game =====")
    print("Commands: take sword, take potion, fight, solve riddle, save, load, inventory, exit")

    while not state["game_over"]:
        show_location()
        command = input("What do you do? ").strip().lower()
        process_input(command)

    print("\nGame Over.")

if __name__ == "__main__":
    main()
