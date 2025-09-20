import random

words = ["Hang", "Game", "Fun", "Console", "Challenge"]


print("""Welcome to Mini Word Guessing Game...
You have 5 words to choose a single one from.
The words include ("Hang", "Game", "Fun", "Console", "Challenge"). 
You have only 4 attempt to guess the randomly chosen word from the words above and Good luck!
""")

def get_word():
    ran = random.randint(0, len(words) - 1)
    return words[ran]
    
    
def main():
    
    attempt = len(words) - 1
    num = 1
    
    word = get_word()
    while  attempt > 0:
        print(f"You have {attempt} attempts to guess the selected word")
        user_input = input(f"{num} > ").lower()
        
   
        if user_input == word.lower():
            print("Congratulations!! You won!!!")
            break
            
        if not user_input or user_input.isdecimal():
            continue
    
        
        attempt -= 1
        num += 1
        
        if attempt <= 0:
            print(f"Sorry, You've got hanged! The selected word is {word}...")
    
    
if __name__ == "__main__":
    main()