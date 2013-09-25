import random

print "Hello there."
print "What is your name?"
name = raw_input("> ")
print "Hello %s, what number am I thinking of between 1 and 100?" % name

random = random.randint(1, 100)

guessed = 0
tries = 1


while guessed != random:

    try:
        input = raw_input("> ")
        guessed = int(input)
        if guessed < random:
            print "Your guess is too low, try again."
            tries += 1
        elif guessed > random:
            print "Your guess is too high, try again."
            tries += 1
        else:
            print "Well done, %s! You found my number in %d tries!" % (name, tries)

    
    except ValueError:
        print "Give me a real number!"
