package com.company;

public class NumericalLinkedListNode {

    private int value;
    private String pointer;
    private boolean empty;

    public NumericalLinkedListNode(int value, String pointer) {
        this.value = value;
        this.pointer = pointer;
        this.empty = false;
    }

    public NumericalLinkedListNode(String pointer) {
        this.value = 0;
        this.pointer = pointer;
        this.empty = true;

    }

    public int getValue() {
        return value;
    }
    public void setValue(int value) {
        this.value = value;
    }
    public String getPointer() {
        return pointer;
    }
    public void setPointer(String pointer) {
        this.pointer = pointer;
    }
    public boolean isEmpty() {
        return empty;
    }

    public void clear() {
        this.empty = true;
    }

    public void fill(int value) {
        this.empty = false;
        this.value = value;
    }

}
