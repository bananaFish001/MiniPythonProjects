# string concatenation (aka how to add strings together?)
# suppose we want to create a string that says "subscribe to _______"
youtuber = " Raj Singh"  # some string variable

# a few ways to do it
print("subscribe to" + youtuber)
print("subscribe to{}".format(youtuber))
print(f"subscribe to{youtuber}")

adj = input("Adjectives: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous_Person: ")
madlib = (f"Computer programming is so{adj}! It makes me very excited all the time because \
I love to{verb1}. Stay hydrated and {verb2} like you are {famous_person}")

print(madlib)
