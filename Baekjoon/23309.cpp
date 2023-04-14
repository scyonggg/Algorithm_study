#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>

using namespace std;


// Node class //
class Node {
	friend class DList;
private:
public:
	int index;
	Node* next;
	Node* prev;
	Node();
	Node(int index);
	~Node();
	Node* init(int index);
	void del();
};

Node::Node() {
	this->index = 0;
	next = NULL;
	prev = NULL;
}

Node::Node(int index) {
	this->index = index;
	this->next = NULL;
	this->prev = NULL;
}

Node::~Node() {
	this->index = 0;
	this->next = NULL;
	this->prev = NULL;
}

Node* Node::init(int index) {
	this->index = index;
	this->next = NULL;
	this->prev = NULL;
	return this;
}

void Node::del() {
	this->index = 0;
	this->next = NULL;
	this->prev = NULL;
}

Node nodes[2000010];

// DList class //
class DList {
private:
public:
	Node* head;
	int size;
	DList();
	~DList();
	bool isEmpty();
	void insertNode(Node* newNode, Node* u, Node* v);
	void insertEnd(int index);
	void insertAfter(int i, int j);
	void insertBefore(int i, int j);

	void deleteNode(Node* delNode);
	void deleteAfter(int i);
	void deleteBefore(int i);
	void deleteAll();
	void printNode();
};

DList::DList() {
	this->head = NULL;
	this->size = 0;
}

DList::~DList() {}

bool DList::isEmpty() {
	if (this->head == NULL)	return true;
	else return false;
}

void DList::insertNode(Node* newNode, Node* u, Node* v) {
	// u v -> u newNode v
	newNode->next = v;
	newNode->prev = u;
	u->next = newNode;
	v->prev = newNode;
	this->size++;
}

void DList::insertEnd(int index) {
	Node* newNode = nodes[index].init(index);

	if (this->isEmpty()) {
		head = newNode;
		head->next = head;
		head->prev = head;
		this->size++;
		return;
	}
	else {
		// head head_prev -> head newNode head_prev
		insertNode(newNode, head->prev, head);
		return;
	}
}

void DList::insertAfter(int i, int j) {
	Node* newNode = nodes[j].init(j);
	if (this->isEmpty()) {
		head = newNode;
		head->next = head;
		head->prev = head;
		this->size++;
		return;
	}
	else {
		Node* cursor = &nodes[i];
		cout << cursor->next->index << '\n';
		insertNode(newNode, cursor, cursor->next);
		return;
	}
}

void DList::insertBefore(int i, int j) {
	Node* newNode = nodes[j].init(j);
	if (this->isEmpty()) {
		head = newNode;
		head->next = head;
		head->prev = head;
		this->size++;
		return;
	}
	else
	{
		Node* cursor = &nodes[i];
		cout << cursor->prev->index << '\n';
		insertNode(newNode, cursor->prev, cursor);
		return;
	}
}

void DList::deleteNode(Node* delNode) {
	// u delNode v -> u v
	if (delNode == this->head) {
		head = delNode->next;
	}
	delNode->next->prev = delNode->prev;
	delNode->prev->next = delNode->next;
	delNode->del();
	delNode = NULL;
	this->size--;
}

void DList::deleteAll() {
	if (!(this->isEmpty())) {
		Node* cursor = this->head;
		Node* temp;
		do {
			temp = cursor->next;
			cursor->del();
			cursor = temp;
		} while (temp != NULL);
	}
}

void DList::deleteAfter(int i) {
	if (!(this->isEmpty())) {
		Node* delNode = &nodes[i];
		cout << delNode->next->index << '\n';
		this->deleteNode(delNode->next);
		return;
	}
}

void DList::deleteBefore(int i) {
	if (!(this->isEmpty())) {
		Node* delNode = &nodes[i];
		cout << delNode->prev->index << '\n';
		this->deleteNode(delNode->prev);
		return;
	}
}

void DList::printNode() {
	if (!(this->isEmpty())) {
		Node* cursor = this->head;
		cout << "head : " << cursor->index << "\t";
		do {
			cout << cursor->index << ' ';
			cursor = cursor->next;
		} while (cursor != this->head);
		cout << '\n';
	}
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n, m;
	cin >> n >> m;

	DList station;

	for (int i = 0; i < n; i++) {
		int idx;
		cin >> idx;
		station.insertEnd(idx);
	}

	//char cmd[2000010];
	char cmd[3];
	//string command;
	for (int i = 0; i < m; i++) {

		cin >> cmd;
		//scanf("%s", cmd);
		//command = cmd;
		if (cmd[0] == 'B' && cmd[1] == 'N') {
			int i, j;
			cin >> i >> j;
			station.insertAfter(i, j);
		}
		else if (cmd[0] == 'B' && cmd[1] == 'P') {
			int i, j;
			cin >> i >> j;
			station.insertBefore(i, j);
		}
		else if (cmd[0] == 'C' && cmd[1] == 'N') {
			int i;
			cin >> i;
			station.deleteAfter(i);
		}
		else if (cmd[0] == 'C' && cmd[1] == 'P') {
			int i;
			cin >> i;
			station.deleteBefore(i);
		}
		//else if (command == "PP") {
		//station.printNode();
		//}
	}
	//station.deleteAll();
	return 0;
}