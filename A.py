import string

english_alphabet = {
                    i: j
                    for i, j
                    in zip(string.ascii_uppercase, range(1,len(string.ascii_uppercase)+1))
                    }

def main():
    n = int(input())
    if n == 0:
        print('', end ='')
    else:
        answer_list = []
        for i in range(n):
            line = input().split(',')

            answer_list.append(calcule_code(line[0],line[1],line[2],line[3],line[4]))

        print(*answer_list)


def calcule_code(firstname, name, secondname, day, month):
    global english_alphabet
    # print(name, firstname, secondname, day, month, year)
    unique_elms = []
    for elem in name+firstname+secondname:
        if elem not in unique_elms:
            unique_elms.append(elem)
    # print(unique_elms)
    intDM = 0
    for number in day+month:
        intDM += int(number)
    intDM *= 64
    # print([firstname[0]])
    intFL = english_alphabet[firstname[0].upper()] * 256
    intSUM = len(unique_elms) + intFL + intDM
    # print(intDM, intFL, len(unique_elms))
    hexSUM = hex(intSUM)[2:].upper()

    print(type(hexSUM))
    print(hexSUM)
    if len(hexSUM) >= 3:
        return (hexSUM[-3:])
    elif len(hexSUM) < 3:
        while len(hexSUM) < 3:
            hexSUM = '0' + hexSUM
        return (hexSUM)

if __name__ == '__main__':
    main()

