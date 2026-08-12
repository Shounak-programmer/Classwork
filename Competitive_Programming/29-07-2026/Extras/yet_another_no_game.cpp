//codeforces problem 282D, Round 173 (Div. 2)

#include <bits/stdc++.h>
using namespace std;
const int MAXV = 300;

int main(){
    int n;
    scanf("%d", &n);
    vector<int> a(n);
    for(auto &x : a) scanf("%d", &x);

    if(n == 1){
        puts(a[0] != 0 ? "BitLGM" : "BitAryo");
        return 0;
    }

    if(n == 2){
        static bool L[MAXV][MAXV];
        static bool hasA[MAXV], hasB[MAXV], hasDiag[2*MAXV+1];
        for(int s = 0; s <= 2*(MAXV-1); s++)
            for(int aa = max(0, s-(MAXV-1)); aa <= min(MAXV-1, s); aa++){
                int bb = s - aa;
                bool isN = hasA[bb] || hasB[aa] || hasDiag[aa-bb+MAXV];
                L[aa][bb] = !isN;
                if(!isN){ hasA[bb]=hasB[aa]=hasDiag[aa-bb+MAXV]=true; }
            }
        puts(L[a[0]][a[1]] ? "BitAryo" : "BitLGM");
        return 0;
    }

    // n == 3
    static bool L[MAXV][MAXV][MAXV];
    static bool hasA[MAXV][MAXV], hasB[MAXV][MAXV], hasC[MAXV][MAXV];
    static bool hasDiag[2*MAXV+1][2*MAXV+1];
    for(int s = 0; s <= 3*(MAXV-1); s++)
        for(int aa = max(0, s-2*(MAXV-1)); aa <= min(MAXV-1, s); aa++){
            int rem = s - aa;
            for(int bb = max(0, rem-(MAXV-1)); bb <= min(MAXV-1, rem); bb++){
                int cc = rem - bb;
                if(cc < 0 || cc >= MAXV) continue;
                bool isN = hasA[bb][cc] || hasB[aa][cc] || hasC[aa][bb]
                           || hasDiag[aa-bb+MAXV][aa-cc+MAXV];
                L[aa][bb][cc] = !isN;
                if(!isN){
                    hasA[bb][cc]=hasB[aa][cc]=hasC[aa][bb]=true;
                    hasDiag[aa-bb+MAXV][aa-cc+MAXV]=true;
                }
            }
        }
    puts(L[a[0]][a[1]][a[2]] ? "BitAryo" : "BitLGM");
    return 0;
}
