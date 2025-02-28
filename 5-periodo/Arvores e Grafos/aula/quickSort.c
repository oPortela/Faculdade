#include <stdio.h>

void swap(int* a, int* b){
	int temp = *a;
	*a = *b;
	*b = temp;
}

int partition(int arr[], int low, int high) {
	int p = arr[low];
	int i = low;
	int j = high;
	
	while (i < j) {
		while (arr[i] <= p && i <= high - 1) {
			i++;
		}
		
		while (arr[j] > p && j >= low + 1){
			j--;
		}
		if (i < j){
			swap(&arr[i], &arr[j]);
		}
	}
	swap(&arr[low], &arr[j]);
	return j;
}

void quickSort(int arr[], int low, int high){
	if (low < high){
		int pi = partition(arr, low, high);
		
		quickSort(arr, low, pi - 1);
		quickSort(arr, pi + 1, high);
	}
}

int main(){
	int arr[] = {5, 8, 15, 66,98,14,1,0,7};
	int n = sizeof(arr) / sizeof(arr[0]);
	
	for (int i = 0; i < n; i++){
		printf("%d ", arr[i]);
	}
	printf("\n");
	
	quickSort(arr, 0, n -1);
	
	for (int i = 0; i < n; i++){
		printf("%d ", arr[i]);
	}
	
	return 0;
}