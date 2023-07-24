import re

def remove_html_tags(text):
    result = re.compile('<.*?>')
    return result.sub(r'', text)

text = '<html> hello </html>'
print(remove_html_tags(text))

# df['column'].apply(remove_html_tags) 

