#ifndef NODE_HPP
#define NODE_HPP

#include <iostream>
#include <string>
#include <ctime>

using namespace std;

class Node{
private:    
    string locationX;
    string locationY;
    string locationZ;
    time_t myTime;
public:
    Node(string locationX,string locationY ,string locationZ);
};
#endif