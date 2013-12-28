package main

import (
	"fmt"
)

type Node struct {
	v string
	next *Node
}

type LinkedList struct {
	head *Node
}

func (n *Node) Next() *Node {
	return n.next
}

func (l *LinkedList) Add(a *Node) {
	if l.head == nil {
		l.head = a
		return
	}
	current := l.head;
	for current.next != nil {
		current = current.next
	}
	current.next = a
}

func (l *LinkedList) Print() {
	current := l.head;
	for current.next != nil {
		fmt.Println(current.v, ", ")
		current = current.next
	}
	fmt.Println(current.v, " ")
}

func main() {
	a := &Node{v:"a"}
	b := &Node{v:"b"}
	c := &Node{v:"c"}
	d := &Node{v:"d"}
	l := new(LinkedList)
	
	l.Add(a)
	l.Add(b)
	l.Add(c)
	l.Add(d)
	l.Print()
}
