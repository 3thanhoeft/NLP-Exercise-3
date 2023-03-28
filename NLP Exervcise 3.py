# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:34:48 2023

@author: marse_nskbter
"""

# If you haven't downloaded Spacy before, use the following commands:
    # !pip install spacy
    # !python -m spacy download es_core_news_sm
    # !python -m spacy download en_core_web_sm
    # !python -m spacy download el_core_news_sm

# In order to use Spacy after downloading it, we need to import it. To be able
# to substitute the 'new lines' for spaces, we also need to import the 're' 
# module. 

import spacy
import re

def esp_pos_bigrams (text):
    '''This function returns the PoS bigrams from the text in Spanish that we 
    put as an input, without taking into acount those that have the tags 
    'SPACE', 'PUNCT', 'X' or 'SYM' in one of their items.'''
    with open(text, 'r', encoding='utf-8') as f:
        doc = f.read()
        
    nlp = spacy.load('es_core_news_sm')
    
    without_new_lines = re.sub('\n', ' ', doc)
    final_text = nlp(without_new_lines)
  
    pos_tags = []
    for tag in final_text:
        pos_tags.append((tag, tag.pos_))
  
    bigrams = []
    for x in range(len(pos_tags)-1):
        if pos_tags[x][1] != 'PUNCT' and pos_tags[x+1][1] != 'PUNCT' \
            and pos_tags[x][1] != 'SPACE' and pos_tags[x+1][1] != 'SPACE' \
                and pos_tags[x][1] != 'X' and pos_tags[x+1][1] != 'X' \
                    and pos_tags[x][1] != 'SYM' and pos_tags[x+1][1] != 'SYM':
            bigrams.append((pos_tags[x][1], pos_tags[x+1][1]))
    
    return bigrams

# To see the PoS bigrams in Spanish of each genre, save the .txt files in the 
# same directory as this script and execute the following lines:
    # esp_pos_bigrams ('esp_speech.txt')
    # esp_pos_bigrams ('esp_poetry.txt')
    # esp_pos_bigrams('esp_song.txt')
    # esp_pos_bigrams('esp_narrative.txt')

def eng_pos_bigrams (text):
    '''This function returns the PoS bigrams from the text in English that we 
    put as an input, without taking into acount those that have the tags 
    'SPACE', 'PUNCT', 'X' or 'SYM' in one of their items.'''
    with open(text, 'r', encoding='utf-8') as f:
        doc = f.read()
        
    nlp = spacy.load('en_core_web_sm')
    
    without_new_lines = re.sub('\n', ' ', doc)
    final_text = nlp(without_new_lines)
  
    pos_tags = []
    for tag in final_text:
        pos_tags.append((tag, tag.pos_))
  
    bigrams = []
    for x in range(len(pos_tags)-1):
        if pos_tags[x][1] != 'PUNCT' and pos_tags[x+1][1] != 'PUNCT' \
            and pos_tags[x][1] != 'SPACE' and pos_tags[x+1][1] != 'SPACE' \
                and pos_tags[x][1] != 'X' and pos_tags[x+1][1] != 'X' \
                    and pos_tags[x][1] != 'SYM' and pos_tags[x+1][1] != 'SYM':
            bigrams.append((pos_tags[x][1], pos_tags[x+1][1]))
    
    return bigrams

# To see the PoS bigrams in English of each genre, save the .txt files in the 
# same directory as this script and execute the following lines:
    # eng_pos_bigrams ('eng_speech.txt')
    # eng_pos_bigrams ('eng_poetry.txt')
    # eng_pos_bigrams('eng_song.txt')
    # eng_pos_bigrams('eng_narrative.txt')

def gre_pos_bigrams (text):
    '''This function returns the PoS bigrams from the text in Greek that we 
    put as an input, without taking into acount those that have the tags 
    'SPACE', 'PUNCT', 'X' or 'SYM' in one of their items.'''
    with open(text, 'r', encoding='utf-8') as f:
        doc = f.read()
        
    nlp = spacy.load('el_core_news_sm')
    
    without_new_lines = re.sub('\n', ' ', doc)
    final_text = nlp(without_new_lines)
  
    pos_tags = []
    for tag in final_text:
        pos_tags.append((tag, tag.pos_))
  
    bigrams = []
    for x in range(len(pos_tags)-1):
        if pos_tags[x][1] != 'PUNCT' and pos_tags[x+1][1] != 'PUNCT' \
            and pos_tags[x][1] != 'SPACE' and pos_tags[x+1][1] != 'SPACE' \
                and pos_tags[x][1] != 'X' and pos_tags[x+1][1] != 'X' \
                    and pos_tags[x][1] != 'SYM' and pos_tags[x+1][1] != 'SYM':
            bigrams.append((pos_tags[x][1], pos_tags[x+1][1]))
    
    return bigrams

# To see the PoS bigrams in Greek of each genre, save the .txt files in the 
# same directory as this script and execute the following lines:
    # gre_pos_bigrams ('gre_speech.txt')
    # gre_pos_bigrams ('gre_poetry.txt')
    # gre_pos_bigrams('gre_song.txt')
    # gre_pos_bigrams('gre_narrative.txt')


def bigram_frequency (bigrams_list):
    '''This function returns the PoS bigrams list that we put as an input and 
    returns it ordered by frequency.'''
    bigrams_count = {}
    for pair in bigrams_list:
        if pair in bigrams_count:
            bigrams_count[pair] +=1
        else:
            bigrams_count[pair] = 1
    word_count = ((value,key) for (key,value) in bigrams_count.items())
    frequency = sorted(word_count, reverse=True)
    return frequency

# In the following step, we assign into a variable the output that we get after
# applying the first function of 'x_pos_bigrams' (x being in each case the 
# language of the data) and afterwards using its output as an input for the 
# 'bigram_frequency' function.
esp_narrative = bigram_frequency(esp_pos_bigrams('esp_narrative.txt'))
esp_poetry = bigram_frequency(esp_pos_bigrams('esp_poetry.txt'))
esp_speech = bigram_frequency(esp_pos_bigrams('esp_speech.txt'))
esp_song = bigram_frequency(esp_pos_bigrams('esp_song.txt'))

eng_narrative = bigram_frequency(eng_pos_bigrams('eng_narrative.txt'))
eng_poetry = bigram_frequency(eng_pos_bigrams('eng_poetry.txt'))
eng_speech = bigram_frequency(eng_pos_bigrams('eng_speech.txt'))
eng_song = bigram_frequency(eng_pos_bigrams('eng_song.txt'))

gre_narrative = bigram_frequency(gre_pos_bigrams('gre_narrative.txt'))
gre_poetry = bigram_frequency(gre_pos_bigrams('gre_poetry.txt'))
gre_speech = bigram_frequency(gre_pos_bigrams('gre_speech.txt'))
gre_song = bigram_frequency(gre_pos_bigrams('gre_song.txt'))



def bigrams_percentages(frequency_list):
    '''This function takes a list of bigrams and their frequency of appearance
    and expresses such frequency as a percentage.'''
    total_sum = 0
    for pair in frequency_list:
        total_sum += pair[0]
    
    frequency_of_appearence = []
    for pair in frequency_list:
        percentage = round(pair[0] * 100 / total_sum, 2)
        frequency_of_appearence.append((percentage, pair[1]))
    return frequency_of_appearence

# In the following step, we assign into a variable the output of the function 
# 'bigrams_percentages', which turns the last list of bigrams and their
# frequency of appearance into a new list but with percentages in order to be 
# able to compare the results easily. 
percentage_esp_narrative = bigrams_percentages(esp_narrative)
percentage_esp_poetry = bigrams_percentages(esp_poetry)
percentage_esp_speech = bigrams_percentages(esp_speech)
percentage_esp_song = bigrams_percentages(esp_song)

percentage_eng_narrative = bigrams_percentages(eng_narrative)
percentage_eng_poetry = bigrams_percentages(eng_poetry)
percentage_eng_speech = bigrams_percentages(eng_speech)
percentage_eng_song = bigrams_percentages(eng_song)

percentage_gre_narrative = bigrams_percentages(gre_narrative)
percentage_gre_poetry = bigrams_percentages(gre_poetry)
percentage_gre_speech = bigrams_percentages(gre_speech)
percentage_gre_song = bigrams_percentages(gre_song)


# If you haven't downloaded this library, use the following command:
    # !pip install prettytable
    
from prettytable import PrettyTable

# First, we need to create the table for the Spanish data
esp_data = PrettyTable()
esp_data.field_names = ["Narrative", "Speech", "Poetry", "Song"]
esp_data.add_row(["DET + NOUN (15,48%)", "DET + NOUN (13,17%)", "DET + NOUN (18,85%)", "PRON + VERB (10,51%)"])
esp_data.add_row(["ADP + DET (8,6%)", "NOUN + ADP (6,92%)", "NOUN + ADP (10,77%)", "DET + NOUN (6,01%)"])
esp_data.add_row(["NOUN + ADP (7,31%)", "ADP + DET (6,7%)", "ADP + DET (9,62%)", "PRON + PRON (5,71%)"])
esp_data.add_row(["VERB + ADP (6,24%)", "ADP + NOUN (6,03%)", "ADP + NOUN (6,92%)", "ADV + VERB (3,3%)"])
esp_data.add_row(["PRON + VERB (4,95%)", "NONUN + ADJ (3,79%)", "NOUN + ADJ (3,85%)", "VERB + SCONJ (3,0%)"])

# We also set the title and style of the table.
esp_data.title = "SPANISH RESULTS"
esp_data.align = "c"
esp_data.hrules = 3
esp_data.vrules = 1

# And finally, we print the table
print(esp_data, '\n')


# We do exactly the same with our English and Greek data. 
eng_data = PrettyTable()
eng_data.field_names = ["Narrative", "Speech", "Poetry", "Song"]
eng_data.add_row(["PRON + VERB (8,18%)", "PRON + VERB (7,26%)", "DET + NOUN (6,95%)", "PRON + VERB (10,84%)"])
eng_data.add_row(["DET + NOUN (7,24%)", "NOUN + ADP (5,77%)", "PRON + NOUN (5,76%)", "VERB + PRON (8,4%)"])
eng_data.add_row(["VERB + PRON (5,37%)", "DET + NOUN (5,56%)", "VERB + PRON (5,52%)", "PRON + AUX (5,42%)"])
eng_data.add_row(["ADP + DET (4,67%)", "ADP + DET (3,85%)", "PRON + VERB (4,8%)", "PRON + PRON (5,15%)"])
eng_data.add_row(["NOUN + ADP (4,44%)", "ADJ + NOUN (3,85%)", "ADP + PRON (4,08%)", "DET + NOUN (5,15%)"])

eng_data.title = "ENGLISH RESULTS"
eng_data.align = "c"
eng_data.hrules = 3
eng_data.vrules = 1

print(eng_data, '\n')


gre_data = PrettyTable()
gre_data.field_names = ["Narrative", "Speech", "Poetry", "Song"]
gre_data.add_row(["DET + NOUN (9,45%)", "DET + NOUN (12,69%)", "DET + NOUN (11,11%)", "DET + NOUN (4,57%)"])
gre_data.add_row(["NOUN + PRON (4,2%)", "ADJ + NOUN (6,46%)", "ADJ + NOUN (6,17%)", "VERB + NOUN (4,06%)"])
gre_data.add_row(["DET + ADJ (4,2%)", "VERB + DET (6,24%)", "NOUN + NOUN (5,68%)", "ADP + NOUN (3,81%)"])
gre_data.add_row(["ADP + NOUN (4,2%)", "AUX + VERB (5,57%)", "NOUN + DET (4,94%)", "NOUN + ADV (3,3%)"])
gre_data.add_row(["AUX + VERB (3,57%)", "DET + ADJ (4,9%)", "NOUN + PRON (4,44%)", "NOUN + PRON (3,05%)"])

gre_data.title = "GREEK RESULTS"
gre_data.align = "c"
gre_data.hrules = 3
gre_data.vrules = 1

print(gre_data, '\n')

