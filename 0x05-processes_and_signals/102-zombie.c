#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Infinite loop.
 *
 * Return: Always 0 (Success).
 */
int infinite_while(void)
{
	while (1)
		sleep(1);

	return (0);
}

/**
 * main - A C program that creates 5 zombie processes.
 *
 * Return: 0 if Success OR 2 If failed.
 */
int main(void)
{
	int i;
	pid_t fd;

	i = 0;
	while (i < 5)
	{
		fd = fork();
		if (fd > 0)
		{
			printf("Zombie process created, PID: %d\n", fd);
			i++;
		}
		else
			exit(2);
	}

	infinite_while();

	return (0);
}
