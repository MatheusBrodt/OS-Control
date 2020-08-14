def inteiro(txt):
    """
    Compare if the number is an integer.
    :param txt: Data input
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
