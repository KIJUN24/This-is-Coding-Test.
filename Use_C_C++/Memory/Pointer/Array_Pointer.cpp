#include<iostream>
using namespace std;

int main(void) {
	int a[4] = { 1, 2, 3, 4 };

	for (int i = 1; i < sizeof(a[4])+1; i++) {
		cout << i << " ";
	}

	cout << endl;

	int* p1 = a;
	cout << *p1 << " ";

	int* p2 = a + 1;
	//int* p2 = p1 + 1;
	cout << *p2 << " ";

	int* p3 = a + 2;
	//int* p3 = p2 + 2;
	cout << *p3 << " ";

	int* p4 = p3 + 1;
	cout << *p4 << " ";
}