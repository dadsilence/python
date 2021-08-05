#city = 'Rostov-on-Don'
#print(city[:])

# name = 'Alexey'
# lastname = 'Zotov'
# print(name + ' ' + lastname)
#list_1 = ['have','a','nice','day']
# print(len(name))
# print(city.find('o'))
# print(city.index('o'))
# print(city.count('n'))
# print(city.replace('Don','Volga'))
# print(city.split('o'))
# print('_'.join(list_1))
#print(city.upper())

#1. Вы получили такую строку логов:
'''
z1 = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
z3 = z1.split(' ')
print(z3)
#Совершите над ней следующие действия:

#1.2. Выделите и выведите на экран дату и время
# print(z1[:15])
print(f'{z3[0]} {z3[1]} {z3[2]}')
#1.3. Выделите и выведите на экран название сервиса (systemd[1]), записавшего лог
print(z1[24:34])
#1.4. Замените название ПК (ideapad) на PC-12092, выведите полученную строку на экран
print(z1.replace('ideapad','PC-12092'))
#1.5. Найдите в логе слово failed и выведите его позицию, если такого слова нет, выведите -1.
print(z1.find('failed'))
#1.6. Посчитайте количество букв 'S' в строке вне зависимости от регистра (и прописных, и заглавных)
print(z1.upper().count('S'))
#1.7. Выделите из строки значения часов, минут и секунд, суммируйте эти 3 числа и выведите полученное число на экран
print(int(z1[7:9])+int(z1[10:12])+int(z1[13:15]))
'''



#2. Опционально) Вы получили такую строку логов:
z2 = 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'
z4 = z2.split(' ')
print(z4)
#print(z4[4].replace(':', '')
z5 = z2.split(':')
print(z5)

#Нужно сформировать и вывести сообщение в таком формате:
'''
#The PC "<имя ПК>" receive message from service "<имя сервиса>" what says "<сообщение>" because "<причина ошибки>" at <дата, время>
pc_name = z2[16:23]
service_name = z2[24:35]
error_text = z2[37:69]
reason_text = z2[71:91]
error_time = z2[:15]
print(f'The PC "{pc_name}" receive message from service "{service_name}" what says "{error_text}" because "{reason_text}" at {error_time}')
print(f'The PC "{z4[3]}" receive message from service "{z4[4]}"')
'''