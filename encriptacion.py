KEYS = {
'a':'z',
'b':'y',
'c':'x',
'd':'w',
'e':'v',
'f':'u',
'g':'t',
'h':'s',
'i':'r',
'j':'q',
'k':'p',
'l':'o',
'm':'ñ',
'n':'n',
'ñ':'m',
'o':'l',
'p':'k',
'q':'j',
'r':'i',
's':'h',
't':'g',
'u':'f',
'v':'e',
'w':'d',
'x':'c',
'y':'b',
'z':'a'

}

def cypher(message):
    words = message.split(' ')
    cypher_message = []

    for word in words:
        cypher_word = ''
        for letter in word:
            cypher_word += KEYS[letter]
        cypher_message.append(cypher_word)

    return ' '.join(cypher_message)

def decipher(message):
    words = message.split('')
    decipher_message = []

    for word in words:
        decipher_word = ''
        for letter in word:
            decipher_word += KEYS[letter.values]

def run():
    while True:
        command = str(input('''
        INGRESE EL COMANDO:

        [c]ifrar
        [d]ecifrar
        [s]alir
        '''))

        if command is 'c' or 'C':
            message = str(input('Ingrese el mensaje: '))
            cifrado_de_mensaje = cypher(message)
            print(cifrado_de_mensaje)
            
        if command is 'd' or 'D':
            message = str(input('Ingrese el mensaje cifrado: '))
            decifrado_de_mensaje = decipher(message)
            print(decifrado_de_mensaje)

        if command is 's' or 'S':
            break
        
        else:
            print('No se enuentra el comando {}'.format(command))



if __name__ == "__main__":
    print('MENSAJES SECREEETOS')
    run()