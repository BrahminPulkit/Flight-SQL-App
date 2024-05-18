import mysql.connector

# Connect to the database server
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',  # Replace 'your_password' with your actual password
        database='indigo'  # Specify the database name here
    )

    mycursor = conn.cursor()
    print('Connection established')

except mysql.connector.Error as e:
    print('Connection error:', e)


# Create the table 
# mycursor.execute("""
# CREATE TABLE airport (
#     airport_id INT PRIMARY KEY AUTO_INCREMENT,
#     code VARCHAR(10) NOT NULL,
#     city VARCHAR(100) NOT NULL,
#     name VARCHAR(255) NOT NULL           
# )
# """)
# conn.commit()

# INSERT DATA INTO TABLE 
# mycursor.execute("""
#     INSERT INTO airport VALUES
#     (1, 'DEL', 'New Delhi', 'IGIA'),
#     (2, 'CCU', 'Kolkata', 'NSCA'),
#     (3, 'BOM', 'Mumbai', 'CSMA')                 
# """)
# conn.commit()


# mycursor.execute("DROP TABLE airport")
# conn.commit()

# Search Retrieve 

mycursor.execute(" SELECT * FROM airport  WHERE airport_id > 1")
data = mycursor.fetchall()
print(data)


for i in data:
    print(i[3])


# update Query

mycursor.execute("""
    UPDATE airport
    SET city = 'Bombay'
    WHERE airport_id = 3
""")
conn.commit()


mycursor.execute(" SELECT * FROM airport  WHERE airport_id > 1")
data = mycursor.fetchall()
print(data)


for i in data:
    print(i[3])



# Delete 
mycursor.execute("DELETE FROM airport WHERE airport_id = 3")
conn.commit()


mycursor.execute(" SELECT * FROM airport  WHERE airport_id > 1")
data = mycursor.fetchall()
print(data)


for i in data:
    print(i[3])
    