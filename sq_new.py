# coding: cp1251

"""
��������� �������� �� Python ������ 2.7.
������������ ��������� cp1251, � �� utf-8, �� ������� ����, ���
��� ���� ������� ���� ����������� Python ������ 2.7, � �� 3.�
� �������� �������� ���� �� ������������ ������� windows 7.
"""


import sqlite3
import sys
from re import sub
from os import path, remove


def create_table(table_name, for_table):

# �������� �������
    try:
        c.execute('''create table %s (date text, name text,
                                     surname text, qty int)''' %table_name)
    except:
        print '������ �������� ������� 1'
        sys.exit()

# ������� ���� ������
    for i in for_table:
        c.execute('insert into %s values %s' %(table_name, str(i))) 
# ���������� (commit) ��������� 
    conn.commit()



def tables_comparison(t1, t2):
    
    tables_distinction = []

    c.execute('select * from %s ' %t1)
    table_1_content = c.fetchall()

    c.execute('select * from %s ' %t2)
    table_2_content = c.fetchall()
# ���������� ������� � �������� � ���������� �� ������
    for e in table_1_content:
        if not e in table_2_content:
            tables_distinction.append(e)



    for x in tables_distinction:
        x = sub('u', '', str(x))
        c.execute('insert into %s values %s' % (t2, x))
    conn.commit()


           
tb_1_name = 'engineers'
tb_2_name = 'economists'

for_table_1 = [('2006-01-05','Peter','Black',24),
               ('2006-01-05','Alexander','Green',35),
               ('2006-01-05','Michael','Cooper',42)
              ]


for_table_2 = [('2006-01-05','Jack','Ford',26),
               ('2006-01-05','Harry','Potter',30),
               ('2006-01-05','Michael','Cooper',42)
              ]



if __name__ == '__main__':
    
    if path.exists('example.db'):
        remove('example.db')

    try:
        conn=sqlite3.connect('example.db')
    except:
        print '������ ���������� � ����� ������'
        sys.exit()

    c = conn.cursor()
    
    tb_1_name = 'engineers'
    tb_2_name = 'economists'
    create_table(tb_1_name, for_table_1)
    create_table(tb_2_name, for_table_2)


    tables_comparison(tb_1_name, tb_2_name)

    # �������� �������, � ������ ���� �� ������ �� �����
    c.close()

