#include<iostream>
using namespace std;

void MaxAndMin(int* maxPtr, int* minPtr, int *arr) {
	*maxPtr = arr[0];
	*minPtr = arr[0];

	for (int i = 1; i < 5; i++) {
		if (arr[i] > *maxPtr) {
			*maxPtr = arr[i];
		}
		if (arr[i] < *minPtr) {
			*minPtr = arr[i];
		}
	}
}

int main(void) {

	int* maxPtr = nullptr;
	int* minPtr = nullptr;
	int arr[5] = { 1,2,3,4,5 };


	/*for (int i = 0; i < 5; i++) {
		cin >> arr[i];
	}*/


	MaxAndMin(maxPtr, minPtr, arr);

	cout << "최댓값: " << *maxPtr << " (주소: " << maxPtr << ")" << endl;
	cout << "최솟값: " << *minPtr << " (주소: " << minPtr << ")" << endl;

}