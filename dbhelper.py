import mysql.connector

class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',  # Update this if needed
                database='flight'
            )
            self.mycursor = self.conn.cursor()
            print('Database connection established')

        except mysql.connector.Error as e:
            print('Connection error:', e)


    def fetch_city_names(self):
        city = []
        try:
            self.mycursor.execute("""
            SELECT DISTINCT(Destination) FROM flights_data
            UNION 
            SELECT DISTINCT(Source) FROM flights_data;
            """)

            data = self.mycursor.fetchall()
            city = [item[0] for item in data]
        except mysql.connector.Error as e:
            print("SQL Error in fetch_city_names:", e)
        
        return city
    

    def fetch_all_flights(self, source, destination):
        try:
            self.mycursor.execute("""
            SELECT Airline, Route, Dep_Time, Duration, Price FROM flights_data
            WHERE Source = %s AND Destination = %s
            """, (source, destination))

            return self.mycursor.fetchall()
        except mysql.connector.Error as e:
            print("SQL Error in fetch_all_flights:", e)
            return []
    

    def fetch_airline_frequency(self):
        airline = []
        frequency = []
        try:
            self.mycursor.execute("""
            SELECT Airline, COUNT(*) FROM flights_data
            GROUP BY Airline
            """)

            data = self.mycursor.fetchall()
            for item in data:
                airline.append(item[0])
                frequency.append(item[1])

        except mysql.connector.Error as e:
            print("SQL Error in fetch_airline_frequency:", e)
        
        return airline, frequency
                              

    def busy_airport(self):
        city = []
        frequency = []
        try:
            self.mycursor.execute("""
            SELECT Source, COUNT(*) FROM (
                SELECT Source FROM flights_data
                UNION ALL
                SELECT Destination FROM flights_data
            ) t
            GROUP BY t.Source
            ORDER BY COUNT(*) DESC
            """)

            data = self.mycursor.fetchall()
            for item in data:
                city.append(item[0])
                frequency.append(item[1])  # Fixed

        except mysql.connector.Error as e:
            print("SQL Error in busy_airport:", e)

        return city, frequency
    

    def daily_frequency(self):
        date = []
        frequency = []
        try:
            self.mycursor.execute("""
            SELECT Date_of_Journey, COUNT(*) FROM flights_data
            GROUP BY Date_of_Journey
            """)

            data = self.mycursor.fetchall()
            for item in data:
                date.append(item[0])
                frequency.append(item[1])  # Fixed

        except mysql.connector.Error as e:
            print("SQL Error in daily_frequency:", e)

        return date, frequency
