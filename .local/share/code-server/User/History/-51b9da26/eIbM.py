#1 we create the skill
def convert_to_usd(rupees):
    usd = rupees / 83.5  #current value
    return usd

#2 we use the skill
amount=float(input("amount in rupees:"))
result=convert_to_usd(amount )
#3 Result 
print("that is $"+ str(round(result.2)+"dollar"))