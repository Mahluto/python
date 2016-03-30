# coding: cp1251

"""
Программа написана на Python версии 2.7.
Использована кодировка cp1251, а не utf-8, по пречине того, что
как было сказано выше использован Python версии 2.7, а не 3.х
и написана прогамма была на операционной системе windows 7.
"""


import sqlite3
import sys
from re import sub
from os import path, remove


def create_table_1(table_1_name):

    
    for_table_1 = [('2006-01-05','Peter','Black',24),
                   ('2006-01-05','Alexander','Green',35),
                   ('2006-01-05','Michael','Cooper',42)
                  ]

    try:
        conn=sqlite3.connect('example.db')
    except:
        print 'Ошибка соединения с базой данных'
        sys.exit()

    c = conn.cursor()
    
# Создание таблицы
    try:
        c.execute('''create table %s (date text, name text,
                                     surname text, qty int)''' %table_1_name)
    except:
        print 'Ошибка создания таблицы 1'
        sys.exit()

# Вставка ряда данных
    for i in for_table_1:
        c.execute('insert into %s values %s' %(table_1_name, str(i))) 
# Сохранение (commit) изменений 
    conn.commit() 
# Закрытие курсора, в случае если он больше не нужен
    c.close()


def create_table_2(table_2_name):


    for_table_1 = [('2006-01-05','Jack','Ford',26),
                   ('2006-01-05','Harry','Green',30),
                   ('2006-01-05','Michael','Cooper',42)
                  ]

    try:
        conn=sqlite3.connect('example.db')
    except:
        print 'Ошибка соединения с базой данных'
        sys.exit()

    c = conn.cursor()
    
# Создание таблицы
    try:
        c.execute('''create table %s (date text, name text,
                                     surname text, qty int)''' %table_2_name)
    except:
        print 'Ошибка создания таблицы 2'
        sys.exit()
        
# Вставка ряда данных
    for j in for_table_1:
        c.execute('insert into %s values %s' % (table_2_name, str(j))) 
# Сохранение (commit) изменений 
    conn.commit() 
# Закрытие курсора
    c.close()



def tables_comparison(t1, t2):
    
    tables_distinction = []
    conn=sqlite3.connect('example.db')
    c = conn.cursor()

    c.execute('select * from %s ' %t1)
    table_1_content = c.fetchall()

    c.execute('select * from %s ' %t2)
    table_2_content = c.fetchall()
# Нахождения разнецы в таблицах и сохранения ее список
    for e in table_1_content:
        if not e in table_2_content:
            tables_distinction.append(e)



    for x in tables_distinction:
        x = sub('u', '', str(x))
        c.execute('insert into %s values %s' % (t2, x))
    conn.commit()


    c.close()


           
tb_1_name = 'engineers'
tb_2_name = 'economists'

if __name__ == '__main__':
    
    if path.exists('example.db'):
        remove('example.db')
    
    tb_1_name = 'engineers'
    tb_2_name = 'economists'
    create_table_1(tb_1_name)
    create_table_2(tb_2_name)

    tables_comparison(tb_1_name, tb_2_name)
