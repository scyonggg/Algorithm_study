#include <iostream>

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
Node::Node() { data = 0; }
Node::Node(int data) { this->data = data; }
Node::~Node() {}

class Stack {
private:
	int top;
	int size;
	Node* node;
public:
	Stack();
	Stack(int size);
	~Stack();

	bool isEmpty();
	void push(int data);
	void pop();
	void printAcc();
};

Stack::Stack() {
	this->top = -1;
	this->size = 0;
	node = NULL;
}
Stack::Stack(int size) {
	this->top = -1;
	this->size = size;
	this->node = new Node[size];
}
Stack::~Stack() {
	this->top = -1;
	this->size = 0;
	delete[] node;
}

bool Stack::isEmpty() {
	if (this->top == -1) return true;
	else return false;
}

void Stack::push(int data) {
	this->node[++top] = data;
}

void Stack::pop() {
	this->top--;
}

void Stack::printAcc() {
	if (this->isEmpty()) {
		cout << 0 << '\n';
		return;
	}
	else {
		int acc = 0;
		for (int i = 0; i <= top; i++) {
			acc += this->node[i].data;
		}
		cout << acc << '\n';
	}
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int k = 0;
	cin >> k;

	Stack stack(100000);

	while (k--) {
		int data;
		cin >> data;
		if (data == 0) {
			stack.pop();
		}
		else {
			stack.push(data);
		}
	}
	stack.printAcc();
}