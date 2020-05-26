#!/usr/bin/env python

import argparse
import sys
from os import path


def usergen(names):
    usernames = []
    with open(names) as names:
        n = names.read().splitlines()
        for name in n:
            f, l = name.split(' ', 1)
            a = f[0]
            usernames.append(f + l)
            usernames.append(f + '.' + l)
            usernames.append(f + l)
            usernames.append(a + l)
            usernames.append(l + a)
    return usernames

def output(outfile, usernames):
    wd = outfile.rsplit('/', 1)[0]
    if path.isdir(wd):
        output = open(outfile, "w+")
        for un in usernames:
            output.write(un + "\n")
        output.close()

    else:
        print("{0} is not a valid directory".format(outfile))






if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A small program to generate a list of usernames from names")
    parser.add_argument("-n", "--names", dest="names",
                        help="a file containing a list os peoples names")
    parser.add_argument("-o", "--outfile", dest="outfile",
                        help="File name to save output")
    args = parser.parse_args()

    if args.names is not None:
        names = args.names
        usernames = usergen(names)
    else:
        print('No names file provided')
        parser.print_help(sys.stderr)
        sys.exit(1)


    if args.outfile is not None:
        output(args.outfile, usernames)
    else:
        for un in usernames:
            print(un)
