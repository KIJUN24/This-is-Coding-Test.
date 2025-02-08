#include<iostream>
using namespace std;


void Fun(int* p) {

	for (int i = 0; i<5 ; i++) {
		cout << p[i] << " ";
	}
}

int main(void) {
	int arr[5] = { 5,6,7,8,9 };

	// 배열의 이름 자체가 포인터이므로
	// 배열을 전달하는 것이 아닌
	// 주소를 전달하는 것임.
	Fun(arr);
}
