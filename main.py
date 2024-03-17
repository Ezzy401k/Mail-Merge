# Open the file containing the list of names in read mode
names = open("./Input/Names/invited_names.txt", "r")
# Read the lines from the file and store them in a list
list1 = names.readlines()
# Close the file
names.close()

# Open the template letter file in read mode
letters = open("./Input/Letters/starting_letter.txt")
# Read the content of the template letter
letter = letters.read()
# Close the file
letters.close()

# Initialize an empty list to store modified names
name = []

# Iterate over each name in the list of names
for i in list1:
    # If the length of the name is greater than 4 characters
    if len(i) > 4:
        # Remove the newline character at the end of the name
        j = len(i) - 1
        name.append(i[:j])
    else:
        # Otherwise, add the name as is to the list
        name.append(i)

# Iterate over each modified name
for n in name:
    # Replace the placeholder '[name]' in the template letter with the current name
    x = letter.replace("[name]", f"{n}")
    # Open a new file for writing the personalized letter
    save = open(f"./Output/ReadyToSend/Letter_for_{n}.txt", "w")
    # Write the personalized letter to the file
    save.write(x)
    # Close the file
    save.close()
