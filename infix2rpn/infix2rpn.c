#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#include "stack.h"

// ... SOME CODE MISSING HERE ...

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("usage: %s \"infix_expr\"\n", argv[0]);
        return 1;
    }

    char *input = argv[1];
    struct stack* s = stack_init();

    for(size_t i=0; i < strlen(input); i++)
    {
        char test = input[i];
        if (test == ' ') {
            continue;
        }
        else if (isdigit(test)){
            printf("%c ", test);
        }
        else {
            stack_push(s, test);
        }
    }
    while (!stack_empty(s)){
        printf("%c ", stack_pop(s));
    }
    printf("\n");
    stack_cleanup(s);

    return 0;
}
