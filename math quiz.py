import random

name = raw_input("What is your name? ")
print ("Hello", name, "Welcome to your maths quiz")
age = raw_input("How old are you? ")
print "Ok %s we wont tell anyone your %s years old. It will be our secret.)" % (name, age)
score = 0
ready = raw_input("Press 'ENTER' to begin.")
print "The current score is:", score

for question_num in range(1, 11):
    ops = ['+', '-', '*']
    rand = random.randint(1, 10)
    rand2 = random.randint(1, 10)
    operation = random.choice(ops)
    maths = eval(str(rand) + operation + str(rand2))
    print('\nQuestion number: {}'.format(question_num))
    print ("The question is", rand, operation, rand2)

    d=int(input("What is your answer:"))
    if d == maths:
        print ("Correct")
        score = score+1
        print "Score is:", score
    else:
        print ("Incorrect. The actual answer is", maths)
