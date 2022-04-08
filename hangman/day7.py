# ============================ Challenge Hangman  ============================
import random
import hangman_art
import hangman_words

print(hangman_art.logo)

stages = hangman_art.stages
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
#print(f"Psst, the solution is {chosen_word}.")

display = []
for letter in chosen_word:
   display.append(["_"])

lives = 6
end_of_game = False

while end_of_game == False:
    guess = input("\nGuess a letter: ").lower()
    
    for position in range(word_length):
      letter = chosen_word[position]
      # print(f"Current position: {position}\nCurrent letter: {letter}\nCurrent guess: {guess}\n")
      if letter == guess:
        display[position] = letter
        # print("right")
    display_str = ' '.join(str(i) for i in display)
    print(f"\n{display_str}\n")
    if guess not in chosen_word:
      lives -= 1
      print(f"Wrong. You guessed the letter '{guess}', that's not in the word.\nYou now have {lives} lives.")
      print(stages[lives])
      if lives == 0:
        end_of_game = True
        print(f"You lose. The hangmans word was: {chosen_word}")
    
    if "_" not in display[position]:
       end_of_game = True
       print(f"You win. The hangmans word was: {chosen_word}")
