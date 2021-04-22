#include "BlockChain.hpp"
using namespace std;
// using namespace BlockChain;


using namespace std;

BlockChain::BlockChain(){
    ifstream myFile("blockchain_data.csv");

    if(myFile.is_open()){
        string line;
        while(getline(myFile, line)){
            auto resVector = split(line, ';');
            Node node = Node(resVector[0],
                                resVector[1],
                                resVector[2],
                                resVector[3],
                                resVector[4],
                                resVector[5]);
            addNode(node);
        }
    }
    else{
        string locationX = "init",
            locationY = "init",
            locationZ = "init";
        Node node = Node(locationX, 
                        locationY, 
                        locationZ,
                        "init");

        addNode(node);
        
        ofstream myFile("blockchain_data.csv", ios::trunc);
        if (myFile.is_open()){
            myFile << "hash; preHash; time; locationX; locationY; locationZ;" << endl;
            myFile.close();
            save(node);
        }
        else{
            cout << "erro ao criar arquivo" << endl;
        }
    }
}

void BlockChain::save(Node node){
    ofstream myFile("blockchain_data.csv", ios::app);
    if(myFile.is_open()){
        string temp_time = ctime(&node.myTime);
        temp_time.pop_back();
        myFile
            << node.hash
            << "; " 
            << node.preHash 
            << "; "
            << temp_time
            << "; "
            << node.locationX
            << "; "
            << node.locationY
            << "; "
            << node.locationZ
            << ";"
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

vector<std::string> BlockChain::split(const string& text, char sep)
{
    std::vector<std::string> tokens;
    std::size_t start = 0, end = 0;

    while ((end = text.find(sep, start)) != std::string::npos)
    {
        tokens.push_back(text.substr(start, end - start));
        start = end + 1;
    }

    tokens.push_back(text.substr(start));
    return tokens;
}