# https://radiusofcircle.blogspot.com/2017/05/project-euler-problem-68-solution-with-python.html

'''
For our convinience we will name each and every circle with letters - 
a, b, c, d, e, f
So a + b + c == d + c + e == f + e + b



In this way for each and every combination of a, b, c you will get different 
d, e, f. We will maintain a list of all these combinations as avail_sol so 
that we can compute the largest value at the end.

Now it is easy to imagine having different combinations of a, b, c, d, e, f. 
It should be noted here that we need only combinations and not permutations. 
With some iterations we will get the same numbers in a jumbled fashion. 
To overcome this problem, the question already states the solution - 
"Working clockwise, and starting from the group of three with the numerically 
lowest external node", so we will first have to find the numerically external 
node and then working clockwise arrange the numbers.

To tackle this problem, we will write a function, which will take a, b, c, d, e, f 
as input and arrange them as per requirement.
'''
# 3-gon ring

numbers = [1, 2, 3, 4, 5, 6]

# list of all combinations available
avail_sol = []

def convert_to_num(a, b, c, d, e, f):
    """
        This function will start with the
        numerically lowest external node,
        moving clockwise arrange the numbers
        on the given line.
    """
    big_num = {a:0, d:1, f:2}
    break_num = big_num[min(big_num.keys())]
    nums = [(a, b, c), (d, c, e), (f, e, b)]
    nums = nums[break_num:]+nums[:break_num]
    string = ''
    for num_tup in nums:
        for num in num_tup:
            string += str(num)
    return string

# iterate through values of a
for a in numbers:
    # duplicate the numbers list
    # so that we can use it for b
    numbers_b = numbers[:]
    # numbers_b should not have a
    numbers_b.remove(a)
    # iterate through values of b
    for b in numbers_b:
        # duplicate the numbers_b list
        # so that we can use it for c
        numbers_c = numbers_b[:]
        # remove b from numbers_b
        # numbers_c will not have a, b
        numbers_c.remove(b)
        # iterate through values of c
        for c in numbers_c:
            # sum of lines - line_sol
            line_sol = a + b + c
            # duplicate the numbers_c list
            # numbers_d will not have a, b, c
            numbers_d = numbers_c[:]
            numbers_d.remove(c)
            for d in numbers_d:
                # similarly numbers_e
                numbers_e = numbers_d[:]
                numbers_e.remove(d)
                # but according to above image
                # e = line_sol - c - d
                e = line_sol - c - d
                # check if e is in line_e
                # this is to check if the combination
                # of a, b, c will form magic gon
                if e in numbers_e:
                    # create numbers_f
                    numbers_f = numbers_e[:]
                    # numbers_f should only contain
                    # 1 number
                    numbers_f.remove(e)
                    # but according to image
                    # f = line_sol - e - b
                    f = line_sol - e - b
                    # check if f is in numbers_f
                    if f in numbers_f:
                        # convert the combination
                        # using convert_to_num func
                        temp = convert_to_num(a, b, c, d, e, f)
                        avail_sol.append(temp)
           
# solution will be the maximum of all the numbers
sol = max([int(x) for x in avail_sol])
print(sol)



# time module
import time

# time at the start of program execution
start = time.time()

# 5-gon ring
# numbers from 1-10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def convert_to_num(a, b, c, d, e, f, g, h, i, j):
    """
    Function to convert a-j to
    required string based on the criteria
    """
    big_num = {a:0, d:1, f:2, h:3, j:4}
    break_num = big_num[min(big_num.keys())]
    nums = [(a,b,c), (d,c,e), (f,e,g), (h,g,i), (j,i,b)]
    nums = nums[break_num:]+nums[:break_num]
    string = ''
    for num_tup in nums:
        for num in num_tup:
            string += str(num)
    return string

# list to store solutions
avail_sol  = []

# start with all the numbers
for a in numbers:
    numbers_b = numbers[:]
    numbers_b.remove(a)
    # numbers without a
    for b in numbers_b:
        numbers_c = numbers_b[:]
        numbers_c.remove(b)
        # numbers without a, b
        for c in numbers_c:
            line_sum = a+b+c
            numbers_d = numbers_c[:]
            numbers_d.remove(c)
            # numbers without a, b, c
            for d in numbers_d:
                numbers_e = numbers_d[:]
                numbers_e.remove(d)
                e = line_sum - c - d
                # numbers without a, b, c, d
                if e in numbers_e:
                    numbers_f = numbers_e[:]
                    numbers_f.remove(e)
                    # numbers without a, b, c, d, e
                    for f in numbers_f:
                        numbers_g = numbers_f[:]
                        numbers_g.remove(f)
                        g = line_sum - e - f
                        # numbers without a, b, c, d, e, f
                        if g in numbers_g:
                            numbers_h = numbers_g[:]
                            numbers_h.remove(g)
                            # numbers without a, b, c, d, e, f, g
                            for h in numbers_h:
                                numbers_i = numbers_h[:]
                                numbers_i.remove(h)
                                i = line_sum - g - h
                                # check if i is in numbers_i list
                                if i in numbers_i:
                                    j = line_sum - i - b
                                    numbers_j = numbers_i[:]
                                    numbers_j.remove(i)
                                    # numbers without a, b, c, d, e, f, g, h, i
                                    if j in numbers_j:
                                        ctn = convert_to_num(a, b, c, d, e, f, g, h, i, j)
                                        avail_sol.append(ctn)

# solution will be the maximum of all the numbers
sol = max([int(x) if len(x) == 16 else 0 for x in avail_sol])

# print the solution
print("Answer: " , sol)

# time at the end
end = time.time()

# total time taken
print("Time taken: " , end - start)