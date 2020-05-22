#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
using namespace std;

struct Cards {
    string suit;
    string rank;
};

int main()
{
    Cards cards[10];
    ifstream fin("cards.txt");
    int sizeStruct = 0;
    char str[100];

    if (!fin) {
        cerr << "Error in opening the file" << endl;
        return 1; // if this is main
    }

   
    Cards temp;
    int size = 0;
    while (fin >> temp.suit >> temp.rank) {
        cards[size]= temp;
        size++;
    }

    /*while (fin.getline(str, 100))
    {
        char* pch;
        pch = strtok(str, " ");
        int j = 1;
        while (pch != NULL)
        {
            switch (j)
            {
            case 1:
                strcpy(cards[sizeStruct].suit, pch);
                j++;
                break;
            case 2:
                strcpy(cards[sizeStruct].rank, pch);
                j++;
                break;
            default:
                break;
            }
            pch = strtok(NULL, " ");
        }

        sizeStruct++;
    }*/

    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            if (cards[i].suit == cards[j].suit && cards[i].rank > cards[j].rank) {
                Cards temp = cards[i];
                cards[i] = cards[j];
                cards[j] = temp;
                
            }
            if (cards[i].suit > cards[j].suit) {
                Cards temp = cards[i];
                cards[i] = cards[j];
                cards[j] = temp;
            }
        }
    }
    

    ofstream fout;
    fout.open("cards_sorted.txt");

    for (int i = 0; i < size; i++) {
        if (cards[i].suit == "spades") {
            for (int j = 0; j < size; j++) {
                cout << cards[j].rank << endl;
            }
        }
    }

    for (int i = 0; i < size; i++) {
        fout << cards[i].suit << " " << cards[i].rank << endl;
    }
    fout.close();
    return 0;
}