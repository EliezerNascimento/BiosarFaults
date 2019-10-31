# Biosar Faults Translater #

# import only system from os 
from os import system, name 
# import sleep to show output for some time period 
from time import sleep
# import DataFrame
from pandas import DataFrame

# define clear function 
def clear(): 
     # for windows 
     if name == 'nt': 
          _ = system('cls')

def idplant(x):
         x = str.lower(x)
         if x == 'p':
               x = 'Pirapora'
               return(x)
         elif x == "g":
               x = 'GUI'
               return(x)
         else:
               print("Planta desconhecida!")
               # sleep for 2 seconds after printing output 
               sleep(2)
               # call clear function 
               clear()
               # Restart process
               return main()

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

pir_df = DataFrame({'Planta':['Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora',
                                 'Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora',
                                 'Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora',
                                 'Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora',
                                 'Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora',
                                 'Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora',
                                 'Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora',
                                 'Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora',
                                 'Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora',
                                 'Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora',
                                 'Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora',
                                 'Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora',
                                 'Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora','Pirapora',
                                 'Pirapora'],
                     'Falta':['Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1',
                              'Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2',
                              'Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3',
                              'Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4',
                              'Warning1','Warning1','Warning1','Warning1','Warning1','Warning1','Warning1','Warning1','Warning1','Warning1','Warning1','Warning1','Warning1',
                              'Warning1','Warning1','Warning1','Warning2','Warning2','Warning2','Warning2','Warning2','Warning2','Warning2','Warning2','Warning2','Warning2',
                              'Warning2','Warning2','Warning2','Warning2','Warning2','Warning2','Warning3','Warning3','Warning3','Warning3','Warning3','Warning3','Warning3',
                              'Warning3','Warning3','Warning3','Warning3','Warning3','Warning3','Warning3','Warning3','Warning3','Status1','Status1','Status1','Status1',
                              'Status1','Status1','Status1','Status1','Status1','Status1','Status1','Status1','Status1','Status1','Status1','Status1','Status2','Status2',
                              'Status2','Status2','Status2','Status2','Status2','Status2','Status2','Status2','Status2','Status2','Status2','Status2','Status2','Status2'],
                      'Bit':['B0','B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','B12','B13','B14','B15','B0','B1','B2','B3','B4','B5',
                             'B6','B7','B8','B9','B10','B11','B12','B13','B14','B15','B0','B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11',
                             'B12','B13','B14','B15','B0','B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','B12','B13','B14','B15','B0','B1',
                             'B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','B12','B13','B14','B15','B0','B1','B2','B3','B4','B5','B6','B7','B8',
                             'B9','B10','B11','B12','B13','B14','B15','B0','B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','B12','B13','B14',
                             'B15','B0','B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','B12','B13','B14','B15','B0','B1','B2','B3','B4','B5',
                             'B6','B7','B8','B9','B10','B11','B12','B13','B14','B15'],
                      'Mensagem':['ECAT operation fault','FPGA version wrong','PIB watchdog fault','DC-Link overvoltage','Float controller fault',
                                  'DC-Link short circuit','Pole grounding','Not used','IGBT VCE desaturation fault','Not used','IGBT feedback fault',
                                  'Not used','Not used','Not used','Not used','Not used','PIB internal power supply','PIB measurement connector','Not used',
                                  'PIB amplifier connection','PIB terminal supply','Current clipping timeout','Short circuit','Not used',
                                  'Heat sink over-temperature','24V terminal supply short circuit','Fieldbus connection fault',
                                  'Battery synchronisation fault','Short-Circuit-To-Earth','DC-link under-voltage','Not used',
                                  'Not used','Line voltage fault','Line voltage measurement','AC-Circuit breaker tripped',
                                  'Feedback AC circuit breaker','Precharging failed','Line filter','Feedback discharging contactor',
                                  'Feedback DC circuit breaker','Amplifier board contactor','DC current direction fault (reverse Idc)',
                                  'UPS fault','Feedback PV short circuit breaker','Not used','Not used','Not used','Not used',
                                  'Heat sink temperature measurement','Heat sink under-temperature','External fan','Power electronics cubicle fan',
                                  'Line inductor fan','Cooling water over-temperature','Cooling water pressure fault','Cooling water pump fault',
                                  'Water heating/cooling fault','Power electronics cubicle over-temperature','Line inductor cubicle over-temperature',
                                  'MV Transformer fault','Isolation fault','Not used','Auxiliary supply fault','Fluid cooling system fault',
                                  'Heat sink over-temperature','Earth current','Line under voltage','Cooling water over-temperature',
                                  'Cooling water pressure','Water pressure sensor','Water heating','Fuse discharging resistor','Cubicle heater',
                                  'Power electronics cubicle over-temperature','Line inductor over-temperature','Not used','Switching cycle AC-Breaker (daily)',
                                  'Pole grounding','Contactor pole grounding','Transformer over-temperature','CPU board over-temperature','CPU core over-temperature',
                                  'Unbalanced DC-Link','Fan lifetime exceeded','dc-link voltage oscillation','Water inlet temperature sensor','Outside temperature sensor',
                                  'Line inductor temperature sensor','Power electronics cubicle temperature sensor','Shut down with local/remote changeover',
                                  'Disconnection from PV generator','Inaccurate power measurement for MPPT','External fan','Fieldbus warning','AC Breaker switching cycle exceeded',
                                  'DC Breaker switching cycle exceeded','Isolation warning','Float controller warning','Over voltage protection','Not used','Not used',
                                  'Not used','Not used','Not used','Not used','Not used','Not used','Not used','Not used','Not used','Not used','Not used','Ready to switch ON',
                                  'Switched ON (power ok)','Operation enabled (RUN)','Fault present','Voltage enabled (drive released)','Quick stop active','Switching ON disabled','Warning present','Line loss',
                                  'Remote','DC circuit breaker ON','Internal limit active','FRT','Converter test mode','Internal alive toggle','Bus alive toggle','B0 Manual stop','B1 Automatic mode','Waiting',
                                  'Cooling initialization','PV-mode','MPP search','MPP reached','PV Power reduction','VAR at night mode','ECAT operational','Buttery operating mode','Synchronization achieved',
                                  'Not used','Not used','Not used','Emergency OFF']})

