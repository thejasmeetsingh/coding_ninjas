#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

int getminvertex(bool * visited, int * weight, int v) {
  int minvertex = -1;
  for (int i = 0; i < v; i++) {
    if (visited[i] == 0 && ((minvertex == -1) || (weight[minvertex] > weight[i]))) {
      minvertex = i;
    }
  }
  return minvertex;
}

int main() {
  int v, e;
  cin >> v >> e;
  int ** aj = new int * [v];
  for (int i = 0; i < v; i++) {
    aj[i] = new int[v] {};
  }
  for (int i = 0; i < e; i++) {
    int ei, ej, wt;
    cin >> ei >> ej >> wt;
    aj[ei][ej] = wt;
    aj[ej][ei] = wt;
  }

  bool * visited = new bool[v] {};
  int * parent = new int[v];
  int * weight = new int[v];
  for (int i = 0; i < v; i++) {
    weight[i] = INT_MAX;
    parent[i] = -1;
  }

  parent[0] = -1;
  weight[0] = 0;

  for (int i = 0; i < v - 1; i++) {
    int minvertex = getminvertex(visited, weight, v);
    visited[minvertex] = 1;

    for (int j = 0; j < v; j++) {
      if (aj[minvertex][j] != 0 && visited[j] == 0) {
        if (weight[j] > aj[minvertex][j]) {
          weight[j] = aj[minvertex][j];
          parent[j] = minvertex;
        }
      }
    }
  }

  for (int i = 1; i < v; i++) {
    if (parent[i] < i) {
      cout << parent[i] << " " << i << " " << weight[i] << "\n";
    } else {
      cout << i << " " << parent[i] << " " << weight[i] << "\n";
    }
  }

  delete parent;
  delete visited;
  delete weight;

  return 0;
}
