import random 

while True:
        print("****")
        user=(input("Guess the number between 1 and 10!: "))

        def guess_nr_game():
            generator=random.randint(1,10)               
            if not user.strip().isdigit():
                print("ERROR")
                print("Parameters need to be numbers!")
            else:
                if generator!=int(user):
                    print("!!!!")
                    print(generator,"Try again!")  
                else:
                    print("$$$$")
                    print(generator,"Congratulations! You guessed the number correctly!")
        guess_nr_game()                        
                                                                   
                