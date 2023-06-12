if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    #####################################################################
    # obatains the list of marks under the desired name.
    # Stores the sum as a numerator and the number of
    # entries in list as the denominator.
    #####################################################################
    query_marks = student_marks[query_name]
    numerator = sum(query_marks)
    denominator = len(query_marks)

    # calculates the average and prints it.
    query_avg = numerator / denominator
    final_print = "{:.2f}".format(query_avg)
    print(final_print)
    

