#include "lists.h"



int is_palindrome(listint_t **head)
{
	listint_t *head2 = *head, *ptr, *crt, *prev, *next;
	int length = 0, i = 0;

	ptr = *head;
	if (ptr == NULL || ptr->next == NULL)
		return (1);
	while (ptr != NULL)
	{
		length++;
		ptr = ptr->next;
	}
	ptr = *head;
	while (i < length / 2)
	{
		ptr = ptr->next;
		i++;
	}
	if (length % 2 != 0)
		ptr = ptr->next;
	prev = NULL;
	crt = ptr;
	while (crt != NULL )
	{
		next = crt ->next;
		crt->next = prev;
		prev = crt;
		crt = next;
	}
	ptr = prev;
	while(ptr != NULL && head2->n == ptr->n)
	{
		ptr = ptr->next;
		head2 = head2->next;
	}
	if (ptr == NULL)
		return (1);
	else
		return (0);
}

listint_t *addnode(listint_t **head, int n)
{
	listint_t *new;

    	new = malloc(sizeof(listint_t));
    	if (new == NULL)
        	return (NULL);

    	new->n = n;
    	new->next = *head;

    	return (new);
}
