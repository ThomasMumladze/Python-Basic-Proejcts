import random
computer_number = random.randint(1 , 30)

step_counter = 0;

while True:
    user_number = input('Guess The Number?!: ')
    if user_number == 'q' or user_number == 'exit':
        print("Bye!")
        break;
    elif not user_number.isdigit():
        print('Please Enter Only Number To Continue!')
        continue
    
    entered_number = int(user_number)
    step_counter += 1
    
    if entered_number == computer_number:
        print("Congratulation you won!")
        print("You Guess The Number in %d steps" % step_counter)
        break
    elif entered_number > computer_number:
        print("Your number is higher Than imagined number!")
    else:
        print("Your number is less Than imagined number!")
        
        



