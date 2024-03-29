#include "BlockChain.hpp"

using namespace std;

int main(){
    BlockChain bChain = BlockChain();
    for (int i = 0;i<10;i++){
        string cord =  to_string(i);
        Node block = Node(cord,cord,cord,bChain.lastNode().hash);
        bChain.addNode(block);
    }
    for (Node x : bChain.chain){
        cout << "x: " 
            << x.locationX 
            << " y: " 
            << x.locationY 
            << " z: " 
            << x.locationZ 
            <<" time: "
            << ctime(&x.myTime) 
            << " hash: "
            << x.hash
            << " preHash: "
            << x.preHash
            << endl;
    }
    return 0;
}