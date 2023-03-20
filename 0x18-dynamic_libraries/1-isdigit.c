#include "main.h"
/**
 * _isdigit - checkes digit vialue
 * Description: checkes digit values
 * @c: input character
 * Return: (1) if digit
 */

int _isdigit(int c)
{
	if (c >= 48 && c <= 57)
		return (1);

	return (0);
}
