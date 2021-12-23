#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	cout << "\t\t\t\tWORDLIST MAKER" << endl << "\t\t\t\t\tBY QUAK69" << endl << endl << endl;
	ofstream fout;
	char f_name[40] = { '\0' };
	char l_name[40] = { '\0' };
	char date_birth[5] = { '\0'};
	char year_birth[5] = { '\0'};
	char sibling_name[50] = { '\0' };
	int flag = 0;
	fout.open("wordlist.txt");
	do {
		cout << "enter your first name" << endl;
		cin.getline(f_name, 39);
		for (int i = 0; f_name[i] != '\0'; i++)
		{
			if (f_name[i] >= 65 && f_name[i] <= 122)
			{
				flag = 0;
			}
			else
			{
				flag = 1;
				cout << "type your fuckin name not your sis number asshole by this i mean no integers" << endl<<endl;
				break;
				
			}
		}
	} while (flag == 1);
	do {
		cout << "enter your last name" << endl;
		cin.getline(l_name, 39);
		for (int i = 0; l_name[i]!='\0'; i++)
		{
			if (l_name[i] >= 65 && l_name[i] <= 122)
			{
				flag = 0;
			}
			else
			{
				flag = 1;
				cout << "type your fuckin name asshole no integers" << endl<<endl;
				break;
				
			}
		}
	} while (flag == 1);
	do {
		cout << "enter your date of birth ( only date )" << endl;

		cin.getline(date_birth, 4);
		for (int i = 0; date_birth[i] != '\0'; i++)
		{


			if (date_birth[i] >= 0 && date_birth[i] <= 47 || date_birth[i] >= 58 && date_birth[i] <= 127)
			{
				cout << "no special characters asshole" << endl << endl;
				flag = 1;
				break;
			}
			else
			{
				flag = 0;
			}
		}
	} while (flag == 1);
	do {
		cout << "enter your year of birth ( only year )" << endl;
		cin.getline(year_birth,5);
		for (int i = 0; year_birth[i] != '\0'; i++)
		{


			if (year_birth[i] >= 0 && year_birth[i] <= 47 || year_birth[i] >= 58 && year_birth[i] <= 127)
			{
				cout << "no spec char" << endl << endl;
				flag = 1;
				break;
			}
			else
			{
				flag = 0;

			}
		}
	} while (flag == 1);
			
	do {
		 cout << "enter your sibling name (only first name )" << endl;
		cin.getline(sibling_name, 49);
		for (int i = 0; sibling_name[i]!='\0' ; i++)
		{
			if (sibling_name[i] >= 65 && sibling_name[i] <= 122)
			{
				flag = 0;
			}
			else
			{
				flag = 1;
				cout << " no integers/specia  l characters" << endl << endl;
				break;

			}
		}
	} while (flag == 1);
	fout << f_name << l_name << endl;
	fout << f_name << l_name << date_birth << endl;
	fout << f_name << l_name << date_birth << year_birth << endl;
	fout << f_name << l_name << year_birth << endl;
	fout << l_name << f_name << endl;
	fout << l_name << f_name << date_birth << endl;
	fout << l_name << f_name << date_birth << year_birth << endl;
	fout << l_name << sibling_name << endl;
	fout << f_name << sibling_name << endl;

	for (int i = 1; i <= 9; i++) // name ascending variation 
	{
		fout << f_name << l_name;
		for (int j = 1; j <= i; j++)
		{
			fout << j;
		}
		fout << endl;
	}
	for (int i = 9; i >= 1; i--) //name descending varitaion
	{
		fout << f_name << l_name;
		for (int j = 9; j >= i; j--)
		{
			fout << j;
		}
		fout << endl;
	}

	for (int i = 1; i <= 9; i++) // reverse name ascending variation 
	{
		fout << l_name << f_name;
		for (int j = 1; j <= i; j++)
		{
			fout << j;
		}
		fout << endl;
	}
	for (int i = 9; i >= 1; i--) //reverse name descending varitaion
	{
		fout << l_name << f_name;
		for (int j = 9; j >= i; j--)
		{
			fout << j;
		}
		fout << endl;
	}

	for (int i = 1; i <= 9; i++) // sibling name ascending variation 
	{
		fout << sibling_name;
		for (int j = 1; j <= i; j++)
		{
			fout << j;
		}
		fout << endl;
	}
	for (int i = 9; i >= 1; i--) //sibling name descending varitaion
	{
		fout << sibling_name;
		for (int j = 9; j >= i; j--)
		{
			fout << j;
		}
		fout << endl;
	}
	for (int i = 1; i <= 9; i++) // sibling full name ascending variation 
	{
		fout << sibling_name << l_name;
		for (int j = 1; j <= i; j++)
		{
			fout << j;
		}
		fout << endl;
	}
	for (int i = 9; i >= 1; i--) //sibling full name descending varitaion
	{
		fout << sibling_name << l_name;
		for (int j = 9; j >= i; j--)
		{
			fout << j;
		}
		fout << endl;
	}
	for (int i = 1; i <= 9; i++) // sibling full name reverse ascending variation 
	{
		fout << l_name << sibling_name;
		for (int j = 1; j <= i; j++)
		{
			fout << j;
		}
		fout << endl;
	}
	for (int i = 9; i >= 1; i--) //sibling full name reverse descending varitaion
	{
		fout << l_name << sibling_name;
		for (int j = 9; j >= i; j--)
		{
			fout << j;
		}
		fout << endl;
	}
	for (int i = 1; i <= 9; i++) // siblings  name ascending variation 
	{
		fout << sibling_name << f_name;
		for (int j = 1; j <= i; j++)
		{
			fout << j;
		}
		fout << endl;
	}
	for (int i = 9; i >= 1; i--) //siblings name descending varitaion
	{
		fout << sibling_name << f_name;
		for (int j = 9; j >= i; j--)
		{
			fout << j;
		}
		fout << endl;
	}
	for (int i = 1; i <= 9; i++) // siblings  name reverse ascending variation 
	{
		fout << f_name << sibling_name;
		for (int j = 1; j <= i; j++)
		{
			fout << j;
		}
		fout << endl;
	}
	for (int i = 9; i >= 1; i--) //sibling  name reverse descending varitaion
	{
		fout << f_name << sibling_name;
		for (int j = 9; j >= i; j--)
		{
			fout << j;
		}
		fout << endl;
	}
	for (int i = 1; i <= 9; i++) // DOB variatiob 
	{
		fout << date_birth << f_name;
		for (int j = 1; j <= i; j++)
		{
			fout << j;
		}
		fout << endl;
	}
	for (int i = 9; i >= 1; i--) //dob variation
	{
		fout << date_birth << f_name;
		for (int j = 9; j >= i; j--)
		{
			fout << j;
		}
		fout << endl;
	}
	for (int i = 1; i <= 9; i++) // DOB variation 
	{
		fout << date_birth << f_name << year_birth;
		for (int j = 1; j <= i; j++)
		{
			fout << j;
		}
		fout << endl;
	}
	for (int i = 9; i >= 1; i--) //dob variation
	{
		fout << date_birth << f_name << year_birth;
		for (int j = 9; j >= i; j--)
		{
			fout << j;
		}
		fout << endl;
	}
	for (int i = 1; i <= 9; i++) // DOB variatiob 
	{
		fout << l_name << f_name << year_birth;
		for (int j = 1; j <= i; j++)
		{
			fout << j;
		}
		fout << endl;
	}
	for (int i = 9; i >= 1; i--) //dob variation
	{
		fout << l_name << f_name << year_birth;
		for (int j = 9; j >= i; j--)
		{
			fout << j;
		}
		fout << endl;
	}

	cout << "THANKS FOR WASTING YOUR PRECIOUS TIME HERE" << endl << endl;

	system("pause");
	return 0;
}
