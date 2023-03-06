#include "lists.h"

/**
 * check_cycle - finds the loop in a linked list
 * @list: head pointer to list
 *
 * Return: 1 on success or 0 on failure
 */

int check_cycle(listint_t *list)
{
	listint_t *sp, *fp;
	unsigned int flag = 0;

	if (list == NULL || list->next == NULL)
		return (0);
	sp = list->next;
	fp = list->next->next;
	while (sp && fp && fp->next)
	{
		if (sp == fp)
		{
			flag = 1;
			break;
		}
		sp = list->next;
		fp = list->next->next;
	}
	return (flag);
}
