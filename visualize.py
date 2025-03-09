import sqlite3
import time
import random
import statistics
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def enable_wal_mode():
    conn = sqlite3.connect('metrics.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA journal_mode=WAL;")
    conn.close()

enable_wal_mode()

def create_table():
    conn = sqlite3.connect('metrics.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
            timestamp REAL PRIMARY KEY,
            packet_loss REAL,
            latency REAL,
            packet_gain REAL
            )
    ''')
    conn.commit()
    conn.close()

create_table()

def insert_data(packet_loss, latency, packet_gain):
    conn = sqlite3.connect('metrics.db')
    cursor = conn.cursor()
    timestamp = time.time()
    try:
        cursor.execute('''
            INSERT INTO metrics (timestamp, packet_loss, latency, packet_gain)
            VALUES (?, ?, ?, ?)
        ''', (timestamp, packet_loss, latency, packet_gain))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Timestamp {timestamp} already exists. Skipping insertion.")
        conn.rollback()
    finally:
        conn.close()

@app.route('/')
def index():
    return render_template('index.html')

last_insert_time = 0
insert_interval = 2 

@app.route('/data')
def get_data():
    conn = sqlite3.connect('metrics.db')
    cursor = conn.cursor()
    global last_insert_time
    current_time = time.time()

    # Generate random metrics data including CPU usage
    packet_loss = random.uniform(0, 20)
    latency = random.uniform(0, 200)
    packet_gain = random.uniform(0, 10)
    
    if current_time - last_insert_time >= insert_interval:
        insert_data(packet_loss, latency, packet_gain)
        last_insert_time = current_time

    insert_data(packet_loss, latency, packet_gain)

    cursor.execute('SELECT * FROM metrics ORDER BY timestamp DESC LIMIT 50')
    rows = cursor.fetchall()
    conn.close()

    data = [{'timestamp': row[0], 'packet_loss': row[1], 'latency': row[2], 'packet_gain': row[3]} for row in rows]

    if data:
        packet_loss_values = [row['packet_loss'] for row in data]
        latency_values = [row['latency'] for row in data]
        packet_gain_values = [row['packet_gain'] for row in data]
        
        stats = {
            'packet_loss': {
                'average': statistics.mean(packet_loss_values),
                'stddev': statistics.stdev(packet_loss_values) if len(packet_loss_values) > 1 else 0,
                'min': min(packet_loss_values),
                'max': max(packet_loss_values),
            },
            'latency': {
                'average': statistics.mean(latency_values),
                'stddev': statistics.stdev(latency_values) if len(latency_values) > 1 else 0,
                'min': min(latency_values),
                'max': max(latency_values),
            },
            'packet_gain': {
                'average': statistics.mean(packet_gain_values),
                'stddev': statistics.stdev(packet_gain_values) if len(packet_gain_values) > 1 else 0,
                'min': min(packet_gain_values),
                'max': max(packet_gain_values),
            },
        }
    else:
        stats = {
            'packet_loss': {'average': 0, 'stddev': 0, 'min': 0, 'max': 0},
            'latency': {'average': 0, 'stddev': 0, 'min': 0, 'max': 0},
            'packet_gain': {'average': 0, 'stddev': 0, 'min': 0, 'max': 0},
                }

    return jsonify({'data': data, 'stats': stats})

if __name__ == '__main__':
    app.run(debug=True)