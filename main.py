def main():
    book_path = "github.com/Prot2099/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    words = sum(1 for word in text.split())
    #print(words)

    slownik = {}
    litery = set(text.lower())
    for znak in text.lower():
        if znak in slownik:
            slownik[znak] += 1
        else:
            slownik[znak] = 1
    #print(slownik)
    for k, v in sorted(slownik.items()):
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")
   # litery = {litera: sum(litera) for litera in text}
    #print(litery)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()