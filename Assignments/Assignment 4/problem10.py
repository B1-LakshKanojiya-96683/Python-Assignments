#10. Define a procedure histogram() that takes a list of integers and prints  histogram to the screen.
#For example, histogram([4, 9, 7]) should print the following:
#****
#*********
#*******


def histogram(graph_list):
    for x in graph_list:
        print("*"*x)


histogram([4,9,7])