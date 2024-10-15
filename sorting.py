import sys

def init_code():
    try:
        sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'w')
    except FileNotFoundError:
        pass  # Ignore if running in an online judge without input/output files




def bubble_sort(arr):
	for i in range(0,len(arr)):
		for j in range(0,len(arr)-i-1):
			if arr[j] > arr[j+1]:
				arr[j] ,arr[j+1] = arr[j+1] ,arr[j]

	return arr


def selection_sort(arr):
	n = len(arr)

	for i in range(0, len(arr)-1):
		min_index  =  i
		for j in range(i+1,n):
			if arr[min_index] > arr[j]:
				min_index = j
     
		arr[i], arr[min_index] = arr[min_index] , arr[i]

	return arr

def insertion_sort(arr):
	n = len(arr)

	for i in range(1,n):
		key = arr[i]
		j = i-1

		while j>=0 and arr[j] > key:
			arr[j+1] = arr[j]
			j = j-1

		arr[j+1] = key

	return arr

def merge_sort(arr):
	
	if len(arr) <= 1:
		return arr

	mid = len(arr)//2
	left_half = arr[:mid]
	right_half = arr[mid:]

	left_half = merge_sort(left_half)
	right_half = merge_sort(right_half)

	return merge(left_half,right_half)



def merge(left, right):
	merged = []
	i = j = 0
	while i<len(left) and j<len(right):
		if left[i] < right[j]:
			merged.append(left[i])
			i = i + 1
		else:
			merged.append(right[i])
			j = j + 1

	merged = merged + left[i:]
	merged = merged + right[j:]

	return merged

def partition(arr,low,high):
	pivot = arr[high]
	i = low - 1

	for j in range(low , high):
		print("j=",j)
		if arr[j] < pivot:
			i = i + 1
			arr[j] ,arr[i] = arr[i] ,arr[j]
			print(arr)

	arr[i+1], arr[high] = arr[high],arr[i+1]
	print(arr)
	return i+1



def quick_sort(arr, low, high):

	if low < high:
		pivot = partition(arr,low,high)
		quick_sort(arr,low,pivot-1)
		quick_sort(arr,pivot+1,high)

	return arr



def main():
    init_code()
    arr = [4,7,2,1,9,3]
    low = 0
    high = len(arr)-1
    newarr = quick_sort(arr, low, high)
    print(newarr)



if __name__ == "__main__":
	main()