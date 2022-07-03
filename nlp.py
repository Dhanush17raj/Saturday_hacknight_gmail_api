
from drafts import gmail_create_draft
import string

stop_words = open("stopwords.txt", encoding="utf-8").read()

from collections import Counter

import matplotlib.pyplot as plt
kh = input("Enter the content for the email: ")
to = input("Enter the recipient mail id: ")
fro_m = input("Enter your email id: ")
sub = input('Enter the subject of the email: ')
gmail_create_draft(to, fro_m, sub, kh)

sent = kh
lower_case = sent.lower()

cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

tokenized_words = cleaned_text.split()

final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)


emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

w = Counter(emotion_list)
print(" The emotion of the mail is ", w)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()



