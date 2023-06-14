import random
import os

#Function to create the file path with the wordlist.txt
def file_path_complete():
    current_working_directory = os.getcwd()
    file_path = os.path.join(current_working_directory,'src\wordlist.txt')
    return file_path

#Function to choose the word of the list
def choose_the_word(file_path):
    with open(file_path) as file:
        wordlist = file.read().splitlines()
    chosen_word = random.choice(wordlist)
    return chosen_word

def determinate_winner(chosen_word):
    minimun_attemp = 12
    guess_attempt = 0
    guesses = []
    chosen_word_list = []
    guess_loop = False
    winner = False
    #append the underscore on the guesses list
    for i in range(len(chosen_word)):
        guesses.append("_")
    #create a list of the chosen word
    for c in chosen_word:
            chosen_word_list.append(c)

    while guess_attempt != minimun_attemp and winner != True:
        while guess_loop != True:
            guess_character = input("Please enter your guess character: ")
            if len(guess_character) == 1:
                guess_loop = True
            else:
                print("Please enter ONLY one character.")
        for i in range(len(chosen_word)):
            if guess_character in chosen_word:
                if guess_character == chosen_word[i]:
                    #Save the guess character on the guess list
                    guesses[i] = guess_character
                    #Replace in the chosen word list the guess character for underscore
                    chosen_word_list[i] = '_'
                    #update the chosen word
                    chosen_word = ''.join(chosen_word_list)
                    print(f"The {guess_character} is in the chosen word")
                    print(f"You have {minimun_attemp} tries")
                    guess_loop = False
                    #If guesses (like a string) is equal to the copy of chosen word the first while loop will finish
                    if ''.join(guesses) == chosen_word_copy:
                        winner = True
                    break
                else:
                    guess_loop = False
            else:
                minimun_attemp -=1
                guess_loop = False
                print(f"You have {minimun_attemp} tries")
                break
        print(f"Your progress is {''.join(guesses)}")
    
    return winner

if __name__ == "__main__":
    #call of the function 
    file_path = file_path_complete()
    chosen_word = choose_the_word(file_path)
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
    chosen_word_copy = chosen_word
    winner = determinate_winner(chosen_word)
    if winner:
        print(f"Congratulations you won! The word was {chosen_word_copy}")
    else:
        print("Oh too bad! You Loose, please try again")
        print(f"The word was {chosen_word_copy}")