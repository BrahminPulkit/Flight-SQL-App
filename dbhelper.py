import mysql.connector

class DB:
    def __init__(self):
        # Connect to the database

        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',  # Replace 'your_password' with your actual password
                database='flight'  # Specify the database name here
            )

            self.mycursor = self.conn.cursor()
            print('Connection established')

        except mysql.connector.Error as e:
            print('Connection error:', e)


    def fetch_city_names(self):
        city = []
        self.mycursor.execute("""
        SELECT DISTINCT(Destination) FROM  flights_data
        UNION 
        SELECT DISTINCT(Source) FROM  flights_data;
    """)
        
        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
        return city
    

    def fetch_all_flights(self, source, destination):
        self.mycursor.execute("""
        SELECT Airline, Route, Dep_Time, Duration, Price FROM flights_data
        WHERE Source = '{}' AND Destination = '{}'
        """.format(source, destination))


        data = self.mycursor.fetchall()
        return data
    

    def fetch_airline_frequency(self):

        airline = []
        frequnecy = []

        self.mycursor.execute("""
        SELECT Airline, COUNT(*) FROM flights_data
        GROUP BY Airline
        """)

        data = self.mycursor.fetchall()
        
        for iteam in data:
            airline.append(iteam[0])
            frequnecy.append(iteam[1])

        return airline, frequnecy
                              
        

    def busy_airport(self):
        city = []
        frequnecy = []
        self.mycursor.execute("""

        SELECT Source, COUNT(*) From (SELECT Source From flights_data
								UNION ALL
								SELECT Destination From flights_data) t
        GROUP BY t.Source
        ORDER BY COUNT(*) DESC
        """)

        data = self.mycursor.fetchall()

        for iteam in data:
            city.append(iteam[0])
            frequnecy.append(iteam[0])

        return city, frequnecy
    


    def daily_frequency(self):
        date = []
        frequnecy = []
        self.mycursor.execute("""

        SELECT  Date_of_Journey, COUNT(*) FROM flights_data
        GROUP BY Date_of_Journey
        """)

        data = self.mycursor.fetchall()

        for iteam in data:
            date.append(iteam[0])
            frequnecy.append(iteam[0])

        return date, frequnecy
    