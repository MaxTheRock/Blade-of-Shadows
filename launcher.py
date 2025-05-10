import curses
import json
import random
from colorama import Fore
import os
import time

def clear_screen():
	print("\033c", end='')

def display_menu_curses(title, options):
	"""
	Displays a terminal menu using curses and returns the selected option.

	:param title: The title of the menu.
	:param options: A list of menu options.
	:return: The selected option as a string.
	"""
	def menu(stdscr):
		curses.curs_set(0)  # Hide the cursor

		# Initialize color pairs
		curses.start_color()
		curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Green text on black background

		current_row = 0

		while True:
			stdscr.clear()
			stdscr.addstr(f"{title}\n")
			stdscr.addstr("-" * len(title) + "\n")

			for idx, option in enumerate(options):
				if idx == current_row:
					# Highlight the current option with green and bold
					stdscr.addstr(f"> {option}\n", curses.color_pair(1) | curses.A_BOLD)
				else:
					stdscr.addstr(f"  {option}\n")

			key = stdscr.getch()

			if key == curses.KEY_UP and current_row > 0:
				current_row -= 1
			elif key == curses.KEY_DOWN and current_row < len(options) - 1:
				current_row += 1
			elif key == curses.KEY_ENTER or key in [10, 13]:  # Enter key
				return options[current_row]

	return curses.wrapper(menu)

def file_create():
	# Step 1: Load the template JSON
	with open('assets/template.json', 'r') as template_file:
		template_data = json.load(template_file)

	# Step 2: Modify the template (if needed)
	template_data["player"]["name"] = input("Enter player name: ")
	template_data["player"]["level"] = 1
	template_data["player"]["experience"] = 0
	template_data["player"]["health"] = 100
	while True:
		template_data["player"]["stats"] = {
			"strength": random.randint(1, 100),
			"dexterity": random.randint(1, 100),
			"intelligence": random.randint(1, 100),
			"wisdom": random.randint(1, 100),
			"charisma": random.randint(1, 100),
			"speed": random.randint(1, 100),
		}
		print(Fore.GREEN + "Player stats generated." + Fore.RESET)
		print(json.dumps(template_data["player"]["stats"], indent=4))
		stats_choice = input(Fore.YELLOW + "Do you want to reroll? (y/n): " + Fore.RESET)
		if stats_choice.lower() == 'y':
			clear_screen()
			continue
		elif stats_choice.lower() == 'n':
			break
	
	new_choice = input(Fore.YELLOW + "Are you sure you want to continue (This will delete any current data!) (y/n): " + Fore.RESET)
	if new_choice.lower() == 'y':	
		print(Fore.GREEN + "New game created." + Fore.RESET)

	# Step 3: Write the modified data to a new JSON file
	with open('assets/player_data.json', 'w') as output_file:
		json.dump(template_data, output_file, indent=4)

def main():
	while True:
		clear_screen()
		option = display_menu_curses("Welcome to Blade of Shadows v0.0.5", ['New', 'Continue', 'Settings', 'Quit'])

		if option == 'New':
			file_create()
		elif option == 'Continue':
			if not os.path.exists('assets/player_data.json'):
				print(Fore.RED + "No saved game found. Please create a new game first." + Fore.RESET)
				time.sleep(2)
			else:
				print("You selected Continue")
				break
		elif option == 'Settings':
			print("You selected Settings")
		elif option == 'Quit':
			print("Exiting...")
			exit()
			break

if __name__ == "__main__":
  main()