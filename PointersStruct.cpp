#include <stdio.h>
#include <iostream>
using namespace std;

struct Rectangle 
{
 int length;
 int breadth;
};

int main()
{

    Rectangle r = {10,5};
    struct Rectangle *p;
    p=(struct Rectangle *)malloc(sizeof(struct Rectangle));
    
    p->length=15;
    p->breadth=7;
    
    cout << p->length << endl;
    cout <<p->breadth<< endl;
    
    return 0;
}
