#include "lists.h"



listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *ptr;

	node = *head;
	ptr = malloc(sizeof(listint_t));
	if (ptr == NULL)
		return (NULL);
	ptr->n = number;
	if (node == NULL || node->n >= number)
	{
		ptr->next = node;
		*head = ptr;
		return (ptr);
	}
	while (node->next != NULL && node->next->n < number)
	{
		node = node->next;
	}
	ptr->next = node->next;
	node->next = ptr;
	return (ptr);

}
