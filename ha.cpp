#include<iostream>
#include<fstream>
#include<string>
#include<stdlib.h>
#include<conio.h>
using namespace std;
main(){
	string ch;
	cout<<"enter data-word: ";
	cin>>ch;
	ofstream l;
	l.open("wir.txt");
	l << ch;
	l.close();
	system("python hamming.py");
	ifstream my("red.txt");
	getline(my,ch);
	cout<<endl<<"code-word is : "<<ch;
	getch();
}
