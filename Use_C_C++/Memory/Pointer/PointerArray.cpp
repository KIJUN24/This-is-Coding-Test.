// 포인터로 배열을 만들 수 있다.
// 포인터배열은 배열 안에 주소를 저장하는 것이다.

#include<iostream>
using namespace std;

int main(void) {

	int* p[5];

	int a, b, c, d, e;
	a = 5, b = 10, c = 15, d = 20, e = 50;

	p[0] = &a;
	p[1] = &b;
	p[2] = &c;
	p[3] = &d;
	p[4] = &e;

	for (int i = 0; i < 5; i++) {
		cout << *p[i] << " ";
	}
}