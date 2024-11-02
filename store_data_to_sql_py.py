import mysql.connector
import pandas as pd
import time

# CONSTANTS
database_name = 'redbus_REDBUS'  # Confirmed database name without extra characters
table_name = 'bus_routes'
csv_path = r'D:\redbus\03_cleaned_data.csv'  # Use raw string to avoid issues with backslashes

# SQL Queries
create_db_query = """CREATE DATABASE IF NOT EXISTS PROJECT_REDBUS"""
create_table_query = """
CREATE TABLE IF NOT EXISTS bus_routes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state TEXT NOT NULL,
    route_name TEXT NOT NULL,
    route_link TEXT NOT NULL,
    bus_name TEXT NOT NULL,
    bus_type TEXT NOT NULL,
    departing_time TIME NOT NULL,
    duration TEXT NOT NULL,
    reaching_time TIME NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    star_rating FLOAT NOT NULL,
    seats_available INT NOT NULL
)
"""
truncate_table_query = f"TRUNCATE TABLE {table_name}"
insert_data_query = """
INSERT INTO bus_routes (
    state, route_name, route_link, bus_name, bus_type, 
    departing_time, duration, reaching_time, price, 
    star_rating, seats_available
) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    state = VALUES(state),
    route_name = VALUES(route_name),
    route_link = VALUES(route_link),
    bus_name = VALUES(bus_name),
    bus_type = VALUES(bus_type),
    departing_time = VALUES(departing_time),
    duration = VALUES(duration),
    reaching_time = VALUES(reaching_time),
    price = VALUES(price),
    star_rating = VALUES(star_rating),
    seats_available = VALUES(seats_available)
"""

# Functions
def read_data_in_chunks(csv_path, chunks=1000):
    """Read CSV data in chunks to manage memory usage."""
    return pd.read_csv(csv_path, chunksize=chunks)

def insert_data_to_sql(cursor, insert_data_query, chunk):
    """Insert a chunk of data into the SQL table."""
    try:
        cursor.executemany(insert_data_query, chunk)
        return True
    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")
        return False

def disable_indexes_and_keys(cursor, table_name, enable=True):
    """Enable or disable indexes for improved performance during bulk inserts."""
    if enable:
        cursor.execute(f'ALTER TABLE {table_name} ENABLE KEYS')
        print(f"Indexes enabled on table {table_name}")
    else:
        cursor.execute(f"ALTER TABLE {table_name} DISABLE KEYS")
        print(f"Indexes disabled on table {table_name}")

# Main script
try:
    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port=3306  # Adjust if necessary
    )
    if db.is_connected():
        print("Connected to the database successfully.")
        cursor = db.cursor(buffered=True)

        # Create database and table
        cursor.execute(create_db_query)
        db.database = database_name
        cursor.execute(create_table_query)

        # Truncate table to start fresh
        cursor.execute(truncate_table_query)
        print(f"Table {table_name} truncated successfully.")

        # Disable indexes and keys for faster insert performance
        disable_indexes_and_keys(cursor, table_name, enable=False)

        # Insert data from CSV in chunks
        chunk_data = read_data_in_chunks(csv_path)
        start_time = time.time()
        chunk_count = 0

        for chunk in chunk_data:
            chunk_count += 1
            data_tuple = [tuple(row) for row in chunk.values]
            if insert_data_to_sql(cursor, insert_data_query, data_tuple):
                db.commit()
                print(f"Chunk {chunk_count} inserted successfully.")
            else:
                print(f"Chunk {chunk_count} failed to insert.")

        # Enable indexes and keys after inserting data
        disable_indexes_and_keys(cursor, table_name, enable=True)
        
        # Total insertion time
        end_time = time.time()
        print(f"Data insertion completed in {end_time - start_time:.2f} seconds.")

    else:
        print("Failed to connect to the database")

except mysql.connector.Error as err:
    print(f"Database error: {err}")

finally:
    # Close the cursor and database connection
    if db.is_connected():
        cursor.close()
        db.close()
        print("Database connection closed.")
