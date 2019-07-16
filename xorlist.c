#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    int both; // next xor prev
};

int main(int argc, char *argv[])
{
    struct node *head = (struct node *)malloc(sizeof(struct node));
    head -> data = 1;
     
    struct node *node2 = (struct node *)malloc(sizeof(struct node)); 
    node2-> data = 2;

    struct node *node3 = (struct node *)malloc(sizeof(struct node)); 
    node3-> data = 3;

    head->both = node2;
    node2->both = (int) head ^ (int) node2;
    node3->both = node2;
    
}