def count_word_frequency(sentence):
    # Initialize an empty dictionary to count word frequency
    word_frequency = {}
    # Split the sentence into words
    words = sentence.split()
    # Iterate over each word in the list
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in word_frequency:
            word_frequency[word] += 1
        # Otherwise, add the word to the dictionary with a count of 1
        else:
            word_frequency[word] = 1
    # Return the dictionary of word frequencies
    return word_frequency


# Test the function with an example sentence
sentence = "This is a simple example of a sentence to test if a function is working."
result = count_word_frequency(sentence)

# Print the word frequency
for word, count in result.items():
    print(f"'{word}': {count}")