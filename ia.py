import sys # to get arguments
from bisect import bisect_left      # for binary search

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

from bisect import bisect_left

def binary_search_sublist(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)
    pos = bisect_left(a, [x,], lo, hi)  # find insertion position
    return (pos if pos != hi and a[pos][0] == x else -1)  # don't walk off the end

def scrub_hex_line(line):
    newline = ""
    for char in line:
        if char >= '0' and char <= '9' or char == 'x' or char >= 'a' and char <= 'f':
            newline += char

    # print(line, "->", newline)
    return newline


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
instruction_info_file = sorted(instruction_info_file, key = lambda list: list[0])

# check if sorted
last_address = instruction_info_file[0][0]
for i in range (1,len(instruction_info_file)):
    curr_address = file[i][0]
    if last_address > curr_address:
        print("SORT BROKE!")
        break
print("SORT CHECK OKAY!")



trace_input_file_name = "hello-instructions.txt"
with open(trace_input_file_name ) as f:
    file = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
file = [x.strip() for x in file]

for i in range(0, len(file)):
    x = file[i]
    x = x.split()
    x[0] = "0x" + x[0]  # so that we are adding teh familiar 0x
    file[i] = x

trace_file = file
trace_file.pop(0)       # deletes the first line containing headers

# now we begin to structure and analyze the trace file



# at this point we have two arrays:
# instruction_info_file <--(SORTED)
# trace_file

### USE THIS CODE TO DETERMINE 100% MATCHES BETWEEN INSTRUCTIONS AND TRACE
matches = 0
mismatches = 0
f = open("mismatched_insns_addresses.txt", "w")
total = len(instruction_info_file)

for line in trace_file:
    if "0x" in line[0]:
        pos = binary_search_sublist(instruction_info_file, line[0])
        if pos >= 0:
            matches += 1
            # print(instruction_info_file[pos])
            f.write(str(int(line[0], 16)) + '\n')
        else:
            mismatches += 1
            # print(line[0])

f.close()

print("matces", matches)
print("mismatches", mismatches)
print(str(float(matches)/(matches+mismatches)*100)+"% positive")


### USE THIS CODE TO EXPORT GDB INSTRUCTION ADDRESS COVERAGE TO A TEXT FILE ###
# f = open("gdb_coverage.txt", "w")
# for line in instruction_info_file:
#     if "0x" in line[0]:
#         line[0] = scrub_hex_line(line[0])
#         f.write(str(int(line[0],16)) + '\n')
# f.close()













