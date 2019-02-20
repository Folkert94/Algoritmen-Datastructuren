#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <getopt.h>
#include <math.h>
#include <ctype.h>

#include "list.h"
#define BUF_SIZE 1024

static char buf[BUF_SIZE];

struct config {
    // You can ignore these options until you implement the
    // extra command-line arguments.

    // Set to 1 if -u is specified, 0 otherwise.
    int unique_values;

    // Set to 1 if -d is specified, 0 otherwise.
    int descending_order;

    // Set to 1 if -i is specified, 0 otherwise.
    int insert_intermediate;

    // Set to 1 if -z is specified, 0 otherwise.
    int zip_alternating;
};

int parse_options(struct config *cfg, int argc, char *argv[]) {
    memset(cfg, 0, sizeof(struct config));
    int c;
    while ((c = getopt (argc, argv, "udiz")) != -1) {
        switch (c) {
            case 'u': cfg->unique_values = 1; break;
            case 'd': cfg->descending_order = 1; break;
            case 'i': cfg->insert_intermediate = 1; break;
            case 'z': cfg->zip_alternating = 1; break;
            default:
                      fprintf(stderr, "invalid option: -%c\n", optopt);
                      return 1;
        }
    }
    return 0;
}

int main(int argc, char *argv[]) {
    struct config cfg;
    if (parse_options(&cfg, argc, argv) != 0) {
        return 1;
    }

    struct list* l = list_init();

    // struct node* n = list_new_node(5);
    // struct node* m = list_new_node(8);
    // struct node* k = list_new_node(7);
    // struct node* p = list_new_node(10);
    //
    // list_add_back(l, n);
    // list_add_back(l, m);
    // list_add_back(l, k);
    // list_insert_after(l, p, k);

    while (fgets(buf, BUF_SIZE, stdin)) {

        const char s[2] = " \n";
        char *token;
        token = strtok(buf, s);
        while(token != NULL) {

            int num = atoi(token);

            struct node* n = list_new_node(num);
            struct node* current = list_head(l);

            while (1) {
                if (current == NULL) {
                    list_add_back(l, n);
                    break;
                }
                if (list_node_value(n) < list_node_value(current)) {
                    list_insert_before(l, n, current);
                    break;
                }
                current = list_next(current);
            }
            token = strtok(NULL, s);
        }
    }
    struct node* current = list_head(l);
    while (current != NULL) {
        printf("%d\n", list_node_value(current));
        current = list_next(current);
    }

    list_cleanup(l);

    return 0;
}
