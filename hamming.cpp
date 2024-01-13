#include <bits/stdc++.h>
using namespace std;

int main(){
    int a[10], b[10];
    int p1, p2, p3;  //parity values

    cout << "Enter 4 bits data: ";
    cin >> a[3];
    cin >> a[5];
    cin >> a[6];
    cin >> a[7];

    a[1] = a[3] ^ a[5] ^ a[7];
    a[2] = a[3] ^ a[6] ^ a[7];
    a[4] = a[5] ^ a[6] ^ a[7];

    for (int i = 1; i < 8 ; i++){
        cout << a[i] << " ";
    }
    cout << endl;
    cout << "Enter 7 bit code : ";

    for (int i = 1; i < 8 ; i++){
        cin >> b[i];
    }

    p1 = b[1] ^ b[3] ^ b[5] ^ b[7];
    p2 = b[2] ^ b[3] ^ b[6] ^ b[7];
    p3 = b[3] ^ b[5] ^ b[6] ^ b[7];

    int p = (p1 * 1) + (p2 * 2) + (p3 * 4);

    if (p == 0){
        cout << "There is no error" << endl;
    }
    else{
        cout << "There is an error at position " << p << endl;
        if(b[p] == 0){
            b[p] = 1;
        }
        else{
            b[p] = 0;
        }

        cout << "The correct Message is: ";

        for (int i = 1; i < 8 ; i++){
            cout << b[i] << " ";
        }
    }
    return 0;
}