raw_name = "   anil dANGI   "

# 1. strip() removes the extra spaces on the ends
clean_name = raw_name.strip()

# 2. title() makes the first letter big and others small
pro_name = clean_name.title()

# 3. len() counts the letters
letters = len(clean_name)

print("Original:" + raw_name)
print("Professional: " + pro_name)
print("Count of letters: " + str(letters))