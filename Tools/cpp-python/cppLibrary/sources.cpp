#include <iostream>
#include <string>
#include <cstdint>

std::vector<uint64_t> cpp_do_the_thing(std::string to_print)
{
    std::cout << to_print << std::endl ;
    std::vector<uint64_t> result;
    result.push_back(1);
    result.push_back(42);
    return result;
}
