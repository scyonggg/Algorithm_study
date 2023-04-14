#include <iostream>

using namespace std;

class Node {
	friend class myStack;
private:
	char data;
	Node* next;
};