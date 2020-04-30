
def foreign_exchange_cal(ammount):
    mex_to_col = 145.97

    return mex_to_col * ammount

def run():

    print('''
----------------------
C A L C U L A D O R A
----------------------

Convierte de pesos mexas a pesos colombiano

    ''')
    ammount = float(input('¿Cual es la cantidad a convertir? '))

    result = foreign_exchange_cal(ammount)
    print('${} pesos mexas son ${} pesos colombianos'.format(ammount,result))
    

if __name__ == "__main__":
    run()