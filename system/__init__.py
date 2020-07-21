from datetime import date
import functions

print('\033[33mControle de serviços Óticas Carol\033[m')
print('-'*33)

date = date.today()

# Dicionários das lojas
loja_1432 = list()
loja_2064 = list()
loja_1518 = list()
loja_1744 = list()
loja_1571 = list()
loja_1574 = list()
loja_1648 = list()

#  others
multifocal_amount = list()
vs_amount = list()
if date.day == 1:
    multifocal_amount.clear()
    vs_amount.clear()

# dictionary for system
temp_dict = dict()

#  date entry for service
while True:
    store = functions.check_store('Digite o número da filial: ')
    os = functions.inteiro('Digite o número da OS: ')
    service_type = functions.inteiro('Digite 1 para "VS" ou 2 para "Multifocal": ')
    tem_store = service_type
    if service_type == 1:
        cont_vs = 1
        service_type = 'VS'
        temp_dict['Loja'] = store
        temp_dict['Sequência'] = os
        temp_dict['Tipo'] = service_type
        temp_dict['Data'] = date
        file_txt = open('arquivo.txt', 'at')  # file open for recording
        if store == 1432:
            loja_1432.append(temp_dict.copy())
        elif store == 2064:
            loja_2064.append(temp_dict.copy())
        elif store == 1518:
            loja_1518.append(temp_dict.copy())
        elif store == 1744:
            loja_1744.append(temp_dict.copy())
        elif store == 1571:
            loja_1571.append(temp_dict.copy())
        elif store == 1574:
            loja_1574.append(temp_dict.copy())
        elif store == 1648:
            loja_1648.append(temp_dict.copy())
        file_txt.write(f'Loja: {store} Seq: {os} Tipo: {service_type} Data: {date}\n')
        temp_dict.clear()
        vs_amount.append(cont_vs)
        file_txt.close()  # closed file for recording
    elif service_type == 2:
        cont_multi = 1
        service_type = 'Multifocal'
        temp_dict['Loja'] = store
        temp_dict['Sequência'] = os
        temp_dict['Tipo'] = service_type
        temp_dict['Data'] = date
        file_txt = open('arquivo.txt', 'at')  # file open for recording
        if store == 1432:
            loja_1432.append(temp_dict.copy())
        elif store == 2064:
            loja_2064.append(temp_dict.copy())
        elif store == 1518:
            loja_1518.append(temp_dict.copy())
        elif store == 1744:
            loja_1744.append(temp_dict.copy())
        elif store == 1571:
            loja_1571.append(temp_dict.copy())
        elif store == 1574:
            loja_1574.append(temp_dict.copy())
        elif store == 1648:
            loja_1648.append(temp_dict.copy())
        file_txt.write(f'Loja: {store} Seq: {os} Tipo: {service_type} Data: {date}\n')
        temp_dict.clear()
        multifocal_amount.append(cont_multi)
        file_txt.close()  # closed file for recording
    else:
        print('\033[31mOpção inválida!\033[m')
    print(loja_1432)
    print(loja_2064)
    print(loja_1518)
    print(loja_1744)
    print(loja_1571)
    print(loja_1574)
    print(loja_1648)
    print(f'Temos {len(vs_amount)} montagens de VS.')
    print(f'Temos {len(multifocal_amount)} montagens de Multifocal.')
