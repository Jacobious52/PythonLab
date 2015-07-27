/*
* @Author: Jacob Gonzalez
* @Date:   2015-07-27 20:30:03
* @Last Modified by:   Jacob Gonzalez
* @Last Modified time: 2015-07-27 22:59:49
*/

#include <iostream>

class modtest
{
public:
    modtest();
    ~modtest();

    void dothis();

property:
    int age;
    std::string name;

readonly:
    int weight;
    std::vector<char> lines;
    std::map<int,int> map;

private:
    int test;
};

int main()
{

    return 0;
}
