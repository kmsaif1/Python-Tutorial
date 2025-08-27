import random
n = random.randint(1,100)
a = -1#we initialise it as -1 because n never become -1 so the condition always remain true
guesses = 0
while(a != n):
    a = int(input("Guess the number : "))
    if(a>n):
        print("Lower number please")
        guesses +=1

    else:
        print("higher number please ") 
        guesses +=1


print(f"You have finally guessed the number correctly in {guesses} attempt")