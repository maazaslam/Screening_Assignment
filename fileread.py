def convertText(fileLocation, text):
    with open(fileLocation, 'r') as file:
        data = file.read()
        
    data = data.replace(text, 'screening')

    with open(fileLocation, 'w') as file:
        file.write(data)

if __name__ =='__main__':
    file = "./example.txt"
    text = 'placement'

    convertText(fileLocation=file, text=text)