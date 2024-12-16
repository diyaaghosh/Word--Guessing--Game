import random
word_list=["Intel","Apple","Google","BNY","TCS","PWC","Jindal"]
computer_choice=random.choice(word_list)
computer_choice1=list(computer_choice)
total_moves=10
i=0
print("::::::::::::::::  Word-Guessing-Game ::::::::::::::::::\n")
print("Game Rules : \n1. You have only 10 chances to guess the word \n2. In each chance You have to guess a letter present in the word\n3. If the letter present in the Word then it shows that \n4. If you are able to guess all the letters of the word then you will win\n5. If the 10 chances are exhausted then you Loss\n")
while(i<total_moves):
    user_choice=(input("Enter the Letter You have Guessed : "))
    if(len(user_choice)>1):
        print("You guess more than one letter !!... Try again")
        continue
    
    if user_choice in computer_choice:
            print(f"'{user_choice}' is present in the word  ")
            if user_choice not in computer_choice1:
                computer_choice1.append(user_choice)
            computer_choice1.remove(user_choice)
    else:
            print(f"{user_choice} is not present in the word ") 
    if(len(computer_choice1)==0):
            break                    
    i+=1
              
              
if(len(computer_choice1)==0):
    print("\nYour Guess is Correct... The Word is ",computer_choice)
    print(f"You Guess the Word within {i+1} chances")
else:
    print("\nOoops !!! You drain out 10 chances !!! You can't guess the word .... Try again")                  
