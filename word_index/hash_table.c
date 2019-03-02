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
    long unsigned int i = 0;
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
    struct array* temp = table_lookup(t, key);
    if (temp != NULL) {
        array_append(temp, value);
        return 0;
    }

    struct node* n = node_init(key, value);
    if (t->array[index] == NULL) {
        t->array[index] = n;
        return 0;
        }

    if (t->array[index] != NULL) {
        struct node* tmp = t->array[index];
        while (1) {
            if (tmp->next == NULL) {
                tmp->next = n;
                break;
            }
            tmp = tmp->next;
        }
        return 0;
    }

    return 1;
}

struct array *table_lookup(struct table *t, char *key) {
    if (t == NULL || key == NULL) {
        return NULL;
    }
    unsigned long index = t->hash_func(key) % t->capacity;
    struct node* temp = t->array[index];

    while (temp != NULL && (compare_string(temp->key, key) != 0)) {
        temp = temp->next;
    }

    if (temp == NULL) {
        return NULL;
    }

    if (compare_string(temp->key, key) == 0) {
        return temp->value;
    }

    return NULL;
}

int table_delete(struct table *t, char *key) {
    if (t == NULL || key == NULL) {
        return 1;
    }
    struct array* tmp = table_lookup(t, key);
    if (tmp == NULL) {
        return 1;
    }

    unsigned long index = t->hash_func(key) % t->capacity;

    struct node* temp = t->array[index];
    struct node* dummy;

    if (compare_string(temp->key, key) == 0) {
        dummy = temp;
        t->array[index] = temp->next;
        array_cleanup(dummy->value);
        free(dummy);
        return 0;
    }

    struct node* prev;

    while (temp != NULL && (compare_string(temp->key, key) != 0)) {
        prev = temp;
        temp = temp->next;
    }

    prev->next = temp->next;
    array_cleanup(temp->value);
    free(temp);
    return 0;
}

void table_cleanup(struct table *t) {
    unsigned long i = 0;
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

int compare_string(char* str1, char* str2) {
    int rc = strcmp(str1, str2);
    if (rc == 0) {
        return 0;
    }
    else {
        return 1;
    }
}
