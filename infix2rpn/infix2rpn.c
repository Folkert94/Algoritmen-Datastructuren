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

bool is_operator(char c) {
    if ((c == '+') || (c == '-') || (c == '/') || (c =='*') || (c == '^')
|| (c == '(') || (c == ')')) {
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

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("usage: %s \"infix_expr\"\n", argv[0]);
        return 1;
    }

    char *input = argv[1];
    struct stack* s = stack_init();

    size_t i = 0;
    while (i < strlen(input))
    {
        char token = input[i];
        if (token == ' ') {
            continue;
        }
        if (!isdigit(token) && !is_operator(token)) {
            stack_cleanup(s);
            return 1;
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
        i++;
    }
    // at the end empty the stack whatever's left
    while (!stack_empty(s)){
        printf("%c ", stack_pop(s));
    }
    printf("\n");
    stack_cleanup(s);
    return 0;
}
