#include "lists.h"

/**
 * insert_node - Function to inserts a number in a
 * sorted singly-linked list.
 * @head: A pointer the starting element of the linked list.
 * @number: The number to be inserted.
 * Return: Return null if fails or pointer to node otherwise.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *node_i;

	node_i = malloc(sizeof(listint_t));
	if (node_i == NULL)
		return (NULL);
	node_i->n = number;

	if (node == NULL || node->n >= number)
	{
		node_i->next = node;
		*head = node_i;
		return (node_i);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	node_i->next = node->next;
	node->next = node_i;

	return (node_i);
}

