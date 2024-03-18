def readBook() ->str:
    with open("./books/Frankenstein.txt") as f:
        content = f.read()

    return content

def countLetter(word) -> int:
    newWord = word.lower()
    char = {}
    for c in newWord:
        if c in char:
            char[c] += 1
        else:
            char[c] = 1


    return char

def sortLetter(data):

    newLetter = dict(sorted(data.items()))
    return newLetter


def main() -> int:
    
    content = readBook()

    cont_count = len(content.split())    
    print(content)
    print(cont_count)

    print(countLetter(content))
    
    print(sortLetter(countLetter(content)))
    return 0

if __name__ == '__main__':
    SystemExit(main())