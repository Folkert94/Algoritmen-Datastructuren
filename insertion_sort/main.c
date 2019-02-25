/*
* Folkert Stijnman
* 10475206
* Datastructuren en Algoritmen
* Insertion Sort; makes use of insertion sort and different flags
*/

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

    while (fgets(buf, BUF_SIZE, stdin)) {

        // Reading and splitting string.
        const char s[2] = " \n";
        char *token;
        token = strtok(buf, s);
        while(token != NULL) {

            int num = atoi(token);

            struct node* n = list_new_node(num);
            struct node* current = list_head(l);

            // Sorting every token.
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
    // Flags and corresponding functions
    int u = cfg.unique_values;
    int d = cfg.descending_order;
    int i = cfg.insert_intermediate;
    int z = cfg.zip_alternating;

    if (u == 1) {
        list_remove_dupl(l);
    }
    if (d == 1) {
        list_desc_order(l);
    }
    if (i == 1) {
        list_inter_values(l);
    }
    if (z == 1) {
        int length = list_length(l);
        int mid = (length / 2);
        struct node* half = list_get_ith(l, mid);
        struct list* l2 = list_cut_after(l, half);
        split_alternate(l, l2);
        free(l2);
    }

    // Print full linked list and clean up.
    struct node* current = list_head(l);
    while (current != NULL) {
        printf("%d\n", list_node_value(current));
        current = list_next(current);
    }
    list_cleanup(l);
    return 0;
}
