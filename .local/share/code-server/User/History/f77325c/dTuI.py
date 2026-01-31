messy_data = ["  anil", "sunil ", "  HARIOM  ", "raHul", "joy"]
long_names = []

print("Filtering long names...")

for name in messy_data:
    fixed = name.strip().title()
        
# We only add to the list IF the name is longer than 4 letters
if len(fixed) > 1:
    long_names.append(fixed)
print("CLEANED & FILTERED DATA:")
print(long_names)