#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

phone_regex = re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')
email_regex = re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}')

with open('examples.txt', 'r') as f:
    for line in f:
        phone_matches = phone_regex.findall(line)
        for match in phone_matches:
            print(match)

        email_matches = email_regex.findall(line)
        for match in email_matches:
            print(match)


# In[ ]:




