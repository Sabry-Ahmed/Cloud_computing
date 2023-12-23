from flask import Flask, jsonify

import mysql.connector

app = Flask(__name__)

# MySQL Configuration
config = {
    'host': 'hmvmdb.mysql.database.azure.com',
    'user': 'test',
    'password': 'H3hitema',
    'database': 'toto',  # Replace 'your_database_name' with your database name
    'ssl_ca': 'DigiCertGlobalRootCA.crt.pem'
}

# Establish a connection to MySQL without specifying a database initially
conn = mysql.connector.connect(host=config['host'], user=config['user'], password=config['password'], ssl_ca=config['ssl_ca'])
cursor = conn.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS toto")  # Replace 'your_database_name' with your desired database name

# Close the previous connection
conn.close()

# Reconnect to the database
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Use the database
cursor.execute("USE toto")  # Replace 'your_database_name' with your desired database name

# Create a table (if it doesn't exist)
cursor.execute("CREATE TABLE IF NOT EXISTS random_numbers (id INT AUTO_INCREMENT PRIMARY KEY, number INT)")

@app.route('/insert_random_number')
def insert_random_number():
    # Generate a random number
    import random
    random_number = random.randint(1, 100)

    # Insert the random number into the table
    cursor.execute("INSERT INTO random_numbers (number) VALUES (%s)", (random_number,))
    conn.commit()

    return jsonify({'message': 'Random number inserted successfully'})

@app.route('/get_random_number')
def get_random_number():
    # Select a random number from the table
    cursor.execute("SELECT number FROM random_numbers ORDER BY RAND() LIMIT 1")
    result = cursor.fetchone()
    if result:
        return jsonify({'random_number': result[0]})
    else:
        return jsonify({'message': 'No random number found'})

if __name__ == '__main__':
    app.run(debug=True)
