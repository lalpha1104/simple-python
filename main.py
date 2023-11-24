from datetime import datetime, timedelta
import os

def is_without_x_minutes(timestamp, x):
    current_time = datetime.now()
    return abs(current_time - timestamp) < timedelta(minutes=x)

def run():
    input_file_path = "./ping.txt"
    output_file_path = "./result.txt"

    with open(input_file_path, 'r') as f:
        lines = f.readlines()

    timestamps_without_x_minutes = []

    for line in lines[1:]:  # Skip the header line
        parts = line.strip().split(',')
        timestamp_str = parts[0].strip('"')
        timestamp = datetime.strptime(timestamp_str, "%d.%m.%Y %H:%M:%S")
        if is_without_x_minutes(timestamp, 20):  # 20 being in minutes
            timestamps_without_x_minutes.append(line)

    if timestamps_without_x_minutes:
        with open(output_file_path, 'w') as result_file:
            result_file.write(lines[0])  # Write the header line
            for line in timestamps_without_x_minutes:
                result_file.write(line)

if __name__ == '__main__':
    run()