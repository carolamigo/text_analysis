
# coding: utf-8

# In[ ]:


#adapted from http://nealcaren.web.unc.edu/an-introduction-to-text-analysis-with-python-part-3/


# ## Retrieving dictionary

# In[26]:


from __future__ import division
import urllib
import csv


# In[27]:


files=['negative.txt','positive.txt']
path='http://www.unc.edu/~ncaren/haphazard/'
for file_name in files:
    urllib.urlretrieve(path+file_name,file_name)


# ## Retrieving file with cleaned full text

# In[28]:


filepath = '/Users/camigo/Documents/text_analysis/chapters_edited_fulltext.txt'

file = open(filepath, "r") 
chapters_edited_fulltext = file.read() 

chapters_edited_fulltext_split = chapters_edited_fulltext.split("\n")

len(chapters_edited_fulltext_split)


# In[40]:


filepath = '/Users/camigo/Documents/text_analysis/chapters_edited.txt'

file = open(filepath, "r") 
chapters_edited_fulltext = file.read() 

chapters_edited_fulltext_split = chapters_edited_fulltext.split("\n")

len(chapters_edited_fulltext_split)


# ## Loading dictionaries with positive and negative words

# In[29]:


pos_sent = open("positive.txt").read()
positive_words=pos_sent.split('\n')
positive_counts=[]

neg_sent = open('negative.txt').read()
negative_words=neg_sent.split('\n')
negative_counts=[]


# ## Counting positive and negative words

# In[38]:


for chapter in chapters_edited_fulltext_split:
    positive_counter=0
    negative_counter=0
    
    words=chapter.split(' ')
    word_count=len(words)
    for word in words:
        if word in positive_words:
            positive_counter=positive_counter+1
        elif word in negative_words:
            negative_counter=negative_counter+1
        
    positive_counts.append(positive_counter/word_count)
    negative_counts.append(negative_counter/word_count)

output=zip(chapters_edited_fulltext_split,positive_counts,negative_counts)

writer = csv.writer(open('fulltext_sentiment.csv', 'wb'))
writer.writerows(output)

