#include "main.h"

/**
  * _memset - allocating memory
  * @s: memory pointer
  * @b: character to be stored
  * @n: total type b to be stored in memory
  * Return: character array pointer
  */
char *_memset(char *s, char b, unsigned int n)
{
	unsigned int i = 0;

	while (i < n)
	{
		s[i] = b;
		i++;
	}
	return (s);
}
