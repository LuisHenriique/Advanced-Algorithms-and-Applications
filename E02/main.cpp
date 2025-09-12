#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

// Struct auxiliar contém as informações de data e valor registrado
struct DayValue
{
    int day;
    int month;
    int year;
    float value;
};

/*Função responsável por exibir o resultado na saída*/
void print(const vector<DayValue> &vec, int qtd_days, float sum, float porcentage)
{
    printf("%d dias (", qtd_days);
    for (auto &t : vec)
    {
        printf("%02d/%02d/%04d", t.day, t.month, t.year); // (DD/MM/AAAA)
        if (&t != &vec.back())                            // Se não for o último elemento ele coloca a vírgula
            printf(", ");
    }

    printf(") | soma=%.2f | %.2f%% dos dias totais", sum, porcentage);
}

/*Função responsável por realizar o algoritmo guloso*/
void greedyGreaterSum(const vector<DayValue> &vec, int &qtd_days, float &sum_smallest_set, vector<DayValue> &result)
{
    float soma_total_ganhos = 0; // Variável responsável por guardar a soma dos ganhos total( de todos os dias)

    for (int j = 0; j < vec.size(); j++)
    {
        // Soma todos os ganhos de todos os dias
        soma_total_ganhos += vec[j].value;
    }

    int i = 0;
    // Enquanto soma dos ganhos do conjunto solução <= (Soma total dos ganhos - soma dos ganhos do conjunto solução)
    while ((i < vec.size()) && (sum_smallest_set <= (soma_total_ganhos - sum_smallest_set)))
    {
        result.push_back(vec[i]);           // Add os maiores elementos primeiro no conjunto solução
        sum_smallest_set += (vec[i].value); // Incrementa o seu valor de soma
        i++;
    }
    qtd_days = i; // Quantidade de dias do conjunto solução
}
int main()
{
    int x_testes; // Quantidade de casos testes
    cin >> x_testes;
    while (x_testes > 0)
    {
        vector<DayValue> vec; // Vetor de structs (DayValue)

        int n_days;  // Quantidade de dias
        string date; // Data DD/MM/AAAA
        float value; // valor obtido no dia

        cin >> n_days;

        for (int i = 0; i < n_days; i++)
        {
            cin >> date >> value;

            int d = stoi(date.substr(0, 2)); // Converte "DD" para int
            int m = stoi(date.substr(3, 2)); // Converte "MM" para int
            int a = stoi(date.substr(6, 4)); // Converte "AAAA" para int
            vec.push_back({d, m, a, value}); // Adiciona no vetor de struct
        }

        // Ordena o vetor em ordem descrecente usando sort com lambda
        sort(vec.begin(), vec.end(), [](const DayValue &a, const DayValue &b)
             { return a.value > b.value; });

        int qtd_days;               // Quantidade de dias que tem no conjunto solução
        float sum_smallest_set = 0; // Guarda a soma total do conjunto solução

        // Conjunto solução (Menor conjunto de dias cujo a soma dos ganhos é menor que a soma dos ganhos dos dias restantes)
        vector<DayValue> result;
        greedyGreaterSum(vec, qtd_days, sum_smallest_set, result);

        // Ordena resultado em ordem cronológica
        sort(result.begin(), result.end(), [](const DayValue &a, const DayValue &b)
             {
            if(a.year != b.year) return a.year < b.year; 
            if(a.month != b.month) return a.month < b.month;
            return a.day < b.day; });

        float porcentage = (qtd_days * 100.0f) / n_days;       // Calcula a porcentagem de dias no conjunto solução em relação ao total de dias
        print(result, qtd_days, sum_smallest_set, porcentage); // Chamada da função que exibe os valores
        printf("\n");

        x_testes--; // Decrementa a quantidade de testes
    }

    return 0;
}