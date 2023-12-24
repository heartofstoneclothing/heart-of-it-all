word_types = {
    "nouns": ["cat", "dog", "Paris", "London"],
    "verbs": ["run", "jump"],
    "adjectives": ["happy", "sad", "big", "small"],
    "adverbs": ["cat", "dog", "run", "jump", "happy", "sad", "big", "small", "Paris", "London"]
}

string_builder = ""

for word_type, words in word_types.items():
    for word in words:
        string_builder += word + ", "

string_builder = string_builder[:-2]

print(string_builder)
