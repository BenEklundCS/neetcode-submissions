class MyHashSet {
    private boolean[] set;

    public MyHashSet() {
        this.set = new boolean[1000000];
    }
    
    public void add(int key) {
        this.set[key] = true;
    }
    
    public void remove(int key) {
        this.set[key] = false;
    }
    
    public boolean contains(int key) {
        return this.set[key];
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */