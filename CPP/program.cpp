#include <iostream>

int main() {

    int num, ans, i=1;

    std:: cout << "Enter a number: ";
    std:: cin >> num;

    while (i <= 10){
        ans = num * i;
        std:: cout << num << " x " << i << " = " << ans << std::endl;
        i += 1;
    }

    return 0;
}