#include <iostream>
#include <string>

using namespace std;

int main() {
    // ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);


    float sum = 0.0;
    float div = 0.0;
    for(int i = 0; i < 20; i++){
        string sub;
        float num;
        string grade;

        cin >> sub >> num >> grade;
        // cin.ignore();
        // cout << sub << num << grade;
        if(grade == "P") continue;
        else if(grade == "A+") {sum += num * 4.5; div += num;}
        else if(grade == "A0") {sum += num * 4.0; div += num;}
        else if(grade == "B+") {sum += num * 3.5; div += num;}
        else if(grade == "B0") {sum += num * 3.0; div += num;}
        else if(grade == "C+") {sum += num * 2.5; div += num;}
        else if(grade == "C0") {sum += num * 2.0; div += num;}
        else if(grade == "D+") {sum += num * 1.5; div += num;}
        else if(grade == "D0") {sum += num * 1.0; div += num;}
        else if(grade == "F") {div += num; continue;}
    }

    cout << sum / div;
}