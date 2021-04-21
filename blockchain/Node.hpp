#ifndef NODE_HPP
#define NODE_HPP

#include <iostream>
#include <string>
#include <ctime>
#include <sstream>
#include "sha256.h"

using namespace std;

class Node{
public:   
    string hash;
    string preHash;
    string locationX;
    string locationY;
    string locationZ;
    time_t myTime;
    
    Node(string locationX,string locationY ,string locationZ, string preHash);
};
#endif