#ifndef BLOCKCHAIN_HPP
#define BLOCKCHAIN_HPP

#include <vector>
#include <iostream>
#include <string>
#include <ctime>
#include "Node.hpp"


using namespace std;

class BlockChain{
public:
    vector<Node> chain;

    BlockChain();

    void addNode(Node node);
    Node lastNode();
};
#endif