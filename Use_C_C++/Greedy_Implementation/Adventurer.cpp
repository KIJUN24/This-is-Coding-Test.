#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int n;
vector<int> arr;

int main(void) {
	cin >> n;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		arr.push_back(x);
	}
	sort(arr.begin(), arr.end());

	// 총 그룹의 수
	int result = 0;
	// 현재 그룹에 포함된 모험가의 수
	int cnt = 0;
	// 공포도를 낮은 것부터 하나씩 확인
	for (int i = 0; i < n; i++) {
		// 현재 그룹에 해당하는 모험가를 포함시키기
		cnt += 1;
		// 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
		if (cnt >= arr[i]) {
			// 총 그룹의 수 증가시키기
			result += 1;
			// 현재 그룹에 포함된 모험가의 수 초기화
			cnt = 0;
		}
	}
	cout << result << "\n";
}