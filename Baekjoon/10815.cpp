#include <iostream>
#include <algorithm>

using namespace std;

bool BinarySearch(const int arr[], int n, int target) {
    int pl = 0;
    int pr = n - 1;
    int pc;

    do {
        pc = (pl + pr) / 2;
        if(arr[pc] == target) return true;
        else if(arr[pc] < target) pl = pc + 1;
        else if(arr[pc] > target) pr = pc - 1;
    } while(pl <= pr);
    
    return false;
}

void Search(const int narr[], int n, const int marr[], int m) {
    bool result;
    for(int i = 0; i < m; i++) {
        result = BinarySearch(narr, n, marr[i]);
        if(result) cout << "1 ";
        else cout << "0 ";
    }
}

int main() {
    int n;  // number of elements
    cin >> n;

    int *narr = new int[n];
    for(int i = 0; i < n; i++) {
        cin >> narr[i];
    }

    int m;  // number of target elements
    cin >> m;

    int *marr = new int[m];
    for(int i = 0; i < m; i++) {
        cin >> marr[i];
    }

    sort(narr, narr + n);
    Search(narr, n, marr, m);
    delete [] narr;
    delete [] marr;
}