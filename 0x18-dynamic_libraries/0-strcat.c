#include "main.h"

/**
  * _strcat - concatenates two strings
  * @dest: destination String
  * @src: source String
  * Return: concatinated String
  */
char *_strcat(char *dest, char *src)
{
	int dest_length = 0;
	int src_length = 0;

	while (dest[dest_length] != '\0')
		dest_length++;

	while (src[src_length])
	{
		dest[dest_length++] = src[src_length++];
	}
	if (src_length > 0)
		dest[dest_length] = '\0';
	return (dest);
}
