from datetime import datetime, timedelta
import os

def process_log_file(filename):
    time_stack = []
    has_time_difference = False

    with open(filename, mode="r", encoding="UTF-8") as log:
        for item in log:
            time_str = item[12:20]
            time_stamp = datetime.strptime(time_str, '%H:%M:%S')
            time_stack.append(time_stamp)
            if len(time_stack) > 1:
                diff = time_stack[1] - time_stack[0]
                if diff >= timedelta(seconds=1800):
                    has_time_difference = True
                    break
                time_stack.pop(0)
 
    if has_time_difference:
        output_filename = "Result_" + os.path.basename(filename)
        with open(filename, mode="r", encoding="UTF-8") as log:
            with open(output_filename, "w") as output_file:
                for entry, item in enumerate(log, 1):
                    time_str = item[12:20]
                    time_stack.append(datetime.strptime(time_str, '%H:%M:%S'))
                    if len(time_stack) > 1:
                        diff = time_stack[1] - time_stack[0]
                        if diff >= timedelta(seconds=1800):
                            output_file.write(f"{entry:02d}:~ {time_str} {diff}\n")
                        time_stack.pop(0)
                    else:
                        output_file.write(f"{entry:02d}:~ Start {time_str}\n")


def run():
    directory = './'
    files = [os.path.join(directory, file) for file in os.listdir(directory) if file.startswith("Access-") and file.endswith(".txt")]
    for file in files:
        process_log_file(file)
    

if __name__ == '__main__':
    run()