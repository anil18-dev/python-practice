import csv

# The "Key" to decode the PAN Status
status_map = {
    "P": "Individual",
    "C": "Company",
    "H": "HUF",
    "A": "AOP",
    "B": "BOI",
    "G": "Govt Agency",
    "F": "Firm",
    "T": "Trust"
}

counts = {}

# Open your real data file
with open('investors.csv', 'r') as file:
    reader = csv.DictReader(file)
                                        
    for row in reader:
        # Get PAN Number and remove spaces/quotes
        pan = row['PAN Number'].strip().replace('"', '')
                                                                    
        # The 4th letter is the Status (Index 3 in Python)
        char = pan[3]
                                                                                            
        # If we see it, add 1 to its count
        if char in counts:
            counts[char] += 1
                                                                                                                                else:
                                                                                                                                            counts[char] = 1

                                                                                                                                            print("--- INVESTOR STATUS REPORT ---")
                                                                                                                                            for char, total in counts.items():
                                                                                                                                                full_name = status_map.get(char, "Unknown")
                                                                                                                                                    print(f"{full_name}: {total}")