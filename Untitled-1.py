# Create a string "s" with the value "I love to write python"
s = "I love to write python"

# Split the string into a list of words called "split_s"
split_s = s.split()

# Loop through the list of words; If any of the words contain the letter "i" print "I found 'i' in: '<WORD>'"
for word in split_s:
    if 'i' in word:
        print(f"I found 'i' in: '{word}'")
