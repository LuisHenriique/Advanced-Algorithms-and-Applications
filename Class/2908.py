
# Example of light in the class
bulbs_example = [1,-1,1,-1,1]
def turn_on(bulbs):
    cost  = 0
    for i in range(len(bulbs)):
        b = bulbs[i]
        if cost % 2 != 0:
            b = -b
        if b == -1:
            cost += 1
    return cost

print(turn_on(bulbs_example))


print("Second exercise-----------------")

intervals = [[1,4], [2,3], [4,6], [8,9]]

def distrib(s_intervals):


    s_intervals.sorted(key = lambda x:x[1])
    count = 1

    selected = [s_intervals[0]]

    for i in s_intervals[1:]:
        if i[0] <= selected[-1][1]:
            continue
        count += 1
        selected.append(i)
print(distrib(intervals))
num = [3,34,34,322,4,-1]

print(num.sort())
