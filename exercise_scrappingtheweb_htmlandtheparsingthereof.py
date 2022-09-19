from bs4 import BeautifulSoup
import requests

html = requests.get("http://www.example.com").text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p')
first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()

print(first_paragraph)
print(first_paragraph_text)
print(first_paragraph_words)

#first_paragraph_id = soup.p['id']   # raises KeyError if no 'id'
#first_paragraph_id2 = soup.p.get('id') # returns None if no 'id'

#all_paragraphs = soup.find_alL('p') # or just soup('p')
#paragraphs_with_ids = [p for p in soup('p') if p.get('id')]

#important_paragraphs = soup('p', {'class' : 'important'})
#important_paragraphs2 = soup('p', 'important')
#important_paragraphs3 = [p for p in soup('p')
#                         if 'important' in p.get('class', [])]

