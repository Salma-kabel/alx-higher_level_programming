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
                while (ptr != node)
                {
                        if (node->next == ptr)
                                return (1);
                        ptr = ptr->next;
                }
                ptr = list;
                node = node->next;
	}
	return (0);
}
