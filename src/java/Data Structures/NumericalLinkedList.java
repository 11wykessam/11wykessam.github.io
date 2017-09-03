package com.company;

public class NumericalLinkedList {

    private int fullHeader;
    private int emptyHeader;

    private NumericalLinkedListNode[] nodes;

    // constructor
    public NumericalLinkedList(int size) {

        nodes = new NumericalLinkedListNode[size];
        clearList();

        // a "-1" as the fullHeader tells the program that the
        fullHeader = -1;
        emptyHeader = 0;

    }

    // method to add a given value to linked list
    public void addNode(int value) {
        // we can't have duplicates as the ordering won't work, we can't add anything if linked list is full
        if(doesListContain(value) || isListFull()) return;
        else {
            // we first need to decide on which slot we will fill
            int indexToFill = emptyHeader;
            emptyHeader = Integer.valueOf(nodes[emptyHeader].getPointer());

            nodes[indexToFill].setValue(value);

            // if the list is empty, set full header to indexToFill and the pointer to "X"
            if(isListEmpty()) {
                nodes[indexToFill].setPointer("X");
                fullHeader = indexToFill;
            }

            else {

                // first we need to find the find the node to succeed our value, ie the next largest node
                int nextNodeIndex = -1;

                // three situations:
                // - Value is LOWEST: set it to be the header and point to older header
                // - Value is IN MIDDLE: set preceding header to this node and this header to the succeeding node
                // - Value is HIGHEST: set old tail value to this node and set this pointer to "X"

                // check for smallest value
                if(value < nodes[fullHeader].getValue()) {

                    nodes[indexToFill].setPointer(String.valueOf(fullHeader));
                    fullHeader = indexToFill;

                }
                // check for largest value
                else if(value > getHighestValue()) {
                    nodes[getHighestValueIndex()].setPointer(String.valueOf(indexToFill));
                    nodes[indexToFill].setPointer("X");
                }
                // we know that its somewhere in the middle
                else {

                    int currentIndex = Integer.parseInt(nodes[fullHeader].getPointer());
                    int previousIndex = fullHeader;

                    while (currentIndex < value) {
                        if(nodes[currentIndex].getPointer().equals("X")) break;

                        previousIndex = currentIndex;
                        currentIndex = Integer.parseInt(nodes[currentIndex].getPointer());
                    }

                    nodes[previousIndex].setPointer(String.valueOf(indexToFill));
                    nodes[indexToFill].setPointer(String.valueOf(currentIndex));

                }

            }
        }

    }

    // return the last value in the LinkedList
    public int getHighestValue() {

        return nodes[getHighestValueIndex()].getValue();

    }

    //returns the index of the highest value
    public int getHighestValueIndex() {

        if(!isListEmpty()) {

            int currentIndex = fullHeader;

            while(!nodes[currentIndex].getPointer().equals("X")) {
                currentIndex = Integer.parseInt(nodes[currentIndex].getPointer());
            }

            return currentIndex;

        }
        else return -1;

    }

    // checks if the linked list has no full cells
    public boolean isListEmpty() {
        return fullHeader == -1;
    }

    public boolean isListFull() {
        return nodes[emptyHeader].getPointer().equals("X");
    }

    // removes all values from linked list
    public void clearList() {
        for(int i = 0; i < nodes.length - 1; i++) {
            nodes[i] = new NumericalLinkedListNode(String.valueOf(i + 1));
        }
        nodes[nodes.length - 1] = new NumericalLinkedListNode("X");
    }

    // checks if linked list contains a given value
    public boolean doesListContain(int value) {
        int currentPointer = fullHeader;
        if(currentPointer == -1) return false;
        else {
            while (true) {
                if(value == nodes[currentPointer].getValue()) return true;
                else {
                    if(nodes[currentPointer].getPointer().equals("X")) return false;
                    else currentPointer = Integer.parseInt(nodes[currentPointer].getPointer());
                }
            }
        }
    }

    // prints the contents of linked list to console
    public void printValues() {
        for(int i = 0; i < nodes.length; i++) {
            System.out.print(i + ": " + nodes[i].getValue() + " (" + nodes[i].getPointer() +")");

            if(i == fullHeader) System.out.print(" FULL HEADER");
            if(i == emptyHeader) System.out.print(" EMPTY HEADER");

            System.out.print("\n");
        }
    }

}
