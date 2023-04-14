#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <sstream>

using namespace std;

class Node {
	friend class Stack;
private:
	int data;
public:
	Node();
	Node(int data);
	~Node();
};

Node::Node() {
	this->data = 0;
}
Node::Node(int data) {
	this->data = data;
}
Node::~Node() {}

class Stack {
private:
	int top;
	int maxSize;
	Node* node;
public:
	Stack();
	Stack(int size);
	~Stack();

	bool isEmpty();
	void printAll();
	void Push(int data);
	void Pop();
	void Size();
	void printEmpty();
	void PrintTop();
};

Stack::Stack() {
	this->top = -1;
	this->maxSize = 0;
	this->node = NULL;
}
Stack::Stack(int size) {
	this->top = -1;
	this->maxSize = size;
	this->node = new Node[size];
}

Stack::~Stack() {
	this->top = -1;
	this->maxSize = 0;
	delete[] node;
}

bool Stack::isEmpty() {
	if (this->top == -1)	return true;
	else	return false;
}

void Stack::printAll() {
	if (this->isEmpty()) return;
	else {
		for (int i = 0; i < this->top; i++) {
			cout << this->node[i].data << ' ';
		}
		cout << '\n';
	}
}

void Stack::Push(int data) {
	this->node[++this->top].data = data;
}

void Stack::Pop() {
	if (this->isEmpty()) {
		cout << -1 << '\n';
		return;
	}
	else {
		cout << this->node[top--].data << '\n';
		return;
	}
}

void Stack::Size() {
	if (this->isEmpty()) {
		cout << 0 << '\n';
		return;
	}
	else {
		cout << top + 1 << '\n';
		return;
	}
}

void Stack::printEmpty() {
	cout << this->isEmpty() << '\n';
}

void Stack::PrintTop() {
	if (this->isEmpty()) {
		cout << -1 << '\n';
		return;
	}
	else {
		cout << node[top].data << '\n';
		return;
	}
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n = 0;
	cin >> n;
	Stack stack(10000);

	while (n--) {
		string cmd;
		cin >> cmd;
		if (cmd == "push") {
			int data;
			cin >> data;
			stack.Push(data);
		}
		else if (cmd == "pop") {
			stack.Pop();
		}
		else if (cmd == "size") {
			stack.Size();
		}
		else if (cmd == "empty") {
			stack.printEmpty();
		}
		else if (cmd == "top") {
			stack.PrintTop();
		}

	}


}