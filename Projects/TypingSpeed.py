import time

string = 'Python is A Programming Language!'
wordCount = len(string.split())

while input("Enter 'yes' when you are ready: ") == 'yes':
    print(string)

    startTime = time.time()
    
    inputText = input("Enter the Phrase: ")
    endTime = time.time()

    # It shows dictionary then count the words exist in both strings
    acc = len(set(inputText.split()) & set(string.split()))
    acc = acc / wordCount
    timeTaken = round((endTime - startTime), 2)
    wordPM = round(((wordCount * 60) / timeTaken), 2)

    print(wordPM, str(acc * 100) + '%', str(timeTaken) + ' secs')