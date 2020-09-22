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
            if store == 0:
                break
            os = functions.integer_with_bar('Digite o número da OS: ')
            if os == 0:
                break
            service_type = functions.inteiro('Digite 1 para "VS" ou 2 para "Multifocal": ')
            if service_type == 0:
                break
            store_comparation = functions.comparation(store)
            lens = functions.type_lens(service_type)
            if service_type == 1:
                connection = mysql.connector.connect(host='localhost', user='root', password='',
                                                     database='controle_de_serviços')
                cursor = connection.cursor()
                cursor.execute(f"SELECT sequencia FROM {store_comparation}")
                result = cursor.fetchall()
                load = 0
                while load == 0:
                    re = 1
                    for line in result:
                        read = line
                        re = 0
                        if os in read:
                            print(f'\033[33mOS já cadastrada!\033[m')
                            os = functions.integer_with_bar('Digite novamente o número da OS: ')
                            re = 1
                        if re != 0:
                            try:
                                connection = mysql.connector.connect(host='localhost', user='root', password='',
                                                                     database='controle_de_serviços')
                                cursor = connection.cursor()
                                cursor.execute(f"INSERT INTO {store_comparation} (dia, sequencia, tipo) "
                                               f"VALUES ('{date}', '{os}', '{lens}')")
                                connection.commit()
                                connection.close()
                                re = 0
                            except:
                                if re != 1:
                                    print(f'\033[31mNão foi possível acessar o banco de dados!\033[m')
                            else:
                                print(f'\033[33mSalvo com sucesso no banco de dados!\033[m')
                                load = 1
            elif service_type == 2:
                connection = mysql.connector.connect(host='localhost', user='root', password='',
                                                     database='controle_de_serviços')
                cursor = connection.cursor()
                cursor.execute(f"SELECT sequencia FROM {store_comparation}")
                result = cursor.fetchall()
                load = 0
                while load == 0:
                    re = 1
                    for line in result:
                        read = line
                        re = 0
                        if os in read:
                            print(f'\033[33mOS já cadastrada!\033[m')
                            os = functions.integer_with_bar('Digite novamente o número da OS: ')
                            re = 1
                        if re != 0:
                            try:
                                connection = mysql.connector.connect(host='localhost', user='root', password='',
                                                                     database='controle_de_serviços')
                                cursor = connection.cursor()
                                cursor.execute(f"INSERT INTO {store_comparation} (dia, sequencia, tipo) "
                                               f"VALUES ('{date}', '{os}', '{lens}')")
                                connection.commit()
                                connection.close()
                                re = 0
                            except:
                                if re != 1:
                                    print(f'\033[31mNão foi possível acessar o banco de dados!\033[m')
                            else:
                                print(f'\033[33mSalvo com sucesso no banco de dados!\033[m')
                                load = 1
            else:
                print('\033[31mOpção inválida!\033[m')
                continue
            break
        continue
    elif option == 2:
        store = functions.check_store('Digite o número da filial: ')
        os = functions.integer_with_bar('Digite o número da OS: ')
        store_comparation = functions.comparation(store)
        connection = mysql.connector.connect(host='localhost', user='root', password='',
                                             database='controle_de_serviços')
        try:
            cursor = connection.cursor()
            cursor.execute(f"SELECT sequencia FROM {store_comparation}")
            result = cursor.fetchall()
            alert = False
            for line in result:
                if os == line:
                    print('\033[34mOS encontrada!\033[m')
                    alert = True
                else:
                    alert = True
            if alert:
                cursor.execute(f"SELECT dia FROM {store_comparation} WHERE sequencia IN ({os})")
                day = cursor.fetchall()
                print(f'Montagem da OS "\033[31m{os}\033[m" realizada {day}.')
            else:
                print(f'\033[34mOS não encontrada!\033[m')
            connection.close()
        except:
            print(f'\033[31mNão foi possível acessar o banco de dados!\033[m')
        else:
            print(f'\033[33mEncontrado com sucesso no banco de dados!\033[m')
    elif option == 0:
        break
    else:
        print(f'\033[31mOpção Inválida no primeiro passo!\033[m')
        continue
print('\033[32mFIM\033[m'.center(32))
print(date)
