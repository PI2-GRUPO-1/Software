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
Node::Node(string hash,string preHash, string myTime, string locationX,string locationY ,string locationZ){
    this->locationX = locationX;
    this->locationY = locationY;
    this->locationZ = locationZ;
    this->preHash = preHash;
    this->hash = hash;
    this->myTime = parseToTime(myTime);
}

time_t Node::parseToTime(string myTime){
    struct tm tm;
    strptime(myTime.c_str(), "%a %b %d %H:%M:%S %Y", &tm);

    time_t time = mktime(&tm);
    return time;
}