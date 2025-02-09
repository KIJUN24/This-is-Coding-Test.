#include<iostream>
using namespace std;

#define NULL 0

void Fun(int* p, int size) {
	for (int i = 0; i < 5; i++) {
		cout << p[i] << " ";
	}
}

// 포인터의 주소를 받는 것이므로 이중 포인터로 받아야 한다.
void Dummy(int** p1, int size1, int *p2, int size2) {
	for (int i = 0; i < 5; i++) {
		p1[i] = &p2[i];

		cout << *p1[i] << " ";
	}
	cout << endl;
	p1[3] = &p2[1];
	cout << *p1[3] << endl;
}

int main(void) {
	int arr[5] = { 1,2,3,4,5 };
	int* ptr[5] = { NULL };

	Fun(arr, 5);
	cout << endl;
	Dummy(ptr, 5, arr, 5);
}