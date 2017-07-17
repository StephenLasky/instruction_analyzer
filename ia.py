import sys # to get arguments

def split_lengths_into_files(file):
    dic = {}

    for line in file:
        length = len(line)
        if length in dic:
            dic[length].append(line)
        else:
            dic[length] = [line]

    for x in dic[8]:
        print(x)

# this will print lines that do not contain an address.
# in our first test, only 6ish lines did not contain an address.
def print_lines_without_address(file):
    for line in file:
        has_address = False
        for token in line:
            if "0x" in token:
                has_address = True
        if has_address == False:
            print(line)

def print_addresses_per_line_stats(file):
    dic = {}
    for line in file:
        number_of_addresses = 0
        for token in line:
            if "0x" in token:
                number_of_addresses += 1
        if number_of_addresses in dic:
            dic[number_of_addresses] += 1
        else:
            dic[number_of_addresses] = 1

    print(dic)

# here we wanted to see how unique addresses are
# in our first trial , it appeared that all first-token addresses were unique
def print_address_occurence_stats(file):
    addresses = []
    for line in file:
        if "0x" in line[0]:
            addresses.append(line[0])

    addresses.sort()

    address_count_dic = {}
    prev_address = addresses[0]
    for i in range(1, len(addresses)):
        curr_address = addresses[i]
        if curr_address == prev_address:
            address_count_dic[curr_address] += 1
        else:
            address_count_dic[curr_address] = 1

    occurence_dic = {}

    for address in address_count_dic:
        occurence = address_count_dic[address]
        if occurence in occurence_dic:
            occurence_dic[occurence] += 1
        else:
            occurence_dic[occurence] = 1

    print(occurence_dic)

def print_address_as_first_token_stats(file):
    yes = 0
    no = 0
    for line in file:
        if "0x" in line[0]:
            yes += 1
        else:
            no += 1

    print("yes: ", yes)
    print("no:  ", no)

# it appears that about 60% of the instructions containt the "<>" cominbation, indicating an informative annotation
def print_lines_that_contain_substring_stats(file,substring):
    yes = 0
    total = len(file)
    for line in file:
        for token in line:
            if substring in token:
                yes += 1
                break

    print("yes:", yes, " percentage: %", float(yes)/total)





# will use default "gdb.txt" if no file name is specified
instruction_input_file_name = "gdb.txt"
if len(sys.argv) > 1:
    input_file_name = sys.argv[1]

with open(instruction_input_file_name ) as f:
    file = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
file = [x.strip() for x in file]

for i in range(0, len(file)):
    x = file[i]
    x = x.split()
    file[i] = x

instruction_info_file = file

trace_input_file_name = "in.txt"
with open(trace_input_file_name ) as f:
    file = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
file = [x.strip() for x in file]

for i in range(0, len(file)):
    x = file[i]
    x = x.split()
    file[i] = x

trace_file = file









