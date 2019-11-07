import sqlite3
import random as r

def main():
    choice = 0

    while choice != 1 or choice != 2:
        if choice == 1:
            print(rBoy())
            break
        
        if choice == 2:    
            print(rGirl())
            break
       
        choice = int(input("Would you like a boy name or girl name?\nPress 1 for boy or 2 for girl!\n"))

        
def rBoy():
    conn = sqlite3.connect('babyNamesDB_2column.db')
    cur = conn.cursor()
    for rowB in cur.execute('SELECT Boys FROM babyNames ORDER BY RANDOM() LIMIT 1;'):
        a = list(rowB)
        return a
    conn.close()


def rGirl():
    conn = sqlite3.connect('babyNamesDB_2column.db')
    cur = conn.cursor()
    for rowG in cur.execute('SELECT Girls FROM babyNames ORDER BY RANDOM() LIMIT 1;'):
        b = list(rowG)
        return b
    conn.close()


if __name__ == "__main__":
    main()