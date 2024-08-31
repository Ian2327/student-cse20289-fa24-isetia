#Ian Setia
#isetia@nd.edu

import argparse

#Reads a given file and returns a list with the lines in the file
def readFile(fileName):
    f = open(fileName, 'r')
    lines = []
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        lines.append(line)
    return lines

#Scans each line in the list of lines for the #include
def countInclude(lines):
    i = 0
    for line in lines:
        if line.startswith('#include'):
            i+=1
    return i

#Counts number of :: substrings present in every line, returns sum
def countMember(lines):
    m = 0
    for line in lines:
        m+=line.count('::')
    return m

#Similar to countMember (searches for -> instead of ::) returns pointer count
def countPtr(lines):
    p = 0
    for line in lines:
        p+=line.count('->')
    return p
    

def countSimplefunc(lines):
    return 100
    
def countSimplefuncec(lines):
    return 100

def main():
    parser = argparse.ArgumentParser()

    #adds argument tags to identify from command line
    parser.add_argument('fileName', type=str, help='name of file to scan')
    parser.add_argument('--include', action='store_true', help='counts number of include statements in code')
    parser.add_argument('--member', action='store_true', help='')
    parser.add_argument('--ptr', action='store_true', help='')
    parser.add_argument('--simplefunc', action='store_true', help='')
    parser.add_argument('--simplefuncec', action='store_true', help='')

    args = parser.parse_args()

    lines = readFile(args.fileName)
    
    print("file: {} lines: {}".format(args.fileName, len(lines)), end=' ')

    if args.include:
        print("include: {}".format(countInclude(lines)), end=' ')
    if args.member:
        print("member: {}".format(countMember(lines)), end=' ')
    if args.ptr:
        print("ptr: {}".format(countPtr(lines)), end=' ')
    if args.simplefunc:
        print("simplefunc: {}".format(countSimplefunc(lines)), end=' ')
    if args.simplefuncec:
        print("simplefuncec: {}".format(countSimplefuncec(lines)), end=' ')

    print("")

    
if __name__ == "__main__":
    main()
