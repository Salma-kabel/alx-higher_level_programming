#include "lists.h"



int is_palindrome(listint_t **head)
{
	listint_t *head2 = NULL, *ptr;
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
		head2 = addnode(&head2, ptr->n);
		ptr = ptr->next;
		i++;
	}
	if (length % 2 != 0)
		ptr = ptr->next;
	while ((head2 != NULL && ptr != NULL) && head2->n == ptr->n)
	{
		head2 = head2->next;
		ptr = ptr->next;
	}
	if (head2 == NULL && ptr == NULL)
	{
		free_listint(head2);
		return (1);
	}
	else
	{
		free_listint(head2);
		return (0);
	}
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
