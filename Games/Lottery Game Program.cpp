// 10/21/2014 - Lottery game in which players have to guess a randomly generated number.

#include <iostream>
#include <string>
#include <iomanip>
#include <cmath>
#include <stdlib.h> // For some reason <stdlib> is invalid or something
#include <ctime>
using namespace std;

int main()
{
	srand(time(NULL));

	string name;
	int lot, guess, tut = 0;
	// Simple Decor and requesting the player's name
	cout << "===============================\n" << "WELCOME TO JAWSH'S LOTTERY GAME\n" << "===============================\n" << endl;
	cout << "Enter your name." << endl;
	cin >> name;
	system("pause");
	// Welcomes the player and gives them instructions
	cout << endl << "Welcome to Jawsh's Lottery game, " << name << endl;
	cout << "--=-=-=--\n" << ":[Rules]:\n" << "--=-=-=--\n" << endl;
	cout << ":// Enter a number 1-20" << endl;
	cout << ":// Any negative number will terminate the program." << endl;
	cout << ":// If you guess the correct lottery number, you win.\n" << endl;
	system("pause");
	cout << endl << ":LETS_BEGIN:\n" << endl;
	system("pause");
	
	while(tut == 0)
	{
		lot = rand() % 20 + 1;
		cout << endl << "Enter a number 1-20" << endl;
		cin >> guess;
		system("pause");
		// This part will end the program if a player enters a number below 0
		if (guess < 1)
		{
			cout << "You have entered a negative number. The program will now terminate." << endl;
			cout << "Thanks for playing!" << endl;
			system("pause");
			return 0;
		}
		// This part will end the program if a player enters a number above 20
		if (guess > 20)
		{
			cout << "You have entered an invalid number." << endl;
			system("pause");
		}

		cout << "You have guessed the number " << guess << endl;
		// This part of the program lets the player know they have either guessed correctly or they have lost
		if(guess == lot)
		{
			cout << "Congratulations, you won! The Lottery number was: " << lot << endl;
		system("pause");
		}
		else
		{
			cout << "Sorry, but you lose. The lottery number was: " << lot << endl;
			system("pause");
		}
	}
	}
