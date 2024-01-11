from collections import Counter

my_str = """Machine learning is an important component of the growing field of data science.
Through the use of statistical methods, algorithms are trained to make classifications or predictions,
and to uncover key insights in data mining projects. These insights subsequently drive decision making within 
applications and businesses, ideally impacting key growth metrics. As big data continues to expand and grow,the market demand for data scientists will increase.
They will be required to help identify the most relevant business questions and the data to answer them."""

#First methos

my_words = my_str.split()
word_counts = Counter(my_words)
unique_words = set(my_words)

number_of_all_words = len(my_words)
number_of_unique_words = len(unique_words)
number_of_repetitive_words = number_of_all_words - number_of_unique_words

print(f"all words: {number_of_all_words}")
print(f"unique words: {number_of_unique_words}")
print(f"repetitive words: {number_of_repetitive_words}")

special_words = {"am", "is", "are", "was", "were"}
tobe_counts = {word: count for word, count in word_counts.items() if word in special_words}
total_specials = sum(tobe_counts.values())

print(f"Total tobe words: {total_specials}")
for word, count in tobe_counts.items():
    print(f"{word} : {count}")
