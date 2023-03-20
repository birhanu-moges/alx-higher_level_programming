#include "main.h"

/**
  * _strpbrk - return the number of bytes in initital string
  * @s: source string
  * @accept: characters to check
  * Return: return matching character starting point
  */
char *_strpbrk(char *s, char *accept)
{
	int i = 0, j = 0;

	for (i = 0; s[i] != '\0'; i++)
	{
		while (accept[j])
		{
			if (s[i] == accept[j])
			{
				return (&s[i]);
			}
			j++;
		}
		j = 0;
	}
	return ('\0');
}
