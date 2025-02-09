// 포인어 선언시 괄호 유무의 차이가 있음.

#include<iostream>
using namespace std;

int main(void) {
	int a[3][2];
	int b[4][3];

	// 포인터 p는 int형의 자료를 2개씩 점프하는 포인터이다.
	int (*p1)[2];
	p1 = a;
	p1[0][0] = 3;
	p1[0][1] = 4;

	for (int i = 0; i < 2; i++) {
		cout << p1[0][i] << " ";
	}

	// 포인터 p는 int형의 자료를 3개씩 점프하는 포인터이다.
	int (*p2)[3];
	p2 = b;


}