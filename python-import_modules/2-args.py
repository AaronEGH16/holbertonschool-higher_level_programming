#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv) - 1) == 0 or (len(sys.argv) - 1) > 1:
        print("{} arguments".format((len(sys.argv) - 1)))
    else:
        print("1 argument")
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, str(sys.argv[i])))
