#include "BlockChain.hpp"
using namespace std;
// using namespace BlockChain;



BlockChain::BlockChain(){
    string locationX = "init",
        locationY = "init",
        locationZ = "init";
    time_t myTime = time(NULL);
    Node node = Node(locationX, 
                    locationY, 
                    locationZ,
                    "init");

    addNode(node);
}

void BlockChain::addNode(Node node){
    chain.push_back(node);
}

Node BlockChain::lastNode(){
    return chain.back();
}
