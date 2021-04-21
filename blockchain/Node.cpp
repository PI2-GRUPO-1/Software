#include "Node.hpp"

using namespace std;

Node::Node(string locationX, string locationY, string locationZ){
    this->locationX = locationX;
    this->locationY = locationY;
    this->locationZ = locationZ;
    myTime = time(NULL);
}