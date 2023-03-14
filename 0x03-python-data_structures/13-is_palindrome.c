#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - check if  a linked list is palindrome
 * @head: head of a list
 *
 * Return: 1 on success 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast_ptr, *slow_ptr, *previous, *tmp;

	fast_ptr = slow_ptr = tmp = *head;
	previous = NULL;
	if (*head == NULL)
		return (1);
	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		tmp->next = previous;
		previous = tmp;
		tmp = slow_ptr;
		slow_ptr = slow_ptr->next;
	}
	if (fast_ptr != NULL)
		slow_ptr = slow_ptr->next;

	while (slow_ptr != NULL && previous != NULL)
	{
		if (slow_ptr->n != previous->n)
			return (0);
		slow_ptr = slow_ptr->next;
		previous = previous->next;
	}
	return (1);
}
