#include "main.h"
/**
 * _isalpha- entry point
 * @c: The letter to be checked
 * Discription: check character is a letter
 * Return: (0) success
 */

int _isalpha(int c)
{
	if ((c >= 97 && c <= 122) || (c >= 65 && c <= 90))
		return (1);
	else
		return (0);
}
