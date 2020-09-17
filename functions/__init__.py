def inteiro(txt):
    """
    Compare if the number is an integer.
    :param txt: Data input.
    :return: If true return number.
    """
    opc = 0
    while opc == 0:
        try:
            var = str(input(txt))
            if var.isalpha():
                print(f'\033[33m"{var}"\033[m Opção Inválida!')
            else:
                var_2 = int(var)
                opc = 1
                return var_2
        except:
            print(f'\033[33mErro ao reconhecer um número inteiro!\033[m')

def integer_with_bar(txt):
    """
    Compare if the number have bar.
    :param txt: Data input.
    :return: If true return number.
    """
    opc = 0
    while opc == 0:
        try:
            var = str(input(txt))
            if var.isalpha():
                print(f'\033[33m"{var}"\033[m Opção Inválida!')
            elif '/' in var:
                var_2 = str(var)
                opc = 1
                return var_2
            else:
                var_2 = str(var)
                opc = 1
                return var_2
        except:
            print(f'\033[31mErro ao reconhecer um número de sequência!\033[m')


def check_store(number):
    """
    Does the conference if there are branches
    :param number: Branch
    :return: Branch
    """
    opc = 0
    while opc == 0:
        try:
            var = inteiro(number)
            if var == 1432 or var == 2064 or var == 1518 or var == 1744 or var == 1571 or var == 1574 or var == 1648:
                return int(var)
            else:
                print(f'\033[31mFilial Inexistente!\033[m')
        except:
            print(f'\033[31mErro ao digitar a filial!\033[m')
            continue

def comparation(num):
    if num == 1432:
        return 'matriz'
    elif num == 2064:
        return 'centro_sao_leo'
    elif num == 2007:
        return 'shopping'
    elif num == 1518:
        return 'feitoria'
    elif num == 1571:
        return 'marcilio_dias'
    elif num == 1744:
        return 'canudos'
    elif num == 1574:
        return 'joaquim_nabuco'
    elif num == 1648:
        return 'sapucaia'

def type_lens(num):
    if num == 1:
        return 'VS'
    elif num == 2:
        return 'Multifocal'
