#include <stdio.h>
#include <stdlib.h>

int main() {

    FILE *fd;
    fd = fopen("day1_input.txt", "r");

    char content[10];

    while(fgets(content, 10, fd)) {
        
        printf("%s\n", content);
    }

}
