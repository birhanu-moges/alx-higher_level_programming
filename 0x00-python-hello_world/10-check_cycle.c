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

	if (list == NULL)
		return (0);
	sp = fp = list;
	while (sp && fp && fp->next)
	{
		sp = sp->next;
		fp = sp->next->next;
		if (sp == fp)
		{
			flag = 1;
			break;
		}
	}
	return (flag);
}
