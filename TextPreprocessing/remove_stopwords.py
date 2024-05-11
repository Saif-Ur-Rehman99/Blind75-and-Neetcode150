from nltk.corpus import stopwords

# print(stopwords.words('english'))

def remove_stopwords(text):
    new_text = []

    for word in text.split():
        if word in stopwords.words('english'):
            new_text.append('')
        else:
            new_text.append(word)
    x = new_text[:]
    new_text.clear()
    return ' '.join(x)

text = 'probably my all-time favorite movie, a story of selflessness'
print(remove_stopwords(text))