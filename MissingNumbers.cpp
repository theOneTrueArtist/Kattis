#include <iostream>

int main()
{
    std::ios_base::sync_with_stdio(false);
    int n;
    std::cin >> n;
    int foo[n+1];
    foo[0] = 0;
    for (int i = 1; i < n+1; i++){
        std::cin >> foo[i];
        for (int j = foo[i-1] + 1; j < foo[i]; j++){
            std::cout<<j<<"\n";
        }
    }
    if (foo[n] == n){
        std::cout << "good job" << std::endl;
    }
}
