import pyodbc

server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'

conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')

import pandas as pd

def get_data_from_table(conn, table_name):
    query = f'SELECT * FROM {table_name}'
    df = pd.read_sql(query, conn)
    return df

table_name = 'servers'
df = get_data_from_table(conn, table_name)
print(df.head())


def insert_data_to_table(conn, table_name, values):
    placeholders = ', '.join(['?'] * len(values))
    query = f'INSERT INTO {table_name} VALUES ({placeholders})'
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()

table_name = 'servers'
new_values = ('server4', '10.0.0.4')
insert_data_to_table(conn, table_name, new_values)

def delete_data_from_table(conn, table_name, where_clause):
    query = f'DELETE FROM {table_name} WHERE {where_clause}'
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

table_name = 'servers'
where_clause = 'name = \'server4\''
delete_data_from_table(conn, table_name, where_clause)

#--------------------------------------------

import pyodbc

def insert_employee_with_savepoint():
    # Bağlantıyı oluştur
    server = 'localhost,1433'
    database = 'company_db'
    username = 'username'
    password = 'password'
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

    # Cursor oluştur
    cursor = cnxn.cursor()

    try:
        # Savepoint aç
        cursor.execute("SAVEPOINT InsertEmployee")

        # İlk insert işlemi
        cursor.execute("INSERT INTO employees (first_name, last_name, department, salary) VALUES (?, ?, ?, ?)", 'John', 'Doe', 'Sales', 5000)

        # İkinci insert işlemi
        cursor.execute("INSERT INTO employees (first_name, last_name, department, salary) VALUES (?, ?, ?, ?)", 'Jane', 'Doe', 'Marketing', 6000)

        # Hata fırlat (Örneğin: aynı kaydın tekrar eklenmesi durumunda Unique Key constraint hatası oluşabilir)
        cursor.execute("INSERT INTO employees (first_name, last_name, department, salary) VALUES (?, ?, ?, ?)", 'John', 'Doe', 'Sales', 5000)

    except:
        # Hata alındığında rollback yap
        cursor.execute("ROLLBACK TO InsertEmployee")
        cnxn.commit()
        print("Insert işlemi başarısız oldu, rollback yapıldı.")

    else:
        # Herhangi bir hata olmadığında commit yap
        cnxn.commit()
        print("Insert işlemi başarılı bir şekilde tamamlandı.")

    finally:
        # Bağlantıyı kapat
        cnxn.close()

#--------------------------------------------

