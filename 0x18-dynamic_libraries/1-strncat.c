#include "main.h"

/**
  * _strncat - concatenates two strings
  * @dest: destination String
  * @src: source String
  * @n: total characters to concatinate
  * Return: concatinated String
  */
char *_strncat(char *dest, char *src, int n)
{
	int dest_length = 0;
	int src_length = 0;

	while (dest[dest_length] != '\0')
		dest_length++;

	while (src_length < n && src[src_length])
	{
		dest[dest_length++] = src[src_length++];
	}
	return (dest);
}
