#include "BlockChain.hpp"
using namespace std;
// using namespace BlockChain;


using namespace std;

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
    
    ofstream myFile("blockchain_data.csv", ios::trunc);
    if (myFile.is_open()){
        myFile << "hash; preHash; time; locationX; locationY; locationZ" << endl;
        myFile.close();
        save(node);
    }
    else{
        cout << "erro ao criar arquivo" << endl;
    }
}

void BlockChain::save(Node node){
    ofstream myFile("blockchain_data.csv", ios::app);
    if(myFile.is_open()){
        myFile
            << node.hash
            << "; " 
            << node.preHash 
            << "; "
            << ctime(&node.myTime)
            << "; "
            << node.locationX
            << "; "
            << node.locationY
            << "; "
            << node.locationZ
            << endl;
        myFile.close();
    }else{
        cout << "erro ao criar arquivo" << endl;
    }
}

void BlockChain::addNode(Node node){
    save(node);
    chain.push_back(node);
}

Node BlockChain::lastNode(){
    return chain.back();
}
