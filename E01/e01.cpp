#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Node
{
    int id;               // identificador único
    bool diabetico;       // se tem diabetes (true/false)
    int fatherN, motherN; // ids do pai/mãe (temporário)
    Node *father;         // ponteiro para o pai
    Node *mother;         // ponteiro para a mãe
};

int main()
{
    // Variáveis
    int x_casos;
    int qtd_pessoas;
    int id, father, mother;
    char diabetico[4];

    cin >> x_casos; // Coleta da quantidade de casos

    while (x_casos >= 0)
    {
        cin >> qtd_pessoas; // Quantidade de pessoas

        std::vector<Node> nodes; // Vetor dinâmico de estruturas Node

        for (int j = 0; j < qtd_pessoas; j++)
        {
            // Lê as informações de cada paciente
            cin >> id >> diabetico >> father >> mother;

            // Guarda essas informações em um array
            nodes[id - 1].diabetico = (diabetico == "sim");
            nodes[id - 1].id = id;
            nodes[id - 1].fatherN = father;
            nodes[id - 1].motherN = mother;
        }
        x_casos--;
    }
    return 0;
}