gui_df = DataFrame({'Planta':['GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI','GUI'],
                      'Falta':['Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1','Fault1',
                              'Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2','Fault2',
                              'Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3','Fault3',
                              'Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4','Fault4',
                              'Warning1','Warning1','Warning1','Warning1','Warning1','Warning1','Warning1','Warning1','Warning1','Warning1','Warning1','Warning1','Warning1',
                              'Warning1','Warning1','Warning1','Warning2','Warning2','Warning2','Warning2','Warning2','Warning2','Warning2','Warning2','Warning2','Warning2',
                              'Warning2','Warning2','Warning2','Warning2','Warning2','Warning2','Warning3','Warning3','Warning3','Warning3','Warning3','Warning3','Warning3',
                              'Warning3','Warning3','Warning3','Warning3','Warning3','Warning3','Warning3','Warning3','Warning3','Status1','Status1','Status1','Status1',
                              'Status1','Status1','Status1','Status1','Status1','Status1','Status1','Status1','Status1','Status1','Status1','Status1','Status2','Status2',
                              'Status2','Status2','Status2','Status2','Status2','Status2','Status2','Status2','Status2','Status2','Status2','Status2','Status2','Status2','Status3'],
                      'Bit':['B0','B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','B12','B13','B14','B15','B0','B1','B2','B3','B4','B5',
                             'B6','B7','B8','B9','B10','B11','B12','B13','B14','B15','B0','B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11',
                             'B12','B13','B14','B15','B0','B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','B12','B13','B14','B15','B0','B1',
                             'B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','B12','B13','B14','B15','B0','B1','B2','B3','B4','B5','B6','B7','B8',
                             'B9','B10','B11','B12','B13','B14','B15','B0','B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','B12','B13','B14',
                             'B15','B0','B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','B12','B13','B14','B15','B0','B1','B2','B3','B4','B5',
                             'B6','B7','B8','B9','B10','B11','B12','B13','B14','B15','B0'],
                      'Mensagem':['ECAT fault','FPGA version','PIB Watchdog','DC-Link overvoltage','Flaat controller','DC-Link short circuit','Pole grounding',
                                    'not used','IGBT desaturation','not used','IGBT Feedback','not used','not used','PIB Central fault','not used','not used',
                                  'PIB internal Power Supply','Short Firing','not used','Amplifier Connector','not used','Current Clipping Timeout','Short Circuit','not used','Heat Sink Over temperature',
                                     'terminal Supply 24V','Fieldbus fault','Battery Synchronisation Fault','Earth Fault','DC-Link Under Voltage','not used','not used',
                                     'Line voltage','Line voltage measurement','AC circuit breaker','FB AC circuit breaker','Pre-charging failed','Line filter','Discharging failed',
                                     'Feedback DC circuit breaker','Amplifier board contactor','DC current direction','UPS','FB PV short circuit breaker','Isolation fault','Max Output Frequency',
                                     'FPGA Firing','PIB hardware configuration','Heat Sink temperature measurement','Low heat Sink temperature','External fan','Cubicle fan','Auxiliary supply',
                                     'Water over temperature','Water pressure','Water pump','initial water heating, initial cooling','Cubicle over temperature','Line inductor over temperature',
                                     'MV transformer vacuum','MV transformer pressure','Mv transformer oil level','MV transformer temperature','FCS','Heat Sink over temperature','Earth fault','Line under voltage',
                                     'Water over temperature','Water pressure','Water pressure sensor','Water heating','Fuse discharging resistor','Cubicle heater','PE cubicle over temperature','Line inductor over temperature',
                                     'not used','Pole grounding over current level 1','Pole grounding over current level 2','Pole grounding Feedback contactor','Pole grounding fuse','CPU board over temperature','CPU core over temperature',
                                     'Unbalanced dc-link voltage','Fan life time exceeded','dc-link voltage ocillation','Water temperature sensor','Outside temperature sensor','Line inductor temperature sensor','PE cubicle temperature sensor',
                                     'Shut down with Local/Remote change-over','Disconnection from PV genertion','inaccurate power measurement for MPPT','External fan*','Switching cycle AC circuit breaker','AC breaker life time exceeded','DC breaker life time exceeded',
                                     'Isolation warning','Float controller','Over voltage protection','not used','not used','Filter cubicle fan','not used','Cubicle temperature warning','SRAM Backup Failure','Fieldbus warning','MV transformer over temperature',
                                     'Isolation sensor','CPU Synchronization','External Power reference','not used ','not used','Ready to switch ON','Switched ON (power ok)','Operation enbled (RUN)','Faul present','Voltage enabled (drive released)','Quick stop active',
                                     'Swiitching ON disabled','Warning present','Line loss','Remote','DC circuit breaker ON','Internal limit active','FRT','Converter test mode','Internal alive toggle','Bus alive toggle','Manual stop','Automatic mode','Waiting',
                                     'Cooling initialization','PV-mode','MPP search','MPP reached','PV Power reduction','VAR at night mode','ECAT operational','Battery operating mode','Synchronization achieved','not used','not used','Isolation monitoring procedure','Hard trip','DC Circuit Breaker Test']})


