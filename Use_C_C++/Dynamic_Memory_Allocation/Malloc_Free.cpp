#include<iostream>
#include<cstdlib>
using namespace std;

int main(void) {
	int* score;
	int n = 0;
	cout << "학생수 입력 : ";
	cin >> n;

	score = (int*)malloc(n * sizeof(int));

	cout << sizeof(score) << endl;
	
	free(score);

	//cout << *score << endl;

	return 0;
}