import requests as req
from bs4 import BeautifulSoup
import sys
import pyperclip as pc


sys.argv

# get user query
if len(sys.argv) > 1:
    word = ' '.join(sys.argv[1:])
else:
    word = pc.paste()


# use the cambridge dictionary to get defnition, family, gender, and phonetics
res = req.get('https://dictionary.cambridge.org/dictionary/french-english/'
              + word)
soup = BeautifulSoup(res.text, 'lxml')

# use linguee to get some example sentences
res2 = req.get('https://www.linguee.com/english-french/search?source=auto&query='
               + word)
soup2 = BeautifulSoup(res2.text, 'lxml')


# extract definition, family, examples, synonyms, language level, and audio
try:
    # translation
    translation = str.strip(soup.find('span', class_='trans dtrans').text)
    # part of speech or family of words (e.g. noun, verb, etc.)
    family = str.strip(soup.find('span', class_='pos dpos').text)
    # gender
    gender = str.strip(soup.find('span', class_='gc dgc').text)
    # phonetics
    phonetics = str.strip(soup.find('span', class_='ipa dipa').text)
    # example sentence
    examples = str.strip(soup2.find('div', class_='example_lines').text)
    # print type and definition
    #print(translation,
          #family,
          #gender,
          #phonetics)
    # print examples but with the target word hidden
    #print(examples.replace(word, "..."))
    print(examples.split("."))

# handle exception
except Exception as e:
    print(e)
    #print("Sorry, I couldn't find that word")
