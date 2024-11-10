# ncw
I created a python module that bans cuss words! It's got its own text input, so when imported, you only need to add the line: ncw.input_text(). It's available via pip!

It's full name is NoCussWords, but it's shortened as ncw - easier to remember and to use. The command is pip install ncw, because ncw.py is the main file. Here are some usage examples:

import ncw  

def wordrepeater():                                              ___________
    while True:                                                            |
        ncw.input_text()                                                   |
        if ncw.text == "You wrote: cuss words":                            |
            print("Please enter your text again.")                         |
            continue                                                       |
        number = int(input("Enter a number of repeats: "))                  ------ The Example Python Code
        for i in range(number):                                            |
            print(i + 1, ncw.text)                                         |
        break                                                              |
                                                                           |
wordrepeater()                                                   ___________

I'm gonna break it down. ncw.input_text() function is the function that allows you to type in any text. The module won't work if the script got it's own input function, because it's coded to detect cuss words in 
the input text function of the module. The 11th line is needed in order for the module to work correctly. In the module itself, there are lines that specifically say that if cuss words are detected, change "text" to "You wrote: cuss words". So, the 11th line corresponds to the module itself and continues with the loop IF cuss words are detected. The "for" command is just for printing the numbers of how many times the word is repeated.
