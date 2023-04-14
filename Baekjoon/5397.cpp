#include <iostream>
#include <list>
#include <string>

using namespace std;

void PrintList(list<char> list) {

	for (auto c : list) {
		cout << c;
	}
	cout << '\n';

}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int t;
	cin >> t;

	while (t--) {
		list<char> clist;
		list<char>::iterator citer = clist.begin();
		string str;
		cin >> str;

		for (int i = 0; i < str.size(); i++) {
			if (str[i] == '-') {
				if (citer != clist.begin()) citer = clist.erase(--citer);
			}
			else if (str[i] == '<') {
				if (citer != clist.begin()) citer--;
			}
			else if (str[i] == '>') {
				if (citer != clist.end()) citer++;
			}
			else {
				clist.insert(citer, str[i]);
			}
		}
		PrintList(clist);
	}


	return 0;
}