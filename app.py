from typing import List, Any, Union, Tuple

import pandas as pd
from sklearn import tree
from sklearn import preprocessing

rooms = 0
size = 0
floor = 0
district = ''
dataset = []
prices = []
count = 0

df = pd.read_csv('http://djo.com.pl/databases/homdbcsv/poz.csv')
df.drop(['Id', 'Description'], axis=1, inplace=True)

while True:
  try:
     rooms = int(input('Podaj ilośc pokoi: '))
  except ValueError:
     print("Musisz podac liczbę!")
     continue
  else:
     break

while True:
  try:
     size = int(input('Podaj wielkośc w metrach: '))
  except ValueError:
     print("Musisz podac liczbę!")
     continue
  else:
     break

while True:
  try:
     floor = int(input("Ktore piętro ?  "))
  except ValueError:
     print("Musisz podac liczbę!")
     continue
  else:
     break

district = input("Jaka dzielnica ? ")

print('\n\n\nWprowadzone dane: \n')
print('Pokoje: %d' % (rooms))
print('Wielkośc mieszkania: %d' % (size))
print('Piętro: %d' % (floor))
print('Dzielnica: %s' % (district))
print('\nObliczam!')

districtEx = ['antoninek', 'dębiec', 'zieliniec', 'kobylepole', 'chartowo', 'kotowo', 'główna', 'głuszyna', 'górczyn',
              'jeżyce', 'junikowo', 'krzesiny', 'krzyżowniki', 'smochowice', 'morasko', 'naramowice', 'ogrody',
              'śródka', 'piątkowo', 'podolany', 'rataje', 'sołacz', 'stare miasto', 'winogrady',
              'starołęka', 'garbary', 'grunwald', 'strzeszyn', 'szczepankowo', 'świerczewo', 'łazarz', 'umultowo', 'warszawskie',
              'wilda', 'winiary', 'wola', 'żegrze', 'zawady']

districtFlat = []
while count <= 4999:
    districtFlat.append([df.iloc[count][4]])
    querywords = str(districtFlat[count]).lower().split()
    resultwords = [word for word in querywords if word.lower() in districtEx]
    result = " ".join(resultwords)
    districtFlat[count] = result
    count += 1

encoder = preprocessing.LabelEncoder()
encoder.fit(districtFlat)

count = 0
while count <= 4999:
    dataset.append([df.iloc[count][1], int(df.iloc[count][2]), df.iloc[count][3], int(encoder.transform([districtFlat[count]]))])
    prices.append(df.iloc[count][0])
    count += 1

clf = tree.DecisionTreeClassifier()
clf.fit(dataset, prices)

price = clf.predict([[rooms, size, floor, int(encoder.transform([district.lower()]))]])

print('\nPrzewidywana cena mieszkania to: %d' % (price))
