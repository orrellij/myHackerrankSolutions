def split_and_join(line):
    split = line.split(" ")
    joined = "-".join(split)
    return joined

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)