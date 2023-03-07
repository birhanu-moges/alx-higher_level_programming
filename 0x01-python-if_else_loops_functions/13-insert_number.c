#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert node in a sorted list
 * @head: head of the linked list
 * @number: value to be added to the list
 *
 * Return: list or null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *current, *pervious;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;

	current = pervious = *head;
	if (*head == NULL)
	{
		*head = newNode;
		return (*head);
	}
	if (number < current->n)
	{
		newNode->next = *head;
		*head = newNode;
		return (*head);
	}
	while (current)
	{
		if (number <= current->n)
		{
			newNode->next = current;
			pervious->next = newNode;
			return (*head);
		}
		pervious = current;
		current = current->next;
	}
	current->next = newNode;
	return (*head);
}
