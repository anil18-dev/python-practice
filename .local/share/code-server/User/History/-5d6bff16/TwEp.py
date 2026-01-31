#1 get the user's age
age_input = input ('how old are you.')
#2 text into number 
age = int(age_input)
has_id = input("Do you have a voter ID? (yes/no): ")
if age >= 18 and has_id == "yes":
    print("You are eligible to vote!")
    elif age >= 18 and has_id == "no":
#3 make the decision 
if age >= 18:
    print('you are an adult.')
    print('you can vote.')
elif age > 12:
    print('you are a teenager.')
    print('you cannot vote yet.')
else :
    print('you are a child')
    print('go play outside.')

