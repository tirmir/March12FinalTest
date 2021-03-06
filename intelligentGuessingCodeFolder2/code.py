# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bSu80QoBG2lEDtva9v3uS3KWVqH3LFS0
"""

import pandas as pd
import re

data = pd.read_csv('intelligentGuessingDataSet', encoding = "ISO-8859-1", index_col = 'rownum')

data = data.drop(axis = 1, columns = 'Comments')

data['firstname'] = data['firstname'].astype(str)
data['lastname'] = data['lastname'].astype(str)

if 'nan' in data['firstname'].values:
  idx = data[data['firstname'] == 'nan'].index.values
  for index in idx:
    for value in data['firstname'].values:
      if value in data['email'][index]:
        
        data['firstname'][index] = value
        break

      for value in data['lastname'].values:
        if value in data['email'][index]:
          data['firstname'][index] = value

if 'nan' in data['lastname'].values:
  idx = data[data['lastname'] == 'nan'].index.values
  for index in idx:
    for value in data['lastname'].values: 
      if value.replace(" ", "") in data['email'][index]:
        data['lastname'][index] = value
        break

      for value in data['firstname'].values:
        if value in data['email'][index]:
          data['lastname'][index] = value

data['lastname'] = data['lastname'].str.replace('\'\s', ' ', regex=True)
data['lastname'] = data['lastname'].str.replace('\'', '', regex=True)
data['lastname'] = data['lastname'].str.replace('-', ' ', regex=True)

data['firstname'] = data['firstname'].str.replace('\'\s', ' ', regex=True)
data['firstname'] = data['firstname'].str.replace('\'', '', regex=True)
data['firstname'] = data['firstname'].str.replace('-', '', regex=True)

for index, row in data.iterrows():
  row['Email Pattern'] = row['email'].split('@')[0].lower()

  row['Email Pattern'] = re.sub(str(row['firstname']).lower(),'<11>', row['Email Pattern'])
  row['Email Pattern'] = re.sub(str(row['lastname']).lower(), '<22>', row['Email Pattern'])

  last =  re.split('\s', row['lastname'])
  if len(last)>1:
    row['Email Pattern'] = re.sub(last[1].lower(), '<21>', row['Email Pattern'])
    row['Email Pattern'] = re.sub(last[0].lower(), '<20>', row['Email Pattern'])                              

  for i in range(len(row['firstname'])-1, 1, -1):
    row['Email Pattern'] = re.sub(row['firstname'][:i].lower(), '<11-f{}1>'.format(i), row['Email Pattern'], count = 1)

  row['Email Pattern'] = re.sub(str(row['firstname'])[0].lower(), '<1>', row['Email Pattern'], count = 1)

data.to_csv('problemset1_submission')

