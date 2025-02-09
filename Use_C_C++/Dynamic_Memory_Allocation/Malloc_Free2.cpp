#include<iostream>
#include<cstdlib>
using namespace std;

int main(void) {

	int* p = (int*)malloc(sizeof(int));

	if (p == nullptr) {
		cout << "메모리 할당 실패" << endl;
		return 1;
	}

	*p = 42;
	cout << "할당된 메모리의 값 : " << *p << endl;

	free(p);
	cout << "메모리 해제 완료" << endl;

	return 0;
}