#include <stdlib.h>
#include <stdio.h>
#include "stack.h"

struct stack {
    int array[STACK_SIZE];
    int size;
    int push_ops;
    int pop_ops;
    int max_size;
};

struct stack *stack_init() {
    struct stack* s = malloc(sizeof(struct stack));
    s->size = 0;
    s->push_ops = 0;
    s->pop_ops = 0;
    s->max_size = 0;
    return s;
}

void stack_cleanup(struct stack* s) {

    fprintf(stderr, "stats %d %d %d\n", s->push_ops, s->pop_ops,
              s->max_size);
    free(s);
}

int stack_push(struct stack *s, int c) {
    if (s == NULL) {
        return 1;
    }
    if (s->size >= STACK_SIZE) {
        return 1;
    }

    s->array[s->size] = c;
    s->size++;
    s->push_ops++;
    return 0;
}

int stack_pop(struct stack *s) {
    if (s == NULL) {
        return -1;
    }
    if (s->size == 0){
        return -1;
    }

    s->size--;
    s->pop_ops++;

    return s->array[s->size];
}

int stack_peek(struct stack *s) {
    if (s == NULL) {
        return -1;
    }
    if (s->size == 0) {
        return -1;
    }

    return s->array[s->size -1];
}

int stack_empty(struct stack *s) {
    if (s == NULL) {
        return -1;
    }
    if (s->size == 0){
        return 1;
    }
    if (s->size > 0){
        return 0;
    }
    return -1;
}
