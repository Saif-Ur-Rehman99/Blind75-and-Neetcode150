import re

def remove_url(text):
    result = re.compile(r'https?://\S+|www\.\S+')
    return result.sub(r'', text)

text1 = 'Check out https://www.kaggle.com/populationdata/org is clear'
text2 = 'Check out http://www.kaggle.com/data is clear'
text3 = 'Check out www.google.com is clear'
text4 = 'Check out https://www.kaggle.com/data on www.google.com website'

print(remove_url(text3))