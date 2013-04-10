#include <stdio.h>

int stringLength(char* str);

int main(){ //def function():
    printf("hello\n");
    char a = 'a';
    char *str = "abcd";
    printf("func2 = %d", stringLength(str));
    return 0;
}

void func1(){
    int x = 1;
    int y = 2;
    int z = x+y;
}

int stringLength(char* str){
    int count = 0;
    char * x = str;
    while(*x != 0){
        count++;
        x++;
    }
    return count;
}
