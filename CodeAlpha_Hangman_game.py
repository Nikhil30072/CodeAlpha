import random
apps = ['apple', 'balloon', 'cartoon', 'donkey', 'eleven', 'falcon']
print("WELCOME TO HANGMAN GAME")
print("Let's Start the Game")
x_Words = random.choice(apps)
b_gussed_words = ['_'] * len(x_Words)
c_gussed_letter= []
d_attempts= 6
while d_attempts > 0 and "_" in b_gussed_words:
    print("Word:", " ".join(b_gussed_words))
    print("Guessed letters:", " ".join(c_gussed_letter))
    print("Attempts left:", d_attempts)
    A_guess = input("Enter your guess: ").lower()
    if not A_guess or len(A_guess) != 1 or not A_guess.isalpha():
        print("Enter a single valid letter.")
        continue
    if A_guess in c_gussed_letter:
        print("You already guessed that letter.")
        continue
    c_gussed_letter.append(A_guess)
    if A_guess in x_Words:
        print("Good guess")
        for i in range(len(x_Words)):
            if x_Words[i] == A_guess:
                b_gussed_words[i] = A_guess
    else:
        print("Wrong guess")
        d_attempts-= 1
if "_" not in b_gussed_words:
    print("Congratulations You guessed the word:", x_Words)
else:
    print("Out of attempts. The word was:", x_Words)
