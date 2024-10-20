from collections import Counter
with open('books/frankenstein.txt', 'r') as f:
    content = f.read()
    words = content.split()
    content_lower = content.lower()
    output = Counter(content_lower)
    print(len(words), "words found in the document\n")
    for x in output:
        print("The '", x, "'character was found ", output[x], " times.")
