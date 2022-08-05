#include <bits/stdc++.h>

const int dx[4] = { 1,0,-1,0 };
const int dy[4] = { 0,-1,0,1 };

using namespace std;

int N, M, k;
set<pair<pair<int, int>, pair<int, int>>> s;

long long dp[101][101];
long long dfs(int r, int c) {
	if (r == M && c == N) {
		return 1;
	}

	long long& ret = dp[r][c];
	if (ret != 0) return ret;

	int nx = c + 1;
	int ny = r;

	if (nx <= N && s.count({ {c,r},{nx,ny} }) == 0) ret += dfs(r, c + 1);

	nx--;
	ny++;

	if (ny <= M && s.count({ {c,r},{nx,ny} }) == 0) ret += dfs(r + 1, c);

	return ret;
}


int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(false);
	cin >> N >> M >> k;
	for (int i = 0; i < k; i++) {
		int a, b, c, d;
		cin >> a >> b >> c >> d;

		if (a > c || b > d) {
			swap(a, c); swap(b, d);
		}
		s.insert({ {a,b},{c,d} });
	}

	cout << dfs(0, 0);
	

	return 0;
}