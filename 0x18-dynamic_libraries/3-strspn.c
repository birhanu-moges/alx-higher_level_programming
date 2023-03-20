#include "main.h"

/**
  * _strspn - return the number of bytes in initital string
  * @s: source string
  * @accept: characters to check
  * Return: return total bytes in accept
  */
unsigned int _strspn(char *s, char *accept)
{
	int i = 0, j = 0;
	unsigned int bytes = 0;

	for (i = 0; s[i] != '\0'; i++)
	{
		while (accept[j])
		{
			if (s[i] == accept[j])
			{
				bytes++;
				break;
			}
			else if (accept[j + 1] == '\0')
				return (bytes);
			j++;
		}
		j = 0;
	}
	return (bytes);
}
