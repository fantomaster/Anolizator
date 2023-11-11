import os

text = input("Введите текст: ")
text = text.lower()

punctuations = [".", ",", "!", "?"]

text = text.replace(punctuations[0], '')
text = text.replace(punctuations[1], '')
text = text.replace(punctuations[2], '')
text = text.replace(punctuations[3], '')

words = text.split()

clear = lambda: os.system('cls')

print("Количество разных слов:", len(set(words)))

word_frequency = {}

for word in words:
  # Подсчет частоты слов
  if word in word_frequency:
    word_frequency[word] += 1
  else:
    word_frequency[word] = 1

print("Частота слов:")
for word, frequency in word_frequency.items():
  print(f"{word}: {frequency}")
