class QuickSort:

    @classmethod
    def partition(cls, input_array, start: int, end: int):
        if start < end:
            pivot = input_array[end]
            separator_index = start - 1

        for index in range(start, end):
            if input_array[index] <= pivot:
                separator_index += 1
                input_array[separator_index], input_array[index] = input_array[index], input_array[separator_index]
        input_array[separator_index+1], input_array[end] = input_array[end], input_array[separator_index+1]

        return separator_index + 1


    @classmethod
    def quicksort_detailed(cls, input_array: list[int], start: int, end: int):
        if start < end:
            separator_index = cls.partition(input_array, start, end)
            cls.quicksort_detailed(input_array, start, separator_index-1)
            cls.quicksort_detailed(input_array, separator_index+1, end)


    @classmethod
    def quicksort(cls, input_array: list[int]):
        cls.quicksort_detailed(input_array, 0, len(input_array)-1)


def main():
    array = [8, 9, 7, 6, -8, 5, 4, 3, 2, 1]

    QuickSort.quicksort(array)
    print(array)

if __name__=='__main__':
    main()