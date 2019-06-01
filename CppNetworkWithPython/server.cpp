#include <iostream>
#include <string>

int main() {
    for (int i = 0; true; i++) {
        std::string s;
        getline(std::cin, s);
        std::cout << "What does \"" + s + "\" mean?" << std::endl;
        std::cout.flush();
    }
    return 0;
}
