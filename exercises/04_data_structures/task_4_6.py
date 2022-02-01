# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
str1=ospf_route.split()
#ip_temp = '''
#Prefix{0:>17}
#AD/Metric{1:>14}
#Next-Hop{2:>15}
#Last Update{3:>12}
#Outbound Interface{4:>20}
#'''
#print('Prefix\tb',ip_temp.format(str1[0],str1[1].strip('[]'),str1[3].strip(','),str1[4].strip(','),str1[5]))
print(' Prefix ',str1[0],'\n','AD/Metric ',str1[1].strip('[]'),'\n','Next-Hop ',str1[3].strip(','),'\n','Last Update\t',str1[4].strip(),'\n','Outbound Interface ',str1[5])