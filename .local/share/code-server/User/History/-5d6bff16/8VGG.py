#1 get the user's age
age_input = input ("how old are you")
#2 text into number 
age = int(age_input)
#3 make the decision 
if age >= 18:
    print('you are an adult.')
    print('you can vote.')
elif age > 12:
    print('you are a teenager.')
    print('you can't vote yet.')
else :
    print('you are a child')
    