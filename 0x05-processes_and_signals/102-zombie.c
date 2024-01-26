#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - A function that creates an infinite loop
 *
 * Return: Always 0;
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - A functtion that creates 5 zombie processes.
 *
 * Return: Always 0
 */

int main(void)
{
	int count;

	for (count = 0; count < 5; count++)
	{
		if (fork() == 0)
		{
			dprintf(1, "Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	}

	infinite_while();

	return (0);
}
