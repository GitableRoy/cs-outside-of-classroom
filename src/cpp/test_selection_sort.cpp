#include <iostream>
#include "tools.hpp"

int main()
{
    auto vec = tools::rand_int(10, 0, 100);
    std::cout << "Before sorting: " << vec << std::endl;
    tools::selection_sort(vec);
    std::cout << "After sorting: " << vec << std::endl;
    std::cout << "Is it sorted? ";
    std::cout << (tools::is_sorted(vec) ? "Yes" : "No") << std::endl;
}
