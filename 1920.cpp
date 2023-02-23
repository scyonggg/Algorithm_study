#include <iostream>
#include <algorithm>

using namespace std;

void ShowArray(const int arr[], int n) {
    for(int i = 0; i < n; i++) {
        cout << arr[i] << ' ';
    }
    cout << '\n';
}

void SortArray(int arr[], int n) {
    int tmp;
    for(int i = 1; i < n; i++) {
        int j = 0;
        while(j < i) {
            if(arr[i] < arr[j]) {
                tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
                continue;
            }
            j++;
        }
    }
}

bool BinarySearch(const int arr1[], int n, int target) {
    int pl = 0;
    int pr = n - 1;

    do {
        int pc = (pl + pr) / 2;
        if(arr1[pc] == target) return true;
        else if(arr1[pc] < target) {
            pl = pc + 1;
        }
        else if(arr1[pc] > target) {
            pr = pc - 1;
        }
    } while(pl <= pr);
    return false;
}

void Search(const int arr1[], const int n, const int arr2[], const int m) {
    bool result;
    for(int j = 0; j < m; j++) {
        result = BinarySearch(arr1, n, arr2[j]);
        if(result) cout << '1' << '\n';
        else cout << '0' << '\n';
    }
}

int main(){
    int n;  // number of elements
    cin >> n;

    int *narr = new int[n];
    for(int i = 0; i < n; i++) {
        cin >> narr[i];
    }

    int m;  // number of elements
    cin >> m;

    int *marr = new int[m];
    for(int i = 0; i < m; i++) {
        cin >> marr[i];
    }
    
    // SortArray(narr, n);  // Too slow
    sort(narr, narr + n);
    Search(narr, n, marr, m);

    delete [] narr;
    delete [] marr;
}