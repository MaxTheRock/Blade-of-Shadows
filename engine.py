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

def main():
	with open("assets/dialogue.json") as d:
		data = json.load(d)
		while True:
			clear_screen()
			m_choice = display_menu_curses(random.choice(data["menu"]["game_menu"]), ["Investigate", "Loot", "Travel", "Random", "Inventory", "Stats", "Save & Quit"])
			if m_choice == "Investigate":
				print("This will investigate the area your in.")
				time.sleep(2)
			elif m_choice == "Loot":
				print("This will loot the area your in.")
				time.sleep(2)
			elif m_choice == "Travel":
				print("This will travel to a new area from a menu.")
				time.sleep(2)
			elif m_choice == "Random":
				print("This will randomly choose an option from the menu.")
				time.sleep(2)
			elif m_choice == "Inventory":
				print("This will show your inventory.")
				time.sleep(2)
			elif m_choice == "Stats":
				print("This will show your stats.")
				time.sleep(2)
			elif m_choice == "Save & Quit":
				print("This will save your game and quit.")
				time.sleep(2)
		
if __name__ == "__main__":
  main()