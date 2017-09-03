package com.company;

public class Stack {

    private int[] values;
    private int nextEmpty;

    public Stack(int size, int[] values) {
        this.values = new int[size];
        this.nextEmpty = 0;

        if(values.length > size) {
            System.out.println("Error: Too Many Values Added");
            return;
        }

        for(int i = 0; i < values.length; i++) {
            this.values[i] = values[i];
            nextEmpty++;
        }
    }

    public void printValues() {
        for(int i = 0; i < nextEmpty; i++) {
            System.out.println(i + ": " + values[i]);
        }
    }

    public void addValue(int value) {
        if(nextEmpty < values.length) {
            values[nextEmpty] = value;
            nextEmpty++;
        }
        else System.out.println("Error: Stack Full");
    }

    public void removeValue() {

    }

}
