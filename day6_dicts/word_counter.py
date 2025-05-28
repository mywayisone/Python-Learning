# 🔍 1. Word Counter
# Input: sentence
# Output: dictionary of word frequencies

# Define word_counter() function
def word_counter(words: list):
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# Define the main() function
def main():
    user_input = input("Enter the sentence: ")
    words = user_input.split(" ")
    freq = word_counter(words)
    print(freq)


if __name__ == "__main__":
    main()