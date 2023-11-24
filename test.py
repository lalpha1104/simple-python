from datetime import datetime, timedelta
import sys

time_stack = []

with open("Access-LynseyWood.txt", mode="r", encoding="UTF-8") as log:
    with open("output.txt", "w") as output_file:
        for entry, item in enumerate(log, 1):
            time_str = item[12:20]
            time_stamp = datetime.strptime(time_str, '%H:%M:%S')
            time_stack.append(time_stamp)
            if len(time_stack) > 1:
                diff = time_stack[1] - time_stack[0]
                if diff >= timedelta(seconds=1800):
                    output_file.write(f"{entry:02d}:~ {time_str} {diff}\n")
                time_stack.pop(0)
            else:
                output_file.write(f"{entry:02d}:~ Start {time_str}\n")