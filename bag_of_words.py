import nltk

def tokenize(input_sentence):
    return nltk.word_tokenize(input_sentence)

def bag_of_words(sentence, vocabulary):
    bag = []
    for word_vocabulary in vocabulary:
        occurences = 0
        for word_sentence in sentence:
            if(word_vocabulary == word_sentence):
                occurences += 1
        bag.append(occurences)
    return bag

if __name__ == '__main__':
    input_sentence = "I get my news mostly from the internet, especially from blogs"
    vocabulary = "news internet blogs videos programming"
    print(bag_of_words(tokenize(input_sentence), tokenize(vocabulary)))
