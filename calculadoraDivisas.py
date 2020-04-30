def MXN(ammount,convertCoin):
    MXNToUSD = 20
    MXNToCOL = 145.97
    DLS = "dolares americanos"

    if convertCoin == 2:
        r = MXNToUSD * ammount
        return r , DLS
    elif convertCoin == 3:
        r = MXNToCOL * ammount
        return r , "pesos colombianos"
    else:
        return "Comando no valido"
    
def USD(ammount,convertCoin):
    USDToMXN = 1
    USDToCOL = 3417.35

    if convertCoin == 1:
        r = USDToMXN * ammount
        return r , "pesos mexicanos"
    elif convertCoin == 3:
        r = USDToCOL * ammount
        return r , "pesos colombianos"
    else:
        return "Comando no valido"

def COL(ammount, convertCoin):
    COLToMXN = .0068
    COLToUSD = .00029

    if convertCoin == 1:
        r = COLToMXN * ammount
        return r , "pesos mexicanos"
    elif convertCoin == 2:
        r = COLToUSD * ammount
        return r , "dolares americanos"
    else:
        return "Comando no valido"

def run():
    actualCoin = int(input('''C O N V E R T I D O R  D E  D I V I S A S
    ¿Cuál es tu moneda actual?
    [1]MXN
    [2]USD
    [3]COL
    => '''))

    convertCoin = int(input('''
    ¿A que moneda quieres convertir?
    [1]MXN
    [2]USD
    [3]COL
    => '''))

    ammount = int(input('''
    ¿Cual es la cantidad que quieres convertir?
    => '''))

    if actualCoin == 1:
        result = MXN(ammount,convertCoin)
        print('${} pesos mexicanos son ${}'.format(ammount,result))
    elif actualCoin == 2:
        result = USD(ammount,convertCoin)
        print('${} dolares americanos son ${}'.format(ammount,result))
    elif actualCoin == 3:
        result = COL(ammount,convertCoin)
        print('${} pesos colombianos son ${}'.format(ammount,result))

if __name__ == '__main__':
    run()