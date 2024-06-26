print ('########################################')
print ('#        ALGORITMOS EM PYTHON          #')
print ('########################################')
print ('#Escolha uma opção                     #')
print ('#1. Fibonacci                          #')
print ('########################################')

try:
    choice = int(input())
    if choice == 1:
        print('FIB')
    else:    
        print('opção inválida')
except:
    print('ocorreu um erro...')
