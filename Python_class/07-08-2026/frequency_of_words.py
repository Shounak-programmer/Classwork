#Write a function that accepts a sentence and prints the frequency of every word, the most frequent word, the least frequent word, and the total number of unique words.  
def freq(sentence):
    words = sentence.split(" ")
    word_count = {}
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1    #used to get the value of the key if it exists, otherwise return 0 and add 1 to it.
        
    most_frequent_word = max(word_count, key=word_count.get)
    least_frequent_word = min(word_count, key=word_count.get)
    unique_words_count = len(word_count)
    
    print("Word Frequencies:")
    for word, count in word_count.items():
        print(f"{word}: {count}")
        
    print(f"\nMost Frequent Word: '{most_frequent_word}' with a count of {word_count[most_frequent_word]}")
    print(f"Least Frequent Word: '{least_frequent_word}' with a count of {word_count[least_frequent_word]}")
    print(f"Total Unique Words: {unique_words_count}")
a = input("Enter a sentence: ")
freq(a)