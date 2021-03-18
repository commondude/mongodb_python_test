import pymongo as pmg
import pprint

# Create the client
client = pmg.MongoClient('localhost', 27017)

# Connect to our database
db = client['test_mongo']

# Fetch our series collection
series_collection = db['cars']

list_of_commands = ['manufacture', 'later_then', 'options', 'help', 'exit']

while (True):
    cmd = input(" > ")
    cmd_name = cmd.split()[0]
    if (cmd_name not in list_of_commands):
        print('Неверная команда. Для получения списка команд введите help')
    elif(cmd_name == list_of_commands[0]):
        print(0)
        result = [r for r in series_collection.find({'manufacture':cmd.split()[1]})]
        print('Количество машин указанного производителя ', len(result))
        for n in result:
            pprint.pprint(n)
            print()
    elif(cmd_name == list_of_commands[1]):
        print(1)
    elif(cmd_name == list_of_commands[2]):
        print(2)
    elif(cmd_name == list_of_commands[3]):
        print('Список команд ')
        print( list_of_commands )
    elif(cmd_name == list_of_commands[4]):
        print('Сеанс работы завершается...')
        break
