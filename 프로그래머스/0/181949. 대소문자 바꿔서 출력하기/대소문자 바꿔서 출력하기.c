#include <stdio.h>
#define LEN_INPUT 10

int main(void) {
    char s1[20];
    scanf("%s", s1);
    
    for(int i=0; s1[i]!='\0'; i++)
    {
        if(s1[i]>64&&s1[i]<91)
        {
            s1[i]=s1[i]+32;
        }
        else if(s1[i]>96&&s1[i]<123)
        {
            s1[i]=s1[i]-32;
        }
         
    }
    printf("%s", s1);
   
    
    
    return 0;
}
