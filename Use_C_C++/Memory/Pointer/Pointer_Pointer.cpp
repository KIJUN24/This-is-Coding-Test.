// 이중 포인터
// 주소를 저장하려면 저장하려는 변수보다 *가 하나 더 있어야 한다.

#include<iostream>
using namespace std;

int main(void) {

	int a = 5;
	int* p1 = &a;
	int** p2 = &p1;
	int*** p3 = &p2;

	cout << "a: " << a << endl;
	cout << "*p1: " << *p1 << endl;
	cout << "**p2: " << **p2 << endl;
	cout << "***p3: " << ***p3 << endl;

	**p2 = 6;
	cout << endl << endl;

	cout << "a: " << a << endl;
	cout << "*p1: " << *p1 << endl;
	cout << "**p2: " << **p2 << endl;
	cout << "***p3: " << ***p3 << endl;
}