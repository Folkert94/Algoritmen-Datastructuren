#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

bool is_precedent(char a, char b);

bool is_precedent(char a, char b) {
    // if ((a == '-' || a == '+') && b == '(' ) {
    //     return true;
    // }
    if ((a == '/' || a == '*') && (b == '-' || b == '+')) {
        printf("true\n");
        return true;
    }
    // else if (a == '^' && (b != '-' && b != '^')) {
    //     return true;
    // }
    else if (a == '-' && b != '-') {
        printf("true\n");
        return true;
    }
        printf("false\n");
        return false;

}

int main() {
    is_precedent('*', '+');
}
