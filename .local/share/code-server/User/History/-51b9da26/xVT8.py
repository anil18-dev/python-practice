#1 we create the skill
def convert_to_usd(rupees):
    usd = rupees / 83.5  #current value
    return usd

#2 we use the skill
amount=float(input("amount in rupees:"))
result=convert_to_usd(amount )
#3 Result 
print("That is $" + str(round(result, 2)) + " Dollars")

# universal converter 
def universal_converter(amount,choice ):
    if choice == "1":
     #rupees to ussd 
    return amount/83.5
print("1: rupees to usd" )
print("2: rupees to usd")
c=input("choose 1 or 2:")
amt=float(input("enter the amount :"))
final=universal_converter(amt,c)
print("result:"+ str(round(final,2)))
# new
def universal_converter(amount, choice):
    if choice == "1":           
# Rupees to USD
                        return amount / 83.5
                            elif choice == "2":
                                    # USD to Rupees
                                            return amount * 83.5

                                            print("1: Rupees to USD")
                                            print("2: USD to Rupees")
                                            c = input("Choose 1 or 2: ")
                                            amt = float(input("Enter amount: "))

                                            final = universal_converter(amt, c)
                                            print("Result: " + str(round(final, 2)))