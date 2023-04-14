#include <iostream>
#include <list>
#include <string>
using namespace std;

int main() {
    list<char> clist;
    list<char>::iterator cursor;

    string str;
    int m;
    cin >> str;
    cin >> m;

    for (int i = 0; i < str.size(); i++) {
        clist.push_back(str[i]);
    }
    cursor = clist.end();

    char cmd;
    while (m--) {
        cin >> cmd;
        if (cmd == 'L') {
            if (cursor != clist.begin()) cursor--;
        }
        else if (cmd == 'D') {
            if (cursor != clist.end()) cursor++;
        }
        else if (cmd == 'B') {
            if (cursor != clist.begin()) cursor = clist.erase(--cursor);
        }
        else if (cmd == 'P') {
            char character;
            cin >> character;
            clist.insert(cursor, character);
        }
    }

    for (list<char>::iterator cptr = clist.begin(); cptr != clist.end(); cptr++) {
        cout << *cptr;
    }

    return 0;
}