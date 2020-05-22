#include <iostream>
#include<cstring>
using namespace std;

struct Rectangle
{
    //поля
    int length;
    int width;
    int per;
    //методи
    int perimeter(int length, int width)
    {
        per = length * width;
        return per;
    }
    //конструктори
    Rectangle(int lenght, int widht)
    {
        (*this).length = lenght;
        (*this).width = width;
    }
};


int main()
{
    Rectangle rect=Rectangle(2,3);
    cout << rect.perimeter(2,3);
}
