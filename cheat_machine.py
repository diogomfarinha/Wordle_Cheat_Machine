# Open the word list file
data = open("5_letter_word_list.txt", "r").read()
  
# Convert string to list
word_list = data.split("\n")

# Match key to a word
def match_key(word,key):
    for index, c in enumerate(key):
        if c!='_' and word[index]!=c:
            return False
    return True

# Get word suggestions for a given key, letters in a word and letters not in a word
def get_suggestions(key,letters,not_letters):
    suggestions = []
    for word in word_list:
        if match_key(word, key) and all(c in word for c in letters) and all(c not in word for c in not_letters):
            suggestions.append(word)
    return suggestions

#Example usage
suggestions = get_suggestions('__ung', 'un', 'adieboschkfl')         
print(*suggestions, sep='\n')
