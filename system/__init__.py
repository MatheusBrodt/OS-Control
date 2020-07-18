from datetime import date

print('\033[33mControle de serviços Óticas Carol\033[m')
print('-'*33)

date = date.today()

# dictionary for system
os_multifocal = list()
os_visao_simples = list()
temp_dict = dict()
cont = 0

#  date entry for service

while True:
    store = int(input('Digite o número da filial: '))
    os = int(input('Digite o número da OS: '))
    service_type = int(input('Digite "1" para VS ou "2" para Multifocal: '))
    cont += 1
    if service_type == 1:
        service_type = 'VS'
        temp_dict['Loja'] = store
        temp_dict['Tipo'] = service_type
        temp_dict['Data'] = date
        os_visao_simples.append(temp_dict.copy())
        temp_dict.clear()
    elif service_type == 2:
        service_type = 'Multifocal'
        temp_dict['Loja'] = store
        temp_dict['Tipo'] = service_type
        temp_dict['Data'] = date
        os_multifocal.append(temp_dict.copy())
        temp_dict.clear()
    else:
        print('\033[31mOpção inválida!\033[m')
    print(os_visao_simples)
    print(os_multifocal)
