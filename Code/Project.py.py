import pandas as pd
import pyodbc

data = pd.read_csv("C:/Users/user/Desktop/projet_entrepot/used_cars.csv")

pd.set_option('display.max_rows', None)  

data = data.dropna()

for index, row in data.iterrows():               
    if row[0] == "???" or row[8] == "???":
        data = data.drop(index) 
    elif row[3] == "Error":
        data = data.drop(index)
    elif int(row[3]) <= 0 or int(row[4]) <= 0:
        data = data.drop(index)     
    elif int(row[2]) > 2024 or int(row[2]) < 1885:
        data = data.drop(index)
    elif int(row[5]) != 2024 - int(row[2]):
        data = data.drop(index)

data = data.reset_index(drop=True)


server = 'DESKTOP-F9JIOS6\TEW_SQLEXPRESS'
database = 'Project'
password = ''

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                            f'SERVER={server};'
                            f'DATABASE={database};'
                            "Trusted_Connection=yes;"
                            )


cursor = connection.cursor()

cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'BrandsAndModels' AND xtype = 'U')
    CREATE TABLE BrandsAndModels (
        Brand VARCHAR(100),
        Model VARCHAR(100)
    )""")
cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'YearAndAge' AND xtype = 'U')
    CREATE TABLE YearAndAge (
        Year INT,
        Age INT
    )""")
cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Mileage' AND xtype = 'U')
    CREATE TABLE Mileage (
        Mileage INT
    )""")
cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'FuelTypeAndTransmission' AND xtype = 'U')
    CREATE TABLE FuelTypeAndTransmission (
        FuelType VARCHAR(50),
        Transmission VARCHAR(50)
    )""")

cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Price' AND xtype = 'U')
    CREATE TABLE Price (
        Price DECIMAL(18, 2),
        ID_brand int identity(1,1),
        ID_date int identity(1,1),
        ID_mileage int identity(1,1), 
        ID_information int identity(1,1)
    )""")

for index, row in data.iterrows():
    brand = row[0]
    model = row[1]
    year = int(row[2])
    age = float(row[5])
    mileage = float(row[4])
    fuel_type = row[6]
    transmission = row[7]
    price = float(row[3])
    cursor.execute("""
        INSERT INTO BrandsAndModels (Brand, Model)
        VALUES (?, ?)
    """, (brand, model))
    cursor.execute("""
        INSERT INTO YearAndAge (Year, Age)
        VALUES (?, ?)
    """, (year, age))
    cursor.execute("""
        INSERT INTO Mileage (Mileage)
        VALUES (?)
    """, (mileage,))
    cursor.execute("""
        INSERT INTO FuelTypeAndTransmission (FuelType, Transmission)
        VALUES (?, ?)
    """, (fuel_type, transmission))
    cursor.execute("""
        INSERT INTO Price (Price)
        VALUES (?)
    """, (price,))

    
connection.commit()

cursor.close()
connection.close()


