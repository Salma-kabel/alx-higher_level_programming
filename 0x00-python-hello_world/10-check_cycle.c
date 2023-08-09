#include "lists.h"



int check_cycle(listint_t *list)
{
	listint_t *tmp, *ptr;

	ptr = list;
	while (ptr != NULL && ptr->next != NULL)
	{
		if (ptr->next == tmp)
			return (1);
		ptr = list->next;
		list->next = tmp;
		list = ptr;
	}
	return (0);
}
