# Faltas Biosar #

# import only system from os 
from os import system, name 
# import sleep to show output for some time period 
from time import sleep
# importando módulos
import csv
import pandas as pd

def main():
    print("\n**** Biosar Inverters Fault ****")

    # define our clear function 
    def clear(): 
        # for windows 
        if name == 'nt': 
             _ = system('cls')

    # Import dataset into workspace
    df = pd.read_excel('Errosefaltas.xlsx')

    # Reading User's input
    print("\n P - Pirapora \n G - Guimarania")
    plant = input("Digite a letra referente a planta: ")
    plant = str.lower(plant)
    bitText = input("Cole aqui o texto completo: ")
    bitText = str(bitText)

    # Replacing text received
    bitText = bitText.replace('register:', '')

    if plant == 'p':
        plant = 'Pirapora'
    elif plant == "g":
         plant = 'GUI'
    else:
        print("Planta desconhecida!")
    # colocar um fim para o script ou retorno ao inicio #

    # split fault text
    fault, register = bitText.split(' ', 1)

    # Conveting Bit format to DataFrame string
    if register == '0000000000000001':
        register = 'B0'
    elif register == '0000000000000010':
         register = 'B1'
    elif register == '0000000000000100':
         register = 'B2'
    elif register == '0000000000001000':
         register = 'B3'
    elif register == '0000000000010000':
         register = 'B4'
    elif register == '0000000000100000':
         register = 'B5'
    elif register == '0000000001000000':
         register = 'B6'
    elif register == '0000000010000000':
         register = 'B7'
    elif register == '0000000100000000':
         register = 'B8'
    elif register == '0000001000000000':
         register = 'B9'
    elif register == '0000010000000000':
         register = 'B10'
    elif register == '0000100000000000':
         register = 'B11'
    elif register == '0001000000000000':
         register = 'B12'
    elif register == '0010000000000000':
         register = 'B13'
    elif register == '0100000000000000':
         register = 'B14'
    elif register == '1000000000000000':
         register = 'B15'
    else:
        print("Bit desconhecido!")
        
        # sleep for 2 seconds after printing output 
        sleep(2)
        # call clear function 
        clear()
        # Restart process
        return main()
    
    q = str ("Planta == '{0}' & Falta == '{1}'& Bit == '{2}'").format(plant, fault, register)
    
    # trying to get the values
    # filtering with query method
    df1 = df.query(q)

    #Printing fault Message
    print(df1.Mensagem.to_string(index=False))

    # sleep for 2 seconds after printing output 
    sleep(10)
    return main()

if __name__ == "__main__":
    main()