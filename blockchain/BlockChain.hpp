#ifndef BLOCKCHAIN_HPP
#define BLOCKCHAIN_HPP

#include <vector>
#include <iostream>
#include <string>
#include <ctime>
#include "Node.hpp"


using namespace std;

class BlockChain{
private:
    vector<Node> chain;
public:
    BlockChain();

    void addNode(Node node);
};
#endif