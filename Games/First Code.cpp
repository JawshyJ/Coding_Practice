// 9/4/2014 - To report the name and grade for quiz 1 and average two numbers
#include <iostream>
using namespace std;

int main()
{
	cout << "My name is John.\n";
	cout << "My grade is A.\n";

	float value1 = 10; // the first data
	float value2 = 105; // the second data
	float average;

	average = (value1 + value2) / 2.0;

	cout << "The average of " << value1 << " and " << value2 << " is " << average << endl;
	cout << "Have a nice day, " << "John" << endl;

	system("pause");
	return 0;

}
