
public class DynamicArray {

    int capacity;
    int size = 0;
    int[] array;

    public DynamicArray(int capacity) {
        if (capacity > 0) {
            this.capacity = capacity;
            array = new int[capacity];
        }
    }

    public int get(int i) {
        return array[i];
    }

    public void set(int i, int n) {
        array[i] = n;
    }

    public void pushback(int n) {
        if (capacity == size) {
            resize();
        }
        array[size] = n;
        size++;
    }

    public int popback() {
        int n = array[size - 1];
        array[size - 1] = 0; 
        size--;
        return n;
    }

    private void resize() {
        int[] new_array = new int[capacity * 2];
        for (int i = 0; i < capacity; i++) {
            new_array[i] = array[i];
        }
        capacity *= 2;
        array = new_array;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }

    public int[] getArray() {
        return array;
    }
}
