"""
Prac 04 Practice - Memberwise Addition
"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]

new_list = list1 + list2
print(new_list)


def main():
    add_memberwise([1, 2, 3], [4, 5, 6])
    add_memberwise([1, 2, 3], [1, 2, 3, 4])

def add_memberwise(list1, list2):
    result = []
    max_length = max(len(list1), len(list2))
    for i in range(max_length):
        # Get element from each list if it exists, otherwise use 0
        val1 = list1[i] if i < len(list1) else 0
        val2 = list2[i] if i < len(list2) else 0
        result.append(val1 + val2)
    print(result)

main()