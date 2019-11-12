# Biosar Faults Translater #

import sys
import pathlib
import numpy as np
# import only system from os 
from os import system, name 
# import sleep to show output for some time period 
from time import sleep
# import DataFrame
from pandas import (DataFrame, read_excel)

# define clear function 
def clear(): 
     # for windows 
     if name == 'nt': 
          _ = system('cls')

def bit(y):
    if y == '0000000000000000':
       print('Sem registro de faltas')
       sleep(2)
       return main()
    elif y == '0000000000000001':
        y = 'B0'
        return(y)
    elif y == '0000000000000010':
        y = 'B1'
        return(y)
    elif y == '0000000000000100':
        y = 'B2'
        return(y)
    elif y == '0000000000001000':
        y = 'B3'
        return(y)
    elif y == '0000000000010000':
        y = 'B4'
        return(y)    
    elif y == '0000000000100000':
        y = 'B5'
        return(y)
    elif y == '0000000001000000':
        y = 'B6'
        return(y)    
    elif y == '0000000010000000':
        y = 'B7'
        return(y)
    elif y == '0000000100000000':
        y = 'B8'
        return(y)
    elif y == '0000001000000000':
        y = 'B9'
        return(y)
    elif y == '0000010000000000':
        y = 'B10'
        return(y)
    elif y == '0000100000000000':
        y = 'B11'
        return(y)
    elif y == '0001000000000000':
        y = 'B12'
        return(y)
    elif y == '0010000000000000':
        y = 'B13'
        return(y)
    elif y == '0100000000000000':
        y = 'B14'
        return(y)
    elif y == '1000000000000000':
        y = 'B15'
        return(y)
    else:
          print("Bit desconhecido!")
          # sleep for 2 seconds after printing output 
          sleep(2)
          # call clear function 
          clear()
          # Restart process
          return main()

def main():
    
    file_path: str = pathlib.Path(__file__).parent.__str__() + "//erros_faltas.xlsx"
    
    print("\n**** Biosar Fault Translater****")
    print(" * by Eliezer Nascimento * ")

    ## Pedir para o usuário digitar algo e, ai sim, executar a lógia de obtenção da mensagem relacionada à falta
    print("\n N - Não iniciou \n P - Parou")
    stat = input("A planta não iniciou ou parou? ")
    stat = str.lower(stat)
    if (stat == "n"):
        stat = "Não iniciou"
    elif (stat == "p"):
        stat = "Parou"
    else:
        print("Vamos lá! Nos deixe saber se planta não iniciou ou parou.")
        # sleep for 2 seconds after printing output 
        sleep(2)
        # call clear function 
        clear()
        # Restart process
        return main()
    
    inv_all = input("Cole o título do inversor aqui: ")
    inv_all = str.lower(inv_all)
    if (inv_all.startswith("p",9,10) == True):
        plant = 'Pirapora'
        inverter = ' '.join(inv_all.split()[1:2])
        inverter = inverter.replace('-inverter', '')#COMO COLOCAR ISSO DENTRO DE UM DEF() E FAZER COM QUE AS VARIÁVEIS SEJAM GLOBAIS?
        inverter = str.upper(inverter)
    elif (inv_all.startswith("gui",9,12) == True):
        plant = 'GUI'
        inverter = ' '.join(inv_all.split()[1:2])
        inverter = inverter.replace('-inverter', '')#COMO COLOCAR ISSO DENTRO DE UM DEF() E FAZER COM QUE AS VARIÁVEIS SEJAM GLOBAIS?
        inverter = str.upper(inverter)
    else:
        print('Você não digitou uma planta válida!')
        # sleep for 2 seconds after printing output 
        sleep(2)
        # call clear function 
        clear()
        # Restart process
        return main()

    if (plant == "p" or plant == "g"):

        bitText = input("Cole aqui o texto completo: ")
        bitText = str(bitText)
        if bitText.startswith("Fault") | bitText.startswith("Warning") | bitText.startswith("Status"):
            # Replacing text received
            bitText = bitText.replace('register:', '')
            
            # split fault text
            fault, register = bitText.split(' ', 1)
            
            q = str ("Planta == '{0}' & Falta == '{1}'& Bit == '{2}'").format(plant, fault, bit(register))
            # trying to get the values and
            # filtering with query method
            df_aux: DataFrame = read_excel(file_path)
            result_query: DataFrame = df_aux.query(q)

            if (plant == "Pirapora"):
                print(" Inverter", inverter, stat, " \n", result_query.Mensagem.to_string(index=False)) #Printing fault Message
            elif (plant == "GUI"):
                print(" Inverter", inverter, stat, " \n", result_query.Mensagem.to_string(index=False)) #Printing fault Message
            else:
                print("Não foi possível identificar o nome da falta.\n Tente novamente por favor. \n Obrigado!")
            sleep(10)
            return main()
        else:
            print("O texto inserido não é válido!")
            # sleep seconds after printing output
            # call clear function 
            sleep(3)
            clear()
            return main()
    else:
        print("Você não digitou uma planta válida!")
        # call clear function
        # sleep seconds after printing output
        sleep(3)
        clear()
        # Restart process
        return main()    

if __name__ == "__main__":
    main()