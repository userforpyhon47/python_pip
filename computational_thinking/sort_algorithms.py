from utils import gen_data, measure_time
import time


@measure_time
def buble_sort(data: list = []) -> list:
    """Implementation of bubble sort algorithm"""
    sorted_data = data.copy()
    steps = 0
    for i in range(len(sorted_data)):
        for j in range(len(sorted_data)-i-1):
            steps += 1
            if sorted_data[j] > sorted_data[j+1]:
                sorted_data[j], sorted_data[j+1] = sorted_data[j+1], sorted_data[j]
    print(f"Bubble Sort: Taken {steps} steps!")
    return sorted_data


@measure_time
def insertion_sort(data: list = []) -> list:
    """Implementation of insertion sort algorithm"""
    sorted_data = data.copy()
    steps = 0
    for index in range(1, len(sorted_data)):
        steps += 1
        current_value = sorted_data[index]
        current_position = index

        while current_position > 0 and sorted_data[current_position-1] > current_value:
            steps += 1
            sorted_data[current_position] = sorted_data[current_position-1]
            current_position -= 1

        sorted_data[current_position] = current_value

    print(f"Insertion Sort: Taken {steps} steps!")
    return sorted_data


def merge_sort(data: list = []) -> list:
    """Implementation of insertion sort algorithm"""
    steps = 0
    
    if len(data) > 1:
        medio = len(data) // 2
        izquierda = data[:medio]
        derecha = data[medio:]

        # llamada recursiva en cada mitad
        merge_sort(izquierda)
        merge_sort(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            steps += 1
            if izquierda[i] < derecha[j]:
                data[k] = izquierda[i]
                i += 1
            else:
                data[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            steps += 1
            data[k] = izquierda[i]
            i += 1
            k +=1

        while j < len(derecha):
            steps += 1
            data[k] = derecha[j]
            j += 1
            k += 1
    
    return data


if __name__ == "__main__":
    n = 1e10
    condition = n < 1000
    raw_list = gen_data(10000)

    if condition: # Bubble and insertion sort has O(n**2) complexity
        sorted_list_bubble = buble_sort(raw_list)
        sorted_list_insertion = insertion_sort(raw_list)
       
    tic = time.time()
    sorted_list_merge = merge_sort(raw_list.copy())
    toc = time.time()
    print(f"Merge Sort:")
    print(f" └->Elapsed time: {toc-tic}")

    print(raw_list[:10])
    if condition:
        print(sorted_list_bubble[:10])
        print(sorted_list_insertion[:10])

    print(sorted_list_merge[:10])
