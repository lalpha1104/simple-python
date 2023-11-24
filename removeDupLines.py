def run():
    input_file_path = "./ping.txt"
    # Open the input file and read the lines
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Create a set to store unique lines and a list to maintain the order
    unique_lines_set = set()
    unique_lines_list = []

    # Iterate through the lines and add them to the set and list
    for line in lines:
        if line not in unique_lines_set:
            unique_lines_set.add(line)
            unique_lines_list.append(line)

    # Open the input file in write mode to update its contents with unique lines
    with open(input_file_path, 'w') as file:
        for line in unique_lines_list:
            file.write(line)

if __name__ == '__main__':
    run()