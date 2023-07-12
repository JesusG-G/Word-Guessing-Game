import random
import os

#Function to create the file path with the wordlist.txt
def file_path_complete() -> str:
    current_working_directory = os.getcwd()
    file_path = os.path.join(current_working_directory,'src\wordlist.txt')
    return file_path

#Function to choose the word of the list
def choose_the_word(file_path: str) -> str:
    with open(file_path) as file:
        wordlist: list[str] = file.read().splitlines()
    chosen_word: str = random.choice(wordlist)
    return chosen_word

def determinate_winner(chosen_word: str) -> bool:
    minimun_attemp: int = len(chosen_word) + 2
    letter_guessed: str = ''
    guess_loop: bool = False
    #append the underscore on the guesses list
    guesses:list[str] = ["_" for _ in range(len(chosen_word))]
    #create a list of the chosen word
    chosen_word_list: list[str] = [c for c in chosen_word]

    while minimun_attemp >= 0:
        while guess_loop != True:
            guess_character:str = str(input("Please enter your guess character: "))
            if not guess_character.isalpha():
                print("Please enter only a Letter")
            elif guess_character in letter_guessed:
                print("You have already guessed that letter")
            elif len(guess_character) == 1:
                guess_loop = True
            else:
                print("Please enter ONLY one character.")

        for word_character in chosen_word:
            if guess_character == word_character:
                index: int = chosen_word_list.index(guess_character)
                #Save the guess character on the guess list
                guesses[index] = guess_character
                #Replace in the chosen word list the guess character for underscore
                chosen_word_list[index] = '_'
                #update the chosen word
                chosen_word = ''.join(chosen_word_list)
                print(f"The {guess_character} is in the chosen word")
                print(f"You have {minimun_attemp} tries yet")
                guess_loop = False
                letter_guessed += guess_character
            else:
                letter_guessed += guess_character
                guess_loop = False
        if guess_character not in chosen_word_copy:
            minimun_attemp -=1
            print(f"Wrong!! You have {minimun_attemp} attempts to try yet")
            letter_guessed += guess_character
            guess_loop = False
            if minimun_attemp == 0:
                print("No more attempts")
                return False
        elif ''.join(guesses) == chosen_word_copy:
            return True
        print(f"Your progress is {''.join(guesses)}")

if __name__ == "__main__":
    #call of the function 
    file_path: str = file_path_complete()
    chosen_word:str  = choose_the_word(file_path)
    #A little presentation
    print("Welcome to the Word Guessing Game")
    print("------------------------------------------------------------------")
    print("""
    -----------------------------------------------------------------------------------
        Rules:
        1.A random Word is choosen from the list.
        2.The Player is going to introduce one letter at time. Attempting to guess the word.
        3.The Player have 12 attemps to discover the word.
    -----------------------------------------------------------------------------------
    """)
    #Create a copy of the chosen word
    chosen_word_copy:str = chosen_word
    winner: bool = determinate_winner(chosen_word)
    if winner:
        print(f"Congratulations you won! The word was {chosen_word_copy}")
    else:
        print("Oh too bad! You Loose, please try again")
        print(f"The word was {chosen_word_copy}")