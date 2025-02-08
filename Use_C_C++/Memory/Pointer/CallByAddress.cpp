#include<iostream>
using namespace std;

void swap(int* p1, int* p2) {
	int temp;

	temp = *p1;
	*p1 = *p2;
	*p2 = temp;
}

int main(void) {
	int a = 3, b = 5;

	cout << "a:" << a << "\t" << "b:" << b << endl;

	swap(&a, &b);

	cout << "a:" << a << "\t" << "b:" << b;
}