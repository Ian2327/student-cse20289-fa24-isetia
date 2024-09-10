#Ian Setia
#isetia@nd.edu

import os, subprocess, argparse, csv

def run_searchsrc_subprocess(file_path, file_name):
    full_path = os.path.join(file_path, file_name)  #combines file path and name
    #command to be run by subprocess
    command = ['python3', 'searchsrc.py', full_path, '--include', '--includelocal', '--memberfuncs', '--onelinefuncs']
    result = subprocess.run(command, stdout=subprocess.PIPE)
    
    #converts to string
    output = result.stdout.decode('utf-8')

    output_dict = {}
    for line in output.split('\n'):
        if ': ' in line:
            key, value = line.split(': ', 1)
            output_dict[key] = value

    return output_dict

#prints the the dictionary given, given that it contains all necessary information
def print_dict(d):
    print("{}, {}, {} LOC, {} I, {} LI, {} MF, {} OLF".format(d.get('path'), d.get('file'), d.get('lines'), d.get('include'), d.get('includelocal'), d.get('memberfuncs'), d.get('onelinefuncs')))

#reads the .cc files in a given directory and returns a dictionary of dictionsaries
def dir_reader(dir_path, isQuiet, isRecursive):
    dir_files = []
    for dirpath, dirnames, filename in os.walk(dir_path):
        for files in filename:
            if(files.endswith(".cc")):
                result = run_searchsrc_subprocess(dirpath, files);
                if not isQuiet:
                    print_dict(result)

                dir_files.append(result)
        if not isRecursive:
            break

    return dir_files

def output_csv(file_list, csv_name):
    with open(csv_name, 'w', newline='') as csvfile:
        fieldnames = ['path', 'file', 'lines', 'include', 'includelocal', 'memberfuncs', 'onelinefuncs']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        writer.writerows(file_list)


def main():
    parser = argparse.ArgumentParser()

    #adds argument tags to identify from command line
    parser.add_argument('directory', type=str, help='directory to analyze')
    parser.add_argument('-r', action='store_true', help='denotes if directories should be processed recursively (default=false)')
    parser.add_argument('--csv', type=str, default=None, help='denotes to output csv file (default=false)')
    parser.add_argument('--stats', action='store_true', help='denotes if statistics should be computed across each of the numeric fields and reported (default=false)')
    parser.add_argument('--quiet', action='store_true', help='requests output to stay quiet (default=false)')

    args = parser.parse_args()
    
    file_list = dir_reader(args.directory, isQuiet=args.quiet, isRecursive=args.r);
    if args.csv:
        output_csv(file_list, args.csv)
    
    


if __name__ == "__main__":
    main()
