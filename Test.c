#include <stdio.h>
#include <conio.h>
#define sum a + b;
int main()
{
    int a,b,c;
    char s1[256],s2[256];
    a = 3;
    b = 5;
    c = a * b;
    a = a - c;
    b = c + a;
    printf ("%d%d%d",a,b,c);
    a = "hello";
    s2 = "world";
    printf ("%s%s",s1,s2);
    c = sum + c;
    return 0;
}