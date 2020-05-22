#include <iostream>
#include <fstream>

using namespace std;

int main()
{


	const int len = 30, strings = 10;
	const char ch = '\n';
	char mass1[len][strings];
	char mass2[len][strings];

	ifstream fs("students1.txt", ios::in | ios::binary);

	if (!fs) return 1;

	for (int r = 0; r < strings; r++)
	{
		fs.getline(mass1[r], len - 1, ch);
	}

	ifstream sc("students2.txt", ios::in | ios::binary);

	if (!sc) return 1;

	for (int r = 0; r < strings; r++)
	{
		sc.getline(mass2[r], len - 1, ch);
	}

	sc.close();
	fs.close();

	ofstream fout("students2.txt", ios_base::out | ios_base::trunc);

	for (int i = 0; i < strings; i++) {
		fout << mass1[i] << endl;
	}
	fout.close();

	ofstream fout1("students1.txt", ios_base::out | ios_base::trunc);

	for (int i = 0; i < strings; i++) {
		fout1 << mass2[i] << endl;
	}
	fout1.close();
	



	return 0;
}