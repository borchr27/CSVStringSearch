"""
Shoutout to aabiddanda for the help / writting this script!

    Getting values out of CSV file
    Input:
        keys- list of strings to match lines with 
        csv_file - file with lines to match
    Output:
        valid_lines - lines which contain all keywords provided
        lines - list of all lines in file
"""
def keyword_search(keys, csv_file):
    keys_lst = keys.lower().split()
    # Only take the description part of the line (splitting on the first comma)
    lines = [line.split(',')[0] for line in open(csv_file, 'r')]
    # list of counters for number of keywords found in each line
    cnts = [0 for i in range(len(lines))]
    for k in keys_lst:
        # loop through all the keys
        for i in range(len(lines)):
            # check if the key is in the i'th line
            if k in lines[i]:
                cnts[i] += 1 # update count if key is found
    # get index of lines which contain all the keys
    max_idx = [i for i, j in enumerate(cnts) if (j == len(keys_lst))]
    valid_lines = [lines[i] for i in max_idx]
    return(valid_lines, lines)
     
# Running an example 
valid_lines , _ = keyword_search('robotic aluminum', 'CMC cycle time data.csv')
print(valid_lines)
valid_lines , _ = keyword_search('robotic weld', 'CMC cycle time data.csv')
print(valid_lines)
