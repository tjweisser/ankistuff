import requests as req
from bs4 import BeautifulSoup
import sys
import pyperclip as pc
import csv
import pandas as pd
import time


# open csv containing french(!) words
df = pd.read_csv("words.csv", header=0)

# loop through dataframe and add info
for i in range(412):
    try:
        # use the cambridge dictionary to get defnition, family, gender, etc.
        res = req.get('https://dictionary.cambridge.org/dictionary/french-english/'
                      + df.at[i, 'word'])

        # generate soup
        soup = BeautifulSoup(res.text, 'lxml')

        # add info to dataframe
        df.at[i, 'translation'] = str.strip(
                                soup.find('span', class_='trans dtrans').text
                                )
        df.at[i, 'family'] = str.strip(
                                soup.find('span', class_='pos dpos').text
                                )
        df.at[i, 'phonetics'] = str.strip(
                                soup.find('span', class_='ipa dipa').text
                                )
        df.at[i, 'gender'] = str.strip(
                             soup.find('span', class_='gc dgc').text
                             )
        df.at[i, 'example_fr'] = str.strip(
                               soup.find('span', class_='eg deg').text
                               )
        df.at[i, 'example_en'] = str.strip(
                               soup.find('span', class_='trans dtrans hdb').text
                               )
        # pause for 3 seconds
        time.sleep(4)

    except AttributeError:
        pass

# print dataframe
print(df.head(4))
df.to_csv(r'export_dataframe.csv', index=False, header=True)
