import pymongo as pmg
import pprint
from bson.objectid import ObjectId

# Создаём клиента
client = pmg.MongoClient('localhost', 27017)

# Присоединяемся к базе данных
db = client['test_mongo']

# Вытаскиваем нужную коллекцию
series_collection = db['cars']

list_of_commands = ['manufacture', 'later_then', 'options', 'help', 'exit']
list_of_description = [' Выводит список машин указанного производителя',
' Выводит список машин собранных не раньше чем указанный год ',
' Выводит список опций машины с указанным id',
' Выводит список команд и их описание',
' Выход из программы',]

while (True):
    cmd = input(" > ")
    cmd_name = cmd.split()[0]
    if (cmd_name not in list_of_commands):
        print('Неверная команда. Для получения списка команд введите help')
    elif(cmd_name == list_of_commands[0]):
        result = [r for r in series_collection.find({'manufacture':cmd.split()[1]})]
        print('Количество машин указанного производителя ', len(result))
        for n in result:
            pprint.pprint(n)
            print()
    elif(cmd_name == list_of_commands[1]):
        result = [r for r in series_collection.find({'year':{'$gte':int(cmd.split()[1])}}).sort('year')]
        print('Количество машин не раньше указанного года ', len(result))
        print()
        for n in result:
            pprint.pprint(n)
            print()
    elif(cmd_name == list_of_commands[2]):
        try:
            result = [r for r in series_collection.find({'_id':ObjectId(cmd.split()[1])})]
            for n in result:
                if('car_options' in n):
                    pprint.pprint(n['car_options'])
                print()
        except:
            print('Нет машины с таким id')

    elif(cmd_name == list_of_commands[3]):
        print('Список команд ')
        for n in range(len(list_of_commands)):
            print(list_of_commands[n])
            print(list_of_description[n])
            print()
    elif(cmd_name == list_of_commands[4]):
        print('Сеанс работы завершается...')
        break
