#Ian Setia
#isetia@nd.edu

import argparse

def readFile(fileName):
    f = open(fileName, 'r')
    lines = []
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        lines.append(line)
    return lines

def countInclude(lines):
    i = 0
    for line in lines:
        if line.startswith('#include'):
            i+=1
    return i

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('fileName', type=str, help='name of file to scan')
    parser.add_argument('--include', action='store_true', help='counts number of include statements in code')
    args = parser.parse_args()

    lines = readFile(args.fileName)
    
    print("file: {} lines: {}".format(args.fileName, len(lines)), end=' ')

    if args.include:
        print("include: {}".format(countInclude(lines)), end=' ');

    print("")

    
if __name__ == "__main__":
    main()
