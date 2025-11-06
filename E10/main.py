from itertools import count

def is_prime(n: int) -> bool:
    """Retorna True se n é primo (teste por tentativa até √n)."""
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

def next_prime(n: int) -> int:
    """Retorna o menor número primo maior que n."""
    return next(filter(is_prime, count(n + 1)))


def extend_euclid(a, b):
    """Algoritmo extendido do algoritmo de Euclides utilizado para encontrar o inverso multiplicativo"""
    if b == 0:
        return a, 1, 0
    else:
        d, xi, yi = extend_euclid(b, a % b)
        x = yi
        y =  xi - (a // b) * yi
        
        # como a e b serao primos entre si entao
        # d = mdc(a,b) = ax + by = 1
        return d,x,y
    
def main():
    n, t = map(int, input().split(' '))
    p = next_prime(n)

    # Calcula inverso multiplicativo de t
    # Como t e p sao primos entre si, a unica solucao para a equacao t*a ≡ 1 mod p 
    # e o inteiro x retornado por extend_euclid
    _,x,_ = extend_euclid(t,p)
    print(x % p)  # Normaliza o inverso no intervalo [0, p-1]
    
if __name__ == "__main__":
    main()