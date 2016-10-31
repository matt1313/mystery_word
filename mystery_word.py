import random

easy_mode = []
medium_mode = []
hard_mode = []

collection = open("/usr/share/dict/words", "r")
line = collection.read().lower()
big_list = line.split()



def word_class():
    master_list = big_list
    for words in master_list:
        if len(words) >= 4 and len(words) <= 6:
            easy_mode.append(words)
            print(len(easy_mode))
            return easy_mode

        if len(words) >= 6 and len(words) <= 8:
            medium_mode.append(words)
            return medium_mode

        if len(words) >= 8:
            hard_mode.append(words)
            return hard_mode

def word_choice(big_list):
    word_pick= random.choice(file_read)
    return word_pick

def game_word(words, guesses):
    progress_display = []
    for letter in words:
        if letter in guesses:
            progress_display.append(letter)
        else:
            progress_display.append('_')
    progress_display = ' '.join(progress_display)
    progress_display = progress_display.upper()
    return progress_display

def finished(words, guesses):
    progress = display_word(words, guesses)
    if '_' in progress:
        return False
    else:
        return True

def difficulty():
    diff = input("""
    READY PLAYER ONE!
    CHOOSE A GAME: Easy, Medium, or Hard """)
    diff.lower()

    if diff == 'easy':
        response = word_choice(easy_mode(master_list))
    elif diff == 'medium':
        response = word_choice(medium_mode(master_list))
    else:
        response = word_choice(hard_mode(master_list))
    return response

def next_stage(response):
    guesses = []
    misses = 0
    print("You're word is {} characters long.".format(len(response)))
    while finished(response, guesses) == False:
        the_guess = (input("PICK A LETTER, ANY LETTER! ")).LOWER()
        if len(the_guess) > 1:
            print("MAKE ONE SELECTION AT A TIME...")
        elif the_guess not in guesses:
            if the_guess not in response:
                print ("That's not in your word.")
                misses += 1
            else:
                print("Good choice!")
        else:
            print("Didn't you pick that already?")
        guesses.append(the_guess)
        print(game_word(response, guesses))
        print("Your guesses: {}".format(guesses))
        print("{} guesses left.".format(8 - fails))
        if fails >= 8:
            break
    if fails >= 8:
        mulligan = input("YOU LOSE! Do over? y/n  ".format(response))
        if mulligan == 'y':
            return main()
        else:
            print("Don't quit your day job.")

    else:
        winner = input("WINNER! Play again?")
        if winner == "y":
            return main()
        else:
            print("See you next time!")

def main():
    response = difficulty()
    return next_stage(response)

main()
