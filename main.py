from rich.console import Console
from rich.prompt import Prompt
from random import choice
from words import word_list


WELCOME_MESSAGE = f'\n[white on blue] WELCOME TO WORDLE [/]\n'
PLAYING_INSTRUCTIONS = "You may start guessing\n"
GUESS_STATEMENT = "\nENTER YOUR GUESS"
ALLOWED_GUESSES = 6

console = Console()

SQUARES = {
    'correct_place': '🟩',
    'correct_letter': '🟨',
    'incorrect_letter': '⬛'
}

def correct_place(letter):
	return f'[black on green]{letter}'

def correct_letter(letter):
	return f'[black on yellow]{letter}'

def incorrect_letter(letter):
	return f'[black on white]{letter}'


def check_guess(guess, chosen_word):
	guessed = []
	wordle_pattern = []
	for i, letter in enumerate(guess):
		if letter in chosen_word:
			if letter == chosen_word[i]:
				guessed.append(correct_place(letter))
				wordle_pattern.append(SQUARES['correct_place'])
			else:
				guessed.append(correct_letter(letter))
				wordle_pattern.append(SQUARES['correct_letter'])
		else:
			guessed.append(incorrect_letter(letter))
			wordle_pattern.append(SQUARES['incorrect_letter'])
	
	return ''.join(guessed), ''.join(wordle_pattern)



def game(chosen_word):
	end_of_game = False
	already_guessed = []
	number_of_guesses = 0
	all_words_guessed = []
	full_wordle_pattern = []

	while not end_of_game:
		guess = Prompt.ask(GUESS_STATEMENT).upper()
		if len(guess) == 5:
			if guess not in already_guessed:
				number_of_guesses += 1
				already_guessed.append(guess)
				guessed, pattern = check_guess(guess, chosen_word)
				all_words_guessed.append(guessed)
				full_wordle_pattern.append(pattern)

				console.print(*all_words_guessed, sep="\n")

				if number_of_guesses == 6  or guess == chosen_word:
					end_of_game = True

				if number_of_guesses == 6 and guess != chosen_word:
					console.print(f'\n[red]WORDLE X/{ALLOWED_GUESSES}[/]')
					console.print(f'\n[green]Correct Word: {chosen_word}[/]')
				else:
					console.print(f"\n[green]WORDLE {len(already_guessed)}/{ALLOWED_GUESSES}[/]\n")

				console.print(*full_wordle_pattern, sep="\n")

			else:
				console.print("[red]You have already guessed this word. You do not lose any attempt:)\n")
		
		elif len(guess) == 0:
			console.print("[red]Type a five letter word\n")
		else:
			console.print("[red]Guessed word should be of five letters\n")





if __name__ == '__main__':	
	chosen_word = choice(word_list)
	console.print(WELCOME_MESSAGE)
	console.print(PLAYING_INSTRUCTIONS)
	game(chosen_word)