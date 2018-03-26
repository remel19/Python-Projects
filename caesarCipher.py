#caesar cipher
import string


upperList = list(string.ascii_uppercase)
loweList = list(string.ascii_lowercase)

def getInstruction():
    print('Caesar ceipher.\n'.upper())
    while True:
        encryptOrDecrypt = input('Would you like to Encrypt(e) or Decrypt(d)? ')
        if encryptOrDecrypt.lower() == 'encrypt' or encryptOrDecrypt.lower() == 'e':
            encryptMessage()
            break
        elif encryptOrDecrypt.lower() == 'decrypt' or encryptOrDecrypt.lower() == 'd':
            decryptMessage()
            break
        else:
            print('\nPlease choose either encrypt or decrypt.')
            continue

def getMessage():
    message = input('Please enter the message: ')
    return message

def getKey():
    while True:
        try:
            key = int(input('Please enter the key of this message: '))
            return key
        except ValueError:
            print('Invalid message, please enter number as a key.')

def encryptMessage():
    print('\n**********Encrypt**********\n')
    message = getMessage()
    key = getKey()
    print('\nEncrypting.....\n')
    encryptedMessage = ''
    for char in message:
        if char.isupper():
            upperIndex = ( (upperList.index(char) + key) % 26 )  
            encryptedMessage += encryptedMessage.join(upperList[upperIndex])
        elif char.islower():
            lowerIndex = ( (loweList.index(char) + key) % 26 )
            encryptedMessage += encryptedMessage.join(loweList[lowerIndex])
        else:
            encryptedMessage += encryptedMessage.join(char)
    print('Encrypted message: ' + encryptedMessage + '\n')

def decryptMessage():
    print('\n**********Decrypt**********\n')
    message = getMessage()
    key = getKey()
    print('\nDecrypting.....\n')
    decryptedMessage = ''
    for char in message:
        if char.isupper():
            upperIndex = ( (upperList.index(char) - key) % 26 )  
            decryptedMessage += decryptedMessage.join(upperList[upperIndex])
        elif char.islower():
            lowerIndex = ( (loweList.index(char) - key) % 26 )
            decryptedMessage += decryptedMessage.join(loweList[lowerIndex])
        else:
            decryptedMessage += decryptedMessage.join(char)
    print('Decrypting: ' + decryptedMessage + '\n')

def __init__():
    getInstruction()
    

__init__()
