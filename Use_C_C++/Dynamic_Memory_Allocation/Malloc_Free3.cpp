#include<iostream>
#include<cstdlib>
using namespace std;

int main(void) {
	int n;

	cout << "배열 크기 입력 : ";
	cin >> n;

	int* arr;
	arr = (int*)malloc(n*sizeof(int));

	if (arr == nullptr) {
		cout << "메모리 할당이 안 되었습니다." << endl;
		return 1;
	}

	cout << n << "개의 정수를 입력하세요 : ";
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	cout << "입력한 값 : ";
	for (int i = 0; i < n; i++) {
		cout << arr[i] << " ";
	}
	cout << endl << endl;

	free(arr);
	cout << "메모리 해제 완료" << endl;

	return 0;
}