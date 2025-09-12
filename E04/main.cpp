#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Quest
{
    int index;
    int level;
    int list_of_int[];
};

int main()
{

    int x_tests;

    cin >> x_tests;
    while (x_tests > 0)
    {
        int n_heroes, m_quests;
        cin >> n_heroes >> m_quests;

        vector<Quest> quests; // Vetor de quests
        int index, time;
        int list_of_int[m_quests - 1];

        for (int i = 0; i < n_heroes; i++)
        {
        }
        for (int j = 0; j < m_quests; j++)
        {
            quests.push_back({})
        }
        x_tests--;
    }

    return 0;
}