#include "lists.h"



int check_cycle(listint_t *list)
{
	listint_t *ptr2, *ptr;

	if (list->next == NULL || list->next->next == NULL)
		return (0);
	
	ptr = list->next;
	ptr2 = list->next->next;

	while (ptr2->next != NULL && ptr2->next->next != NULL)
	{
		if (ptr == ptr2)
			return (1);
		ptr = ptr->next;
		ptr2 = ptr2->next->next;
	}
	return (0);
}
