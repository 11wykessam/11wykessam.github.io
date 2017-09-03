package com.company;

public class CircularQueue {

    private int[] values;
    private int headerValue;
    private int tailValue;

    public CircularQueue(int size, int[] inputValues) {

        if(inputValues.length <= size) {
            headerValue = 0;
            tailValue = values.length - 1;

            for(int i = 0; i < values.length; i++) {
                values[i] = inputValues[i];
            }
        }
        else {
            values = new int[size];
            headerValue = -1;
            tailValue = -1;
        }

    }

    public CircularQueue(int size) {
        values = new int[size];
        headerValue = -1;
        tailValue = -1;
    }

    public void add(int value) {
        if(!isFull()) {
            if(isEmpty()) {
                headerValue = 0;
                tailValue = 0;
            }
            else if(tailValue == values.length - 1) tailValue = 0;
            else tailValue++;

            values[tailValue] = value;

        }
        else System.out.println("Error: Queue Full");
    }
    public void remove() {
        if(!isEmpty()) {
            if(headerValue == values.length - 1) {
                if(headerValue == tailValue) {
                    headerValue = -1;
                    tailValue = -1;
                }
                else headerValue = 0;
            }
            else headerValue++;
        }
        else System.out.println("Error: Queue Empty");

    }

    public void printValues() {
        int startPrint;
        int endPrint;
        if(headerValue < tailValue) {
            startPrint = headerValue;
            endPrint = tailValue;
        }
        else {
            startPrint = tailValue;
            endPrint = headerValue;
        }

        for(int i = 0; i < values.length; i++) {
            if(i >= startPrint && i <= endPrint) System.out.print(values[i] + " ");
            else System.out.print("* ");
        }
        System.out.println("  H: " + headerValue + " T: " + tailValue);

    }

    public boolean isEmpty() {
        return headerValue == -1 || tailValue == -1;
    }
    public boolean isFull() {
        if(tailValue != headerValue -1) {
            if(!(tailValue == values.length - 1 && headerValue == 0)) {
                return false;
            }
            else return true;
        }
        else return true;
    }

}
