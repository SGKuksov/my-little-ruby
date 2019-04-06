'''
Программа, которая по атомному номеру элемента 
в переодической таблице химических элементов 
определяет его название.
'''

def table(num):
    '''
    >>> table(10)

    >>>
    '''


    from random import randint

    if len(num) and num.isdigit():
        elem = ''
        num = int(num)

        if num == 3:
            elem = 'Li'
        elif num == 25:
            elem = 'Mn'
        elif num == 80:
            elem = 'Hg'
        elif num == 17:
            elem = 'Cl'
        elif num == 0:
            return
        else:
            table_data = [3, 25, 80, 17]
            r = randint(0, 3)
            table_data[r]

            print(f'Такого номера нет. Введите другой номер, например {table_data[r]} или 0, чтобы завершить программу')
            return table()
    
        return print(f'Вы ввели номер {num}. Это атомный номер элемента {elem}')

    else:
        print('Введите атомный номер элемента (введите 0, чтобы завершить программу): ')
        return table()


num = input('Введите атомный номер элемента или 0, чтобы завершить программу: ')
table(num)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

