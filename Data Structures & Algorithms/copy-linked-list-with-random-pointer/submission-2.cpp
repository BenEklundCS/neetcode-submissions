/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        std::unordered_map<Node*, Node*> umap;
        // in one pass, create a deep copy of the list linked to a hashmap of the OG list
        // this will allow us to create all nodes before assigning the random pointers in a second pass
        Node* curr = head;
        while (curr) {
            umap[curr] = new Node(curr->val); // create deep copy node linked in umap
            curr = curr->next;
        }
        // now link the pointers
        curr = head;
        while (curr) {
            Node* copy = umap[curr]; // get the copy from the map
            copy->next = umap[curr->next]; // link next pointer
            copy->random = umap[curr->random]; // link random pointer
            curr = curr->next;
        }
        return umap[head];
    }
};
