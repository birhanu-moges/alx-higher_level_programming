#include "main.h"

/**
  * _strcmp - copies a string
  * @s1: destination String
  * @s2: source String
  * Return: int
  */
int _strcmp(char *s1, char *s2)
{
	int i = 0;

	while (s1[i] && s2[i])
	{
		if (s1[i] == s2[i])
		{
			i++;
			continue;
		}
		return (s1[i] - s2[i]);
	}
	if (s1[i] != '\0')
		return (s1[i]);
	return (-1 * s2[i]);

}
