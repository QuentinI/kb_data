import csv
import datetime
import json
import sys
import random
import string

def genid():
    source = string.ascii_lowercase + string.digits
    return ''.join(random.choice(source) for i in range(32))

with open('flights.csv', newline='') as flights:
    reader = csv.reader(flights)
    next(reader, None) # skip header

    tickets = []

    for row in reader:
        try:
            y, m, d = int(row[0]), int(row[1]), int(row[2])

            # First month only
            if m > 1:
                break

            origin  = row[7]
            destination = row[8]

            departure_hour = int(row[9][0:2])
            departure_minute = int(row[9][2:4])
            arrival_hour = int(row[20][0:2])
            arrival_minute = int(row[20][2:4])

            departure_time = datetime.datetime(y, m, d, departure_hour, departure_minute)
            arrival_time = datetime.datetime(y, m, d, arrival_hour, arrival_minute)

            dist = int(row[17])
            price = int(random.gauss(dist + 1000, 1000))
            if price < 300:
                price = 300

            tickets.append({
                "id": genid(),
                "departure_code": origin,
                "arrival_code": destination,
                "departure_time": int(departure_time.timestamp()),
                "arrival_time": int(arrival_time.timestamp()),
                "price": price
            })

        except Exception as e:
            print("Error processing row: ", e, file=sys.stderr)

    print(json.dumps({ "tickets": tickets}))
