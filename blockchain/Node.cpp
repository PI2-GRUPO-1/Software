#include "Node.hpp"

using namespace std;

Node::Node(string locationX, string locationY, string locationZ){
    locationX = locationX;
    locationY = locationY;
    locationZ = locationZ;
    myTime = time(NULL);
}