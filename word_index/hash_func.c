
/* Do not edit this function, as it used in testing too
 * Add you own hash functions with different headers instead. */
unsigned long hash_too_simple(unsigned char *str) {
    return (unsigned long) *str;
}
// unsigned long hash_folly(struct table* t, unsigned char *str) {
//     return str % t->capacity;
// }
