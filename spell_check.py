from textblob import TextBlob

text = 'this is notbook'

result = TextBlob(text)
print(result.correct().string)