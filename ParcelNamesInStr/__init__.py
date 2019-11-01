def ParcelNamesInStr(your_names):
    '''
    Функція перетворює рядок з ПІБ у 3, де прізвище, ім'я, побатькові виводиться у кожному окремо.
    :param your_names: type(str), format(ПІБ), in(input), example(Рижкова Дар'я Олександрівна)
    :return: type(str),format(Прізвище        example(Рижкова
                              Ім'я                    Дар'я
                              Побатькові)             Олександрівна)
    '''
    NameList = your_names.split(" ")
    FirstName = NameList[0]
    SecName = NameList[1]
    SurName = NameList[2]
    # print (FirstName)
    # print (SecName)
    # print (SurName)
    return None
your_names = input (" ")
ParcelNamesInStr(your_names)

