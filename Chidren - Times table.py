import random

def testOnDivision():
    rN = generateRandomNumbers() #rN stands for random number

    numerator = rN[0] * rN[1] #gets a multiple of the first and second number
    dinominator = rN[1]    
    
    question = "\t\t\t\t Question: {0} {1} {2} = ".format(numerator, "/", dinominator)
    answer = numerator / dinominator
    
    return [question, answer]

    
def testOnMultiplication():
    rN = generateRandomNumbers() #rN stands for random number
    question = "\t\t\t\t Question: {0} {1} {2} = ".format(rN[0], "x", rN[1])
    answer = rN[0] * rN[1]
    
    return [question, answer]

def generateRandomNumbers():
    a = random.randint(2,12)
    b = random.randint(1,12)

    return [a, b]

def getAnswer(array):

    while True:
        answer = input(array[0])
        if answer.isdigit():
            answer = int(answer)
            if answer == array[1]: # checks against actual calculated correct answer
                print(" ^ Correct ^")
                break
            else:
                print(" --Wrong")
        else:
            print("This is not a number")
    


## Program Loop Starts Here ##
    
operation = "multiplication" # default starting operation
while True:
    #operations = ["multiplication", "division"]
    #typeOfOperation = random.choice(operations)

    if operation == "multiplication":
        getAnswer(testOnMultiplication())
    else:
        getAnswer(testOnDivision())

    if operation == "multiplication": # flips the operations back and forth 
        operation = "division"
    else:
        operation = "multiplication"

    
    
