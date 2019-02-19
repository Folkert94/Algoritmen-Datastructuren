/*
* Folkert Stijnman
* 10475206
* Datastructuren en Algoritmen
* Infix2rpn; writes infix input to Reversh Polish Notation
*/

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#include "stack.h"

bool is_operator(char c);
bool is_precedent(char a, int b);
bool is_parenthesis(char c);
bool invalid_char_check(char * input);
bool parentheses_check(char *input);
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
    if ((a == '^') && ((b != '^') || (b == '^'))) {
        return true;
    }
    if ((a == '/' || a == '*') && (b == '-' || b == '+')) {
        return true;
    }
    if ((a == '-' || a == '+') && b == '(' ) {
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

bool parentheses_check(char *input) {
    int left_par = 0;
    int right_par = 0;
    for (size_t i = 0 ; i < strlen(input); i++) {
        char token = input[i];
        if (token == '(') {
            left_par++;
        }
        if (token == ')') {
            right_par++;
        }
    }
    if (left_par != right_par) {
        printf("Insufficient parenthesis...\n");
        exit(1);
    }
    return 0;
}

bool invalid_char_check(char * input) {
    for (size_t i = 0 ; i < strlen(input); i++) {
        char token = input[i];
        if (token == ' ') {
            continue;
        }
        if (!isdigit(token) && !is_operator(token) && !is_parenthesis(token)) {
        printf("Invalid character(s) found...\n");
        exit(1);
        }
    }
    return 0;
}

void infix2rpn(struct stack *s, char *input) {
    for (size_t i=0; i < strlen(input); i++)
    {
        char token = input[i];

        //skip spaces
        if (token == ' ') {
            continue;
        }

        //output digit directly
        if (isdigit(token)){
            printf("%c", token);
            while (isdigit(input[i + 1])) {
                printf("%c", input[++i]);
            }
        printf(" ");
        }

        if (is_operator(token)) {
            while (!is_precedent(token, stack_peek(s)) && !stack_empty(s) &&
        (stack_peek(s) != '(')) {
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
    invalid_char_check(input);
    parentheses_check(input);
    infix2rpn(s, input);
    stack_cleanup(s);
    return 0;
}
