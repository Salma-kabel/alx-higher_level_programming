#include "lists.h"



int check_cycle(listint_t *list)
{
	listint_t *ptr, *node;

	node = list->next;
	ptr = list;
	while (node != NULL)
	{
		if (node->next == ptr)
			return (1);
		node = node->next;
	}
	return (0);
}
