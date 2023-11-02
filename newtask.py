import psycopg2
import pandas

try:

    db_params = {
        'dbname': 'test',
        'user': 'shubham',
        'password': 'shubham',
        'host': '127.0.0.1',
        'port': '5432',
    }
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    df = pandas.read_csv('/home/shubham/Downloads/MOCK_DATA 1.csv')

    for row in df.itertuples(index = False):
        id, first_name, last_name, email, gender = row

        query = f"INSERT INTO mocktesting(id, first_name, last_name, email,gender) VALUES (%s, %s, %s, %s, %s);"

        cursor.execute(query, (id,first_name , last_name, email, gender))

    conn.commit()
    print("Success")

except psycopg2.Error as error:
    print(f"Error: {error} ")

finally:
    cursor.close()
    conn.close()