def main():
    print("\n**** Biosar Fault Translater****")
    print(" * by Eliezer Nascimento * ") 

    # Reading User's input
    print("\n P - Pirapora \n G - Guimarania \n\n O 'texto completo' colado a seguir deve obedecer a forma: \n FaultX register:0000000000000000")
    plant = input("\n Digite a letra referente a planta: ")
    plant = str.lower(plant)
    if (plant == "p" or plant == "g"):
         bitText = input("Cole aqui o texto completo: ")
         bitText = str(bitText)
         if bitText.startswith("Fault") | bitText.startswith("Warning") | bitText.startswith("Status"):
            # Replacing text received
            bitText = bitText.replace('register:', '')
            
            # split fault text
            fault, register = bitText.split(' ', 1)
            
            q = str ("Planta == '{0}' & Falta == '{1}'& Bit == '{2}'").format(idplant(plant), fault, bit(register))
            # trying to get the values and
            # filtering with query method
            if idplant(plant) == "Pirapora":
                df1 = pir_df.query(q)
                print(df1.Mensagem.to_string(index=False)) #Printing fault Message
            elif idplant(plant) == "GUI":
                df1 = gui_df.query(q)
                print(df1.Mensagem.to_string(index=False)) #Printing fault Message
            else:
                print("Não foi possível identificar o nome da falta.\n Tente novamente por favor.")
                # sleep seconds after printing output
                sleep(5)
                return main()

            sleep(3)
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