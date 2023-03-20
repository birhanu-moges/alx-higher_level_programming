#include "main.h"

/**
  * _strncpy - copies a string
  * @dest: destination String
  * @src: source String
  * @n: total characteres to copy
  * Return: String
  */
char *_strncpy(char *dest, char *src, int n)
{
	int i;

	for (i = 0; i < n && src[i] != '\0'; i++)
		dest[i] =  src[i];
	for ( ; i < n; i++)
		dest[i] = '\0';
	return (dest);
}
