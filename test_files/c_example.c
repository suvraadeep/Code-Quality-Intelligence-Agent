#include <stdio.h>
#include <string.h>

// TODO: replace unsafe functions
void copy(char *dst, const char *src) {
    // Potentially unsafe
    strcpy(dst, src);
}

int main() {
    char buf[16];
    // Use of gets() is unsafe
    gets(buf);
    printf("%s", buf);
    return 0;
}


