#include "main.h"

/**
  * _memcpy - copy n bytes from memory
  * @dest: destination to copy from memory
  * @src: source memory area
  * @n: total type to be copied
  * Return: copied string
  */
char *_memcpy(char *dest, char *src, unsigned int n)
{
	unsigned int i = 0;

	while (i < n)
	{
		dest[i] = src[i];
		i++;
	}
	return (dest);
}
