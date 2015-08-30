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

	// getter/setter for int _age
	int get_age() const;
	void set_age(int age);

	// getter/setter for std::string _name
	std::string get_name() const;
	void set_name(std::string name);


	// readonly getter for int _weight
	int get_weight() const;

	// readonly getter for std::vector<char> _lines
	std::vector<char> get_lines() const;

	// readonly getter for std::map<int,int> _map
	std::map<int,int> get_map() const;


private:
	std::map<int,int> map;
	std::vector<char> lines;
	int weight;
	std::string name;
	int age;
    int test;
};

int main()
{

    return 0;
}
