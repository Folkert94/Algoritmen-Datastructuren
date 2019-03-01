#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "hash_table.h"
#include "array.h"

struct table {
    // The (simple) array used to index the table
    struct node **array;
    // The function used for computing the hash values in this table
    unsigned long (*hash_func)(unsigned char *);

    // Maximum load factor after which the table array should be resized
    double max_load;
    // Capacity of the array used to index the table
    unsigned long capacity;
    // Current number of elements stored in the table
    unsigned long load;
};

/* Note: This struct should be a *strong* hint to a specific type of hash table
 * You may implement other options, if you can build them in such a way they
 * pass all tests. However, the other options are generally harder to code. */
struct node {
    // The string of characters that is the key for this node
    char *key;
    // A resizing array, containing the all the integer values for this key
    struct array *value;

    // Next pointer
    struct node *next;
};

struct node* node_init(char *key, int value) {
    struct node* n = malloc(sizeof(struct node));
    n->key = key;
    n->value = array_init(4);
    array_append(n->value, value);
    n->next = NULL;
    return n;
}

// TODO
// node resize;

struct table *table_init(unsigned long capacity, double max_load,
                            unsigned long (*hash_func)(unsigned char *)) {
    struct table* t = malloc(sizeof(struct table));
    t->array = malloc(sizeof(struct node) * capacity);
    int i = 0;
    while (i < capacity) {
        t->array[i] = NULL;
        i++;
    }
    t->hash_func = hash_func;
    t->max_load = max_load;
    t->capacity = capacity;
    t->load = 0;
    return t;
}

int table_insert(struct table *t, char *key, int value) {
    int index = t->hash_func(key) % t->capacity;

    // struct node* tmp = table_lookup(t, key);

    struct node* n = node_init(key, value);

    //als de plek nog vrij is
    if (t->array[index] == NULL) {
        t->array[index] = n;
        return 0;
        }
    //als de plek niet vrij is, stop m achteraan
    if (t->array[index] != NULL) {
        struct node* temp = t->array[index];
        while (1) {
            if (temp->next == NULL) {
                temp->next = n;
                break;
            }
            temp = temp->next;
        }
        return 0;
    }
}


struct array *table_lookup(struct table *t, char *key) {
    int index = t->hash_func(key) % t->capacity;
    struct node* temp = t->array[index];
    if (temp->next == NULL) {
        return temp->value;
    }
    while (temp != NULL) {
        if (temp->key == key) {
            return temp->value;
        }
        temp = temp->next;
    }
    return NULL;
}

int table_delete(struct table *t, char *key) {
    // ... SOME CODE MISSING HERE ...
}

void table_cleanup(struct table *t) {
    int i = 0;
    while (i < t->capacity) {
        if (t->array[i] != NULL) {

            // APARTE FUNCTIE?????
            struct node* tmp = t->array[i]->next;
            struct node* tmp2;

            while (tmp != NULL) {
                tmp2 = tmp;
                tmp = tmp->next;
                array_cleanup(tmp2->value);
                free(tmp2);
            }

            array_cleanup(t->array[i]->value);
            free(t->array[i]);
        }
        i++;
    }
    free(t->array);
    free(t);
}
