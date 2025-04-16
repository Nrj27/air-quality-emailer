import os
import json
import datetime

DRIVES = {
    'W': 'Office',
    'X': 'Bedroom',
    'Y': 'Kitchen',
    'Z': 'Outdoor'
}
FILENAME = "latest_config_measurements.json"
FIELDS = [
    "timestamp", "pm01_ugm3", "pm25_ugm3", "pm10_ugm3",
    "voc_ppb", "co2_ppm", "humidity_RH", "temperature_C"
]

def format_timestamp(ts):
    try:
        dt = datetime.datetime.fromisoformat(ts)
        return dt.strftime("%d/%m/%y %H:%M")
    except:
        return "-"

def read_measurement(drive_letter):
    try:
        path = os.path.join(f"{drive_letter}:/", FILENAME)
        with open(path, 'r') as f:
            data = json.load(f)
        values = [format_timestamp(data.get("timestamp", "-"))]
        for field in FIELDS[1:]:
            values.append(str(data.get(field, "-")))
        return values
    except Exception as e:
        print(f"Error reading from {drive_letter}: {e}")
        return ["-"] * len(FIELDS)

def read_all_measurements():
    results = {}
    for drive, location in DRIVES.items():
        results[location] = read_measurement(drive)
    return results
