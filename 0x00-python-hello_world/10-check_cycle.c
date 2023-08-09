#include "lists.h"



int check_cycle(listint_t *list)
{
	listint_t *ptr, *node;
	
	if (list == NULL)
		return (0);
	node = list->next;
	ptr = list;
	while (node != NULL && node->next != NULL)
	{
                if (node->next == ptr)
               		return (1);
                ptr = ptr->next;
                node = node->next;
	}
	return (0);
}
