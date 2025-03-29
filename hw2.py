# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 13:14:44 2025

@author: USER
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

word_count = {}

with open('hw2_data.txt', 'r') as inputfile:
    for line in inputfile:
        word = line.strip()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
unique_word_count = len(word_count)
print("不重複的單字數量:%d" %unique_word_count)

sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_word_count:
    print("%s:%d" %(word, count))

words, counts = zip(*sorted_word_count) 

plt.figure(figsize=(max(12, len(word) * 0.3), 6))  
plt.bar(words, counts)

# 旋轉 x 軸標籤，確保不重疊
plt.xticks(rotation=90, ha="right", fontsize=8) 
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Word Frequency Statistics")


plt.savefig('output.png')
