#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

struct Request
{
    int id;       // Identificador do cliente
    int hour_r;   // Hora de retirada
    int minute_r; // Minuto de retirada
    int hour_d;   // Hora de devolução
    int minute_d; // Minuto de devolução
    int id_car;   // Identificador do carro
};

void greedy_selector_algorithm(vector<Request> &vec, vector<Request> &solution)
{

    solution.clear(); // Zerando os valores presente no conjunto solução, para evitar acumulo.

    // Ordenação da lista de solicitações de aluguel
    sort(vec.begin(), vec.end(), [](const Request &a, const Request &b)
         {
             if (a.hour_d != b.hour_d)
                 return a.hour_d < b.hour_d; // Ordena pela hora de devolução
             if (a.minute_d != b.minute_d)
                 return a.minute_d < b.minute_d; // Caso as horas de devolução seja igual, verifica os minutos.
             if (a.hour_r != b.hour_r)
                 return a.hour_r < b.hour_r; // Caso as horas e minutos sejam iguais, coloca como preferência quem tem a menor hora de retirada
             if (a.minute_r != b.minute_r)
                 return a.minute_r < b.minute_r; //  Caso o horario de devolução e hora de retirada sejam iguais, ordena pelos minutos do horario de retirada
             return a.id < b.id;                 // Ultimo caso, caso os horarios de devolução e retirada sejam iguais, ordena por user_id.
         });

    solution.push_back(vec[0]); // Adiciona a solicitação que tem o tempo de devolução que termina mais cedo.(elemento a0)
    int k = 0;
    for (int i = 1; i < vec.size(); i++)
    {
        int time_r = vec[i].hour_r * 60 + vec[i].minute_r; // Conversão o horário de retirada para minutos
        int time_d = vec[k].hour_d * 60 + vec[k].minute_d; // Conversão o horário de devolução para minutos

        if (time_r >= time_d)
        {
            solution.push_back(vec[i]);
            k = i;
        }
    }

    return;
}
void print(int car_id, const vector<Request> &vec)
{
    cout << car_id << ": " << vec.size() << " = ";
    for (auto &request : vec)
    {
        printf("%d", request.id);
        if (&request != &vec.back())
        {
            printf(", ");
        }
    }
}

int main()
{
    int x_testes; // Quantidade de casos testes
    cin >> x_testes;

    while (x_testes > 0)
    {

        int n_requests;                      // Quantidade de solicitações de aluguel
        int id;                              // User id
        string return_time, withdrawal_time; // Horario de devolução e horario de retirada
        int id_car;                          // Car id
        int qtd_model_cars;                  // Quantidade de modelos de carros
        map<int, vector<Request>> cars;      // Dicionario de listas, onde int = idCar, vector<Request> = lista de requisições para o respectivo idCar.
        vector<Request> solution;            // Conjunto solução

        cin >> qtd_model_cars;
        cin >> n_requests;

        for (int i = 0; i < n_requests; i++)
        {

            cin >> id >> withdrawal_time >> return_time >> id_car;
            // Insere no dicionário a lista de requisições para o respectivo id_car, se id_car(key do dicionário) não existir o dicionário cria uma.
            cars[id_car].push_back({id,
                                    stoi(withdrawal_time.substr(0, 2)), // Converte "HH" --> int
                                    stoi(withdrawal_time.substr(3, 2)), // Converte "MM" --> int
                                    stoi(return_time.substr(0, 2)),     // Converte "HH" --> int
                                    stoi(return_time.substr(3, 2)),     // Converte "MM" --> int
                                    id_car});
        }

        // Saída do programa
        bool first_loop = true;
        for (int car_id = 1; car_id <= qtd_model_cars; car_id++)
        {
            if (!first_loop)
                cout << " | "; // Separador entre modelos
            first_loop = false;

            // Verifica se a minha respectiva chave no dicionario tem um valor associado a ela
            if (cars.count(car_id))
            { // Chamada a função que executa o algoritmo guloso
                greedy_selector_algorithm(cars[car_id], solution);

                // Antes de imprimir a saida, ordena
                //  Ordena o conjunto solução em ordem crescente de tempo de retirada
                sort(solution.begin(), solution.end(), [](const Request &a, const Request &b)
                     {
                         if (a.hour_r != b.hour_r)
                             return a.hour_r < b.hour_r; // retorna o que tiver a menor hora
                         return a.minute_r < b.minute_r; // Retorna o que tiver o menor minuto
                     });

                print(car_id, solution);
            }
            else
            {
                cout << car_id << ": 0";
            }
        }
        cout << "\n";
        x_testes--; // Decremento dos casos testes
    }

    return 0;
}