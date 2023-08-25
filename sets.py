def add(a, b):
    return a+b

word = "abracdabra"
unique_chars =set(word)
print(unique_chars)

sentence = " beautiful , the moon is beautiful , isn't it? "
unique_words = set(sentence.split())
print(unique_words)

set1 = {1,7,5,9,3,2}
set2 = {5,7,3,4,11}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

