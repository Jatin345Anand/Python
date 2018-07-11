import random

optionList = ['stone', 'paper', 'scissor']

userCounter = 0
cpuCounter = 0

while True:
    
    cpu_choice = random.choice(optionList)

    userChoice = input("Enter your choice : ")
    print("CPU : ",cpu_choice)

    if userChoice == cpu_choice:
        print("Match Tie")
    elif userChoice == 'stone' and cpu_choice == 'scissor':
        print("User Win")
        userCounter += 1
        print("User : ",userCounter)
    elif userChoice == 'paper' and cpu_choice == 'stone':
        print("User Win")
        userCounter += 1
        print("User : ",userCounter)
    elif userChoice == 'scissor' and cpu_choice == 'paper':
        print("User Win")
        userCounter += 1
        print("User : ",userCounter)
    elif userChoice == 'stone' and cpu_choice == 'paper':
        print("CPU Win")
        cpuCounter += 1
        print("CPU : ",cpuCounter)
    elif userChoice == 'paper' and cpu_choice == 'scissor':
        print("CPU Win")
        cpuCounter += 1
        print("CPU : ",cpuCounter)
    elif userChoice == 'scissor' and cpu_choice == 'stone':
        print("CPU Win")
        cpuCounter += 1
        print("CPU : ",cpuCounter)
    else:
        print("Wrong Choice...")
    
