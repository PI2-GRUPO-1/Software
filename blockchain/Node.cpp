#include "Node.hpp"

using namespace std;

Node::Node(string locationX, string locationY, string locationZ,string preHash){
    this->locationX = locationX;
    this->locationY = locationY;
    this->locationZ = locationZ;
    this->preHash = preHash;
    myTime = time(NULL);
    stringstream ss;
    ss << myTime << preHash;
    hash = sha256(ss.str());
}