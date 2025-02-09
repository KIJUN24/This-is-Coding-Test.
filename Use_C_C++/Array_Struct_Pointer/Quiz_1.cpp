#include<iostream>
#include<cmath>
using namespace std;

typedef struct struct_point {
	int x;
	int y;
} point;

double get_distance(point p1, point p2) {
	double result;
	result = sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2));

	return result;
}


int main(void) {
	point p1, p2;

	p1.x = 1;
	p1.y = 2;
	p2.x = 9;
	p2.y = 8;

	cout << get_distance(p1, p2);

}