# Create a function called mergesort that takes a list and sorts it.

# Example:
# input [54, 26, 93, 17, 77, 31, 44, 55, 20]
# result [17, 20, 26, 31, 44, 54, 55, 77, 93]


def mergesort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2

        lefthalf = lst[:mid]
        righthalf = lst[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                lst[k] = lefthalf[i]
                i += 1
            else: #lefthalf[i] > righthalf[j]:
                lst[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            lst[k] = lefthalf[i]
            i += 1
            k += 1
            

        while j < len(righthalf):
            lst[k] = righthalf[j]
            j += 1
            k += 1

    return lst

print(mergesort([54, 45, 26, 36]))
