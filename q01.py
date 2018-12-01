# Vincent Ren
# 2018-12-01

# ================== Solutions ==================
def part1(inputs):
    
    val = 0

    for input in inputs:
        val += input
        

    return val


# -----------------------------------------------

def part2(inputs):

    val = 0
    s = set()

    while True:
        for input in inputs:
            val += input
            
            if val in s:
                return val

            s.add(val)



# =================== Driver ====================

with open("in01.txt", "r") as f:

    # as single string
    # inputs = f.read()

    # as single int
    # inputs = int(f.read())

    # as lists of ints
    # inputs = [[int(x) for x in row.split()] for row in f.read().split('\n')]

    # as single array of ints
    # inputs = [ int(row) for row in f.read().split('\n')]
    inputs = [ int(row) for row in f.read().split('\n')]

    # as generic list of strings
    # inputs = [[x for x in row.split()] for row in f.read().split('\n')]

    print("\n----------------- input stats -----------------")
    print("len(inputs):", len(inputs))
    # print("row sum", sum(inputs[0]))
    print("inputs[0]:", inputs[0])
    # print("len(inputs[0]):", len(inputs[0]))

    print("\n----------------- solutions -----------------")
    print("part1:", part1(inputs))
    print("part2:", part2(inputs))

    print("\n")