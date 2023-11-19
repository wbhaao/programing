Node* insertFirst(Node* head, element data) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->data = data;
    node->next = head;
}