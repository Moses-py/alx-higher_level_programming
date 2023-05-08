#include "lists.h"

/**
 * check_cycle - function to check for a loop in a
 * linked list
 * @list: start item of the linked list to be checked
 *
 * Return: 1 if a loop is found, and 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *unoptimized, *optimized;

	if (!list)
	{
		return (0);
	}
	unoptimized = list;
	optimized = list->next;
	while (optimized && unoptimized && optimized->next)
	{
		if (unoptimized == optimized)
		{
			return (1);
		}
		unoptimized = unoptimized->next;
		optimized = optimized->next->next;
	}
	return (0);
}
