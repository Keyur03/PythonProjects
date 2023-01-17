def func(data):
    try:
        count = 1
        endstring = ''
        mark = ''
        l = len(data)
        ccount = 0
        for c in range(l):

            if '?' == data[c] or '!' == data[c]:
                if c == (l - 1):
                    if count == 1:
                        mark = data[c]
                        count = 2
                # elif c+1 != (l-1):
                #     endstring = endstring + data[c]
            else:
                endstring = endstring + data[c]

        endstring = endstring + mark
        return endstring
    except BaseException as e:
        print(e)
        raise e

i = True
while i is True:
    datastring = input(str('Enter String: '))

    print('input string is : {}'.format(datastring))
    abc = func(datastring)
    print('output string is : {}'.format(abc))

    conti = input(str('Do you want to continue y/n:'))
    if conti == 'n' or conti == 'N':
        print('Exiting..')
        break