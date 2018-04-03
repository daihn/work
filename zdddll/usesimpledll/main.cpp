//------------------ main.cpp -------------------

#include "simpledll.h"
using namespace zdd;
#include <iostream>
using namespace std;

int main(char argc, char**argv)
{
	//
	SimpleDll *sd = new SimpleDll;
	cout << "---------add-------------" << sd << endl;
	
	int a,b;
	cout << "please input the first num" << endl;
	cin >> a;
	cout << "please input the second num" << endl;
	cin >> b;

	int sum = sd->add(a,b);

	printf("%d + %d = %d\n", a, b, sum);

	cout << "please press Enter exit.\n";
	getchar();
	
	return 0;
} 