#ifndef BLOCKCHAIN_HPP
#define BLOCKCHAIN_HPP

#include <vector>
#include <iostream>
#include <string>
#include <ctime>
#include <fstream>
#include "Node.hpp"


class BlockChain{
public:
    vector<Node> chain;

    BlockChain();

    void addNode(Node node);
    Node lastNode();
    void save(Node node);
};
#endif