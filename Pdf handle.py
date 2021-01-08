# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:44:33 2021

@author: ASUS
"""
import PyPDF2 as doc

inputfile = input('Enter the input file name.: ')
try:
    myfile = open(inputfile, 'rb') # Read the pdf
    pdf_read = doc.PdfFileReader(myfile)  # object for reading pdf
    
    print('The total page number.:\t',pdf_read.numPages) # print total number of page.
    print('The Doc info: \n\t',pdf_read.getDocumentInfo())
    
    option = input('Do you want a Separate file(yes/no) : ')
     
    str = "" # creat a empty string. And we store the content of pdf later.
    
   
    if option == 'yes':
        outputfile = input('Enter the file name of output file.: ')
        x = int(input('Enter the starting page.: '))
        y = int(input('Enter the end page.: '))
        newfile = open(outputfile, 'wb')  # write a pdf file
        pdf_write = doc.PdfFileWriter()  # object for writing the pdf
        
        for j in range(x,y):
            page = pdf_read.getPage(j)
            pdf_write.addPage(page)
        pdf_write.write(newfile)
        
        
    elif option == 'no':
        x = int(input('Enter the starting page.: '))
        y = int(input('Enter the end page.: '))
        for i in range(x,y): # The loop runupto 6 And indexing start form 0
            page = pdf_read.getPage(i) 
            str += page.extractText()
            
        print('The page content : ')
        print(str)
     
        
    else:
        print('Enter the right option: ')
    
    ######################################
    ### word search############
    print('<-----Word searcher------->')
    search_word = input("Enter the word you want to search .: ")
    x = int(input('Enter the starting range.: '))
    y = int(input('Enter the end range.: '))
    print('Processing...')
    search_word_count = 0
    for pageNum in range(x, y):
        pageObj = pdf_read.getPage(pageNum)
        text = pageObj.extractText().encode('utf-8')
        search_text = text.lower().split()
        for word in search_text:
            if search_word in word.decode("utf-8"):
                search_word_count += 1
            
    print("The word '{}' was found {} times in between page {} and {}".format(search_word, search_word_count,x,y))
            
    newfile.close()
    myfile.close()
    
except:
    print('Enter the right file name.')
    
