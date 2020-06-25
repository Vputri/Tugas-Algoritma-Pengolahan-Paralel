def quicksort(tengah, awal, akhir):
    if akhir - awal > 1:
        p = partition(tengah, awal, akhir)
        quicksort(tengah, awal, p)
        quicksort(tengah, p + 1, akhir)
 
 
def partition(tengah, awal, akhir):
    pivot = tengah[awal]
    i = awal + 1
    j = akhir - 1
 
    while True:
        while (i <= j and tengah[i] <= pivot):
            i = i + 1
        while (i <= j and tengah[j] >= pivot):
            j = j - 1
 
        if i <= j:
            tengah[i], tengah[j] = tengah[j], tengah[i]
        else:
            tengah[awal], tengah[j] = tengah[j], tengah[awal]
            return j
 
 
urut = input('Enter the list of numbers: ').split()
urutan = [int(x) for x in urut]
quicksort(urutan, 0, len(urutan))
print('Sorted list: ', end='')
print(urutan)
