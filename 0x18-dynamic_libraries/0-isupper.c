#include "main.h"
/**
 * _isupper - checkes uppercase
 * Description: checkes character case
 * @c: input character
 * Return: (1) is uppercase
 */

int _isupper(int c)
{
	if (c >= 'A' && c <= 'Z')
		return (1);
	return (0);
}
