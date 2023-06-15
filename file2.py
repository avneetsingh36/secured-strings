def receptionOfInfo():
    global receptionInfo
    with open('/path/to/intermediaryNode.txt', encoding= 'utf-8') as f:
        receptionInfo = f.read()
    print("Information from the intermediary node was accessed by the receieving Node and stored effctively!")
    print("Here is what will be saved in our data base: ")
    print(receptionInfo)