from collections import defaultdict

def group_anagrams(words):
    anagram_dict = defaultdict(list)  # Dictionary to group anagrams
    frequency_dict = {}  # Dictionary to store frequencies of each group
    
    for word in words:
        # Sort the word to find the anagram key
        key = ''.join(sorted(word))
        anagram_dict[key].append(word)
    
    # Calculate the total frequency of characters for each group
    for key, group in anagram_dict.items():
        frequency = defaultdict(int)
        for word in group:
            for char in word:
                frequency[char] += 1
        frequency_dict[key] = dict(frequency)
    
    return anagram_dict, frequency_dict

def find_highest_frequency_group(frequency_dict):
    max_frequency = 0
    max_group = None
    
    for key, freq in frequency_dict.items():
        total_frequency = sum(freq.values())
        if total_frequency > max_frequency:
            max_frequency = total_frequency
            max_group = key
    
    return max_group, max_frequency

# Input and process
user_input = input("Enter a list of words (separated by commas): ")
words = [word.strip() for word in user_input.split(",")]
anagram_dict, frequency_dict = group_anagrams(words)

# Sorting the anagrams and displaying output
sorted_anagrams = []
for key in sorted(anagram_dict.keys()):
    sorted_anagrams.extend(anagram_dict[key])

print("\nWords sorted by anagram groups:")
print(sorted_anagrams)

print("\nAnagram Dictionary:")
for key, group in anagram_dict.items():
    print(f"'{key}': {group}")

print("\nCharacter Frequencies:")
for key, freq in frequency_dict.items():
    print(f"'{key}': {freq}")

# Finding the group with the highest total frequency
highest_group, highest_frequency = find_highest_frequency_group(frequency_dict)
print(f"\nGroup with the highest total character frequency: '{highest_group}' (Total Frequency: {highest_frequency})")
