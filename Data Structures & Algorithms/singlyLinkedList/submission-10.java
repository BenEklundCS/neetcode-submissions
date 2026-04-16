

class ListNode {
    int val;
    ListNode next;

    ListNode(int val) {
        this.val = val;
    }

    ListNode() {

    }
}

public class LinkedList {
    ListNode head;

    LinkedList() {

    }

        public int get(int index) {
        if (head == null) {
            return -1;
        }
        ListNode ptr = head;
        for (int i = 0; i < index; i++) {
            ptr = ptr.next;
            if (ptr == null) {
                return -1;
            }
        }
        return ptr.val;
    }

    public void insertHead(int val) {
        ListNode node = new ListNode(val);
        if (head != null) {
            node.next = head;
        }
        head = node;
    }

    public void insertTail(int val) {
        ListNode node = new ListNode(val);
        if (head == null) {
            head = node;
        }
        else {
            ListNode ptr = head;
            while (ptr.next != null) {
                ptr = ptr.next;
            }
            ptr.next = node;
        }
    }

    public boolean remove(int index) {
        if (head == null) {
            return false; // List is empty
        }

        if (index == 0) {
            head = head.next;
            return true; // Removed head
        }

        ListNode ptr = head;
        for (int i = 0; i < index - 1; i++) {
            if (ptr.next == null) {
                return false; // Reached end of list before reaching index
            }
            ptr = ptr.next;
        }

        if (ptr.next == null) {
            return false; // No node at index to remove
        }

        ptr.next = ptr.next.next; // Remove node at index
        return true; // Removal was successful
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> list = new ArrayList<>();
        ListNode ptr = head;
        while (ptr != null) {
            list.add(ptr.val);
            ptr = ptr.next;
        }
        return list;
    }

    public void printList() {
        ListNode current = head;
        while (current != null) {
            System.out.print((current.next != null) ? current.val + "-->" : current.val);
            current = current.next;
        }
    }



}
