import functions
from datetime import date
import mysql.connector

print('\033[33mControle de serviços Óticas Carol\033[m')
print('-' * 33)

#  date entry for service
while True:
    #  current date
    date = date.today()
    option = functions.inteiro('(1) Para cadastrar / (2) Para pesquisar: ')
    if option == 1:
        while True:
            store = functions.check_store('Digite o número da filial: ')
            os = functions.integer_with_bar('Digite o número da OS: ')
            service_type = functions.inteiro('Digite 1 para "VS" ou 2 para "Multifocal": ')
            store_comparation = functions.comparation(store)
            lens = functions.type_lens(service_type)
            if service_type == 1:
                try:
                    connection = mysql.connector.connect(host='localhost', user='root', password='',
                                                         database='controle_de_serviços')
                    cursor = connection.cursor()
                    cursor.execute(f"INSERT INTO {store_comparation} (dia, sequencia, tipo) "
                                   f"VALUES ('{date}', '{os}', '{lens}')")
                    connection.commit()
                    connection.close()
                except:
                    print(f'\033[31mNão foi possível acessar o banco de dados!\033[m')
                else:
                    print(f'\033[33mSalvo com sucesso no banco de dados!\033[m')
            elif service_type == 2:
                try:
                    connection = mysql.connector.connect(host='localhost', user='root', password='',
                                                         database='controle_de_serviços')
                    cursor = connection.cursor()
                    cursor.execute(f"INSERT INTO {store_comparation} (dia, sequencia, tipo) "
                                   f"VALUES ('{date}', '{os}', '{lens}')")
                    connection.commit()
                    connection.close()
                except:
                    print(f'\033[31mNão foi possível acessar o banco de dados!\033[m')
                else:
                    print(f'\033[33mSalvo com sucesso no banco de dados!\033[m')
            else:
                print('\033[31mOpção inválida!\033[m')
                continue
            break
        continue
    elif option == 2:
        print('2')
        continue
    else:
        print(f'\033[31mOpção Inválida no primeiro passo!\033[m')
        continue
