#include<iostream>
using namespace std;

int main(void) {
	int a = 5;
	double d = 3.5;

	cout << "a:" << a <<  "  " << "d:" << d << endl;

	int* p = &a;
	double* ptr = &d;

	*p = 8;
	*ptr = 1.25;

	cout << "a:" << a << "  " << "d:" << d << "\n";

}