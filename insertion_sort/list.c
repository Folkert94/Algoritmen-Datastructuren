/*
* Folkert Stijnman
* 10475206
* Datastructuren en Algoritmen
* Linked List structure with corresponding functions
*/

#include <stdlib.h>
#include <stdio.h>

#include "list.h"

struct list {
    struct node *head;
};

struct node {
    int num;
    struct node *next;
};

struct list* list_init(void) {
    struct list *l = malloc(sizeof(struct list));
    l->head = NULL;
    return l;
}

struct node* list_new_node(int num) {
    struct node *n = malloc(sizeof(struct node));
    n->num = num;
    n->next = NULL;
    return n;
}

struct node* list_head(struct list* l) {
    if (l == NULL) {
        return NULL;
    }
    return l->head;
}

struct node* list_next(struct node* n) {
    if (n == NULL) {
        return NULL;
    }
    return n->next;
}

int list_add_front(struct list* l, struct node* n) {
    if (l == NULL || n == NULL) {
        return 1;
    }
    if (l->head == NULL) {
    l->head = n;
    return 0;
    }
    n->next = l->head;
    l->head = n;
    return 0;
}

struct node* list_tail(struct list* l) {
    if (l->head == NULL) {
        return NULL;
    }
    struct node* tmp = l->head;
    struct node* tmp1;

    while (tmp != NULL) {
        tmp1 = tmp;
        tmp = tmp->next;
    }
    return tmp1;
}

struct node* list_prev(struct list* l, struct node* n) {
    struct node* current = l->head;
    if (current == n) {
        return NULL;
    }
    while (1) {
        if (current->next == n) {
            return current;
        }
        current = current->next;
    }
    return NULL;
}

int list_add_back(struct list* l, struct node* n) {
    if (l == NULL || n == NULL) {
        return 1;
    }
    if (l->head == NULL) {
        l->head = n;
        return 0;
    }
    struct node *current = l->head;
    while (1) {
        if (current->next == NULL) {
            current->next = n;
            break;
        }
        current = current->next;
    }
    return 0;
}

int list_node_value(struct node* n) {
    if (n == NULL) {
        return 0;
    }
    return n->num;
}

int list_unlink_node(struct list* l, struct node* n) {
    if (l == NULL || n == NULL) {
        return 1;
    }
    if (l->head == n) {
        l->head = n->next;
        return 0;
    }

    struct node* temp = l->head;
    struct node* prev;

    while (temp != n) {
        if (temp == NULL) {
            return 1;
        }
        prev = temp;
        temp = temp->next;
    }
    prev->next = n->next;
    return 0;
    }


void list_free_node(struct node* n) {
    free(n);
}

int list_cleanup(struct list* l) {
    if (l == NULL) {
        return 1;
    }
    struct node* tmp;
    while (l->head != NULL) {
        tmp = l->head;
        l->head = tmp->next;
        free(tmp);
    }
    free(l);
    return 0;
}

int list_node_present(struct list* l, struct node* n) {
    if (l == NULL || n == NULL) {
        return 0;
    }
    struct node* temp = l->head;
    while (temp != n) {
        if (temp == NULL) {
            return 0;
        }
        temp = temp->next;
    }
    return 1;
}

int list_insert_after(struct list* l, struct node* n, struct node* m) {
    if (l == NULL || n == NULL || m == NULL) {
        return 1;
    }
    if (list_node_present(l, n) == 1 || list_node_present(l, m) == 0) {
        return 1;
    }
    if (m->next == NULL) {
        list_add_back(l, n);
        return 0;
    }
    n->next = m->next;
    m->next = n;
    return 0;
}

int list_insert_before(struct list* l, struct node* n, struct node* m) {
    if (l == NULL || n == NULL || m == NULL) {
        return 1;
    }
    if (l->head == m) {
        list_add_front(l, n);
        return 0;
    }
    struct node* temp = l->head;
    struct node* prev;
    while (temp != m) {
    if (temp == NULL || temp == n) {
        return 1;
    }
        prev = temp;
        temp = temp->next;
    }
    prev->next = n;
    n->next = m;
    return 0;
}

int list_length(struct list* l) {
    if (l == NULL) {
        return 0;
    }
    int length = 0;
    struct node* temp = l->head;
    while (temp != NULL) {
        temp = temp->next;
        length++;
    }
    return length;
}

struct node* list_get_ith(struct list* l, int i) {
    int j = 0;
    struct node* temp = l->head;
    while (j < i) {
        if (temp == NULL) {
            return NULL;
        }
        temp = temp->next;
        j++;
    }
    return temp;
}

struct list* list_cut_after(struct list* l, struct node* n) {
    if (l == NULL || n == NULL) {
        return NULL;
    }
    if (list_node_present(l, n) == 0) {
        return NULL;
    }
    struct list* l_2 = list_init();
    l_2->head = n->next;
    n->next = NULL;

    return l_2;
}

void list_remove_dupl(struct list* l) {
    if (l == NULL) {
        return;
    }
    struct node* temp = l->head;
    struct node* dummy;

    while (temp->next != NULL) {
        if (list_node_value(temp) == list_node_value(temp->next)) {
            dummy = temp->next->next;
            free(temp->next);
            temp->next = dummy;
        }
        else {
            temp = temp->next;
        }
    }
}

void list_desc_order(struct list* l) {
    if (l == NULL) {
        return;
    }
    struct node *prev, *temp;

    prev = l->head;
    temp = l->head->next;
    l->head = l->head->next;
    prev->next = NULL;

    while (l->head != NULL) {
        l->head = l->head->next;
        temp->next = prev;
        prev = temp;
        temp = l->head;
    }
    l->head = prev;
}

void list_inter_values(struct list *l) {
    if (l == NULL) {
        return;
    }
    struct node *temp = l->head;

    while (temp->next != NULL) {
        int val = list_node_value(temp) - list_node_value(temp->next);
        int num = list_node_value(temp) - (val / 2);
        struct node* n = list_new_node(num);
        list_insert_after(l, n, temp);
        temp = temp->next->next;
    }
}

void split_alternate(struct list *l, struct list *l2) {
    if (l == NULL || l2 == NULL) {
        return;
    }
    struct node* temp = l2->head;
    struct node* temp2 = l->head;
    struct node* dummy;
    while (temp != NULL) {
        dummy = temp;
        temp = temp->next;
        list_insert_after(l, dummy, temp2);
        temp2 = temp2->next->next;
    }
}
