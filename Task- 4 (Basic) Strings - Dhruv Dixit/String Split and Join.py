def split_and_join(line):
    t=line.split(" ")
    return('-'.join(t))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)