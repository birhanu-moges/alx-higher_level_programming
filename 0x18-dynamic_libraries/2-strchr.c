#include "main.h"

/**
  * _strchr - find first occurance of a character
  * @s: source string
  * @c: character to check
  * Return: return pointer to the first occurance
  */
char *_strchr(char *s, char c)
{
	int i = 0;

	for (i = 0; s[i] >= '\0'; i++)
	{
		if (s[i] == c)
			return (s + i);
	}
	return ('\0');
}
