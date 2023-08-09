#include "lists.h"

/**
 * check_cycle - Checks if singly linked list has a cycle
 * @list: pointer to singly linked list
 * Return: 0 if no cycle, 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr2, *ptr;

	if (list == NULL || list->next == NULL || list->next->next == NULL)
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
