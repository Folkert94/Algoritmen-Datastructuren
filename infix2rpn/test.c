#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>


bool is_operator(char c);

bool is_operator(char c) {
    if ((c == '+') || (c == '-') || (c == '/') || (c =='*') || (c == '^')
|| (c == '(') || (c == ')')) {
        printf("yes");
        return true;
    }
    else {
        return false;
    }
}

int main() {
    is_operator('(');
}
