class MyHashMap {
    class Entry {
        public int key, value;
        public Entry(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    // reduce array to size 10007 (prime number, which reduces collisions)
    private int NUM_BUCKETS = 10007;
    private LinkedList<Entry>[] map;

    public MyHashMap() {
        this.map = new LinkedList[NUM_BUCKETS];
    }
    
    public void put(int key, int value) {
        LinkedList<Entry> bucket = getOrCreateBucket(key);
        for (Entry entry : bucket) {
            if (entry.key == key) {
                entry.value = value;
                return;
            }
        }
        bucket.add(new Entry(key, value));
    }
    
    public int get(int key) {
        LinkedList<Entry> bucket = getOrCreateBucket(key);
        for (Entry entry : bucket) {
            if (entry.key == key) {
                return entry.value;
            }
        }
        return -1;
    }
    
    public void remove(int key) {
        LinkedList<Entry> bucket = getOrCreateBucket(key);

        Iterator<Entry> iterator = bucket.iterator();
        while (iterator.hasNext()) {
            Entry entry = iterator.next();
            if (entry.key == key) {
                iterator.remove();
            }
        }
    }

    private LinkedList<Entry> getOrCreateBucket(int key) {
        LinkedList<Entry> bucket = map[hash(key)];
        if (bucket == null) {
            bucket = new LinkedList();
            map[hash(key)] = bucket;
        }
        return bucket;
    }

    private int hash(int key) {
        return key % NUM_BUCKETS;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */