# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:44:33 2021

@author: ASUS
"""

import PyPDF2
pdfFileObj = open('Demo.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)

search_word = "python"
search_word_count = 0

for pageNum in range(4, 6):
    pageObj = pdfReader.getPage(pageNum)
    text = pageObj.extractText().encode('utf-8')
    search_text = text.lower().split()
    for word in search_text:
        if search_word in word.decode("utf-8"):
            search_word_count += 1
        
print("The word {} was found {} times".format(search_word, search_word_count))