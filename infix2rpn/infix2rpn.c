#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#include "stack.h"

// ... SOME CODE MISSING HERE ...

bool is_operator(char c);
bool is_precedent(char a, int b);
bool is_parenthesis(char c);
void infix2rpn(struct stack *s, char *input);

bool is_operator(char c) {
    if ((c == '+') || (c == '-') || (c == '/') || (c =='*') || (c == '^')) {
        return true;
    }
    else {
        return false;
    }
}

bool is_precedent(char a, int b) {
    if ((a == '-' || a == '+') && b == '(' ) {
        return true;
    }
    if ((a == '/' || a == '*') && (b == '-' || b == '+')) {
        return true;
    }
        return false;
}

bool is_parenthesis(char c) {
    if ((c == '(') || (c == ')')) {
        return true;
    }
    return false;
}


void infix2rpn(struct stack *s, char *input) {
    for (size_t i=0; i < strlen(input); i++)
    {
        char token = input[i];
        if (token == ' ') {
            continue;
        }
        if (!isdigit(token) && !is_operator(token) && !is_parenthesis(token)) {
            exit(1);
        }
        if (isdigit(token)){
            printf("%c", token);
            while (isdigit(input[i + 1])) {
                printf("%c", input[++i]);
            }
        printf(" ");
        }

        if (is_operator(token)) {
            while (!is_precedent(token, stack_peek(s)) && !stack_empty(s)) {
                printf("%c ", stack_pop(s));
            }
            stack_push(s, token);
        }

        if (token == '(') {
            stack_push(s, token);
        }
        if (token == ')') {
            while (stack_peek(s) != '(') {
                printf("%c ", stack_pop(s));
            }
        stack_pop(s);
        }

    }
    while (!stack_empty(s)){
        printf("%c ", stack_pop(s));
    }
    printf("\n");

}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("usage: %s \"infix_expr\"\n", argv[0]);
        return 1;
    }

    char *input = argv[1];
    struct stack* s = stack_init();
    infix2rpn(s, input);
    stack_cleanup(s);
    return 0;
}
