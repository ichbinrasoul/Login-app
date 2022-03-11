import sqlite3
from my_employee import Karmand
from tabulate import tabulate
# connection
conn = sqlite3.connect('My_database.db')
cur = conn.cursor()
# cur.execute('''CREATE TABLE karmand (
#     first text,
#     last text,
#     pay integer
# )''')


def insert_emp(emp):
    with conn:
        cur.execute('INSERT INTO karmand VALUES (:first, :last, :pay)', {
                    'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emp_by_lastname(lastname):
    cur.execute('SELECT * FROM karmand WHERE last = :last',
                ({'last': lastname}))
    return cur.fetchall()


def get_all_emp():
    cur.execute('SELECT * FROM karmand')
    return cur.fetchall()


def update_pay(emp, pay):
    with conn:
        cur.execute('''UPDATE karmand SET pay = :pay WHERE first = :first AND last = :last''',
                    {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        cur.execute('''DELETE from karmand WHERE first = :first AND last = :last''',
                    {'first': emp.first, 'last': emp.last})


emp1 = Karmand('ali', 'zand', 6200)
emp2 = Karmand('mitra', 'hajjar', 5800)
mng1 = Karmand('afsane', 'pakrou', 10000)
dev1 = Karmand('rasoul', 'hejazi', 7000)

# insert_emp(mng1)
# insert_emp(dev1)
# insert_emp(emp1)
# insert_emp(emp2)

# emps = get_emp_by_lastname('hejazi')
# print(emps)

# emps = get_all_emp()
# print(tabulate(emps))

# update_pay(emp2,600)
# emps = get_emp_by_lastname('hajjar')
# print(tabulate(emps))

# remove_emp(mng1)

print(tabulate(get_all_emp()))

conn.close()
