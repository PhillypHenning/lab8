import sys
import os
import hashlib

def main(arg):
    for idx, val in enumerate(reversed(arg[1])):
        if val == '/':
            fileh = arg[1][len(arg[1])-idx:len(arg[1])]
            break
    print('The file within the string "' + arg[1] + '" is: ' + fileh)

    size_of_file = os.path.getsize(arg[1]) or 0
    print('The size of ' + fileh + ' is ' + str(size_of_file) + ' bytes')

    with open(arg[1]) as infile:
        file_content = infile.read()

    sha1hash = hashlib.sha1(file_content)
    md5hash = hashlib.md5(file_content)

    print('sha1 hash of file ' + fileh + ' is [' + sha1hash.hexdigest() + ']')
    print('md5 hash of file ' + fileh + ' is [' + md5hash.hexdigest() + ']')





if __name__ == '__main__':
    main(sys.argv)