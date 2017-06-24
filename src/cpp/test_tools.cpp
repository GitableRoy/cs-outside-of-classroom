#include "tools.hpp"
#include <iostream>

int main()
{
    auto vec = tools::rand_int(10);
    std::cout << vec << std::endl;
    std::cout << "Is the array sorted?" <<
        (tools::is_sorted(vec) ? "Yes" : "No") << std::endl;
}
