"""
###` Create a Serialized dict of frequency of words in the file. And from given list of words, using serialized dict show word count.

* List of word will be given
word_list = ['alice', 'wonder', 'natural']
"""
import json
file="day_10_file_handling/q_05.json"
strings = """Alice was beginning to get very tired of sitting by her sister
            on the bank, and of having nothing to do:  once or twice she had
            peeped into the book her sister was reading, but it had no
            pictures or conversations in it, `and what is the use of a book,'
            thought Alice `without pictures or conversation?'

            So she was considering in her own mind (as well as she could,
            for the hot day made her feel very sleepy and stupid), whether
            the pleasure of making a daisy-chain would be worth the trouble
            of getting up and picking the daisies, when suddenly a White
            Rabbit with pink eyes ran close by her.

            There was nothing so VERY remarkable in that; nor did Alice
            think it so VERY much out of the way to hear the Rabbit say to
            itself, `Oh dear!  Oh dear!  I shall be late!'  (when she thought
            it over afterwards, it occurred to her that she ought to have
            wondered at this, but at the time it all seemed quite natural);
            but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-
            POCKET, and looked at it, and then hurried on, Alice started to
            her feet, for it flashed across her mind that she had never
            before seen a rabbit with either a waistcoat-pocket, or a watch to
            take out of it, and burning with curiosity, she ran across the
            field after it, and fortunately was just in time to see it pop
            down a large rabbit-hole under the hedge."""
with open(file,'w') as f:
    dict_freq={}
    for word in strings.split():
        word=word.lower()
        new_word=""
        for letter in word:
            if letter.isalpha():
                new_word+=letter
        if new_word:    
            if new_word in dict_freq:
                dict_freq[new_word]+=1
            else:
                dict_freq[new_word]=1
    json.dump(dict_freq,f, indent=4)

with open(file,'r') as f:
    dict_output=json.load(f)

word_list = ['alice', 'wonder', 'natural']
for word in word_list:
    if word in dict_output:
        print(f"{word} freqency in given string is : {dict_output[word]} ")
    else:
        print(f"{word} not present in dictionary")


        
