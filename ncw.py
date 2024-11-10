text = None
cuss_words = ("hi", "im", "dory")

def input_text():
    global text
    text = input("Enter your text: ")
    if any(word in text for word in cuss_words):  
        print("This text was censored because of cuss words detected in it. Family friendly only!")
        text = "You wrote: cuss words"
        print(text)

if __name__ == "__main__":
    input_text() 
