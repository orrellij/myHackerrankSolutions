def split_and_join(line):
    split = line.split(" ") #splits the string up by spaces
    joined = "-".join(split) #joins the strings split up connecting them with hyphens
    return joined

if __name__ == '__main__': #code stub given by Hackerrank
    line = input()
    result = split_and_join(line)
    print(result)