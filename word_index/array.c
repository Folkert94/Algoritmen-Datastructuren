#include <stdlib.h>

#include "array.h"

struct array {
    int capacity;
    int size;
    int *data;
};

struct array* array_init(unsigned long initial_capacity) {
    struct array* a = malloc(sizeof(struct array));
    a->data = malloc(sizeof(int) * initial_capacity);
    a->size = 0;
    a->capacity = initial_capacity;
    return a;
}

void array_cleanup(struct array* a) {
    free(a->data);
    free(a);
}

int array_get(struct array *a, unsigned long index) {
    return a->data[index];
}

/* Note: Although this operation might require the array to be resized and
 * copied, in order to make room for the added element, it is possible to do
 * this in such a way that the amortized complexity is still O(1).
 * Make sure your code is implemented in such a way to guarantee this. */
int array_append(struct array *a, int elem) {
    if (a->size >= a->capacity) {
        a->capacity *= 2;
        a->data = realloc(a->data, sizeof(int) * a->capacity);
    }
    a->data[a->size] = elem;
    a->size++;
    return 0;
}

unsigned long array_size(struct array *a) {
    return a->size;
}
