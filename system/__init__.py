from datetime import date
import functions

print('\033[33mControle de serviços Óticas Carol\033[m')
print('-'*33)

date = date.today()
temporary_comparison = ''

#  date entry for service
option = functions.inteiro('(1) Para cadastrar / (2) Para pesquisar: ')
if option == 1:
    while True:
        store = functions.check_store('Digite o número da filial: ')
        os = functions.inteiro('Digite o número da OS: ')
        service_type = functions.inteiro('Digite 1 para "VS" ou 2 para "Multifocal": ')
        tem_store = service_type
        if service_type == 1:
            cont_vs = 1
            service_type = 'VS'
            file_txt = open('arquivo.txt', 'at')  # file open for recording
            temporary = str(f'Loja: {store} | Seq: {os} | Tipo: {service_type}\n')
            read_file = open('arquivo.txt', 'r')
            for line in read_file:
                if temporary != line:
                    temporary_comparison = temporary
                else:
                    print(f'\033[31mVocê terá que alterar o código da filial ou o número da OS!\033[m')
                    store = functions.check_store('Digite o código da filial: ')
                    os = functions.inteiro('Digite o número da OS: ')
                    correct = str(f'Loja: {store} | Seq: {os} | Tipo: {service_type}\n')
                    temporary = correct
                    file_txt.write(correct)
            file_txt.write(temporary_comparison)
            file_txt.close()  # closed file for recording
        elif service_type == 2:
            cont_multi = 1
            service_type = 'Multifocal'
            file_txt = open('arquivo.txt', 'at')  # file open for recording
            temporary = str(f'Loja: {store} | Seq: {os} | Tipo: {service_type}\n')
            read_file = open('arquivo.txt', 'r')
            for line in read_file:
                if temporary != line:
                    file_txt.write(temporary)
                else:
                    print(f'\033[31mVocê terá que alterar o código da filial ou o número da OS!\033[m')
                    store = functions.check_store('Digite o códgio da filial: ')
                    os = functions.inteiro('Digite o número da OS: ')
                    correct = str(f'Loja: {store} | Seq: {os} | Tipo: {service_type}\n')
                    file_txt.write(correct)
            file_txt.close()  # closed file for recording
        else:
            print('\033[31mOpção inválida!\033[m')
            continue
else:
    print('2')
