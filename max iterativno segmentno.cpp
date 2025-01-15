#include <bits/stdc++.h>
using namespace std;

void build(vector<int> a, int n, vector<int> &v)
{
    for(int i=0;i<n;i++)
    v[i+n] = a[i];
    
    for(int i=n-1; i>=1; i--)
    {
        v[i] = max(v[i*2],v[i*2+1]);
    }
}

void update(int pos, int val, vector<int> &v, int n)
{
    pos+=n;
    
    v[pos] = val;
    
    while(pos>1)
    {
        pos = pos>>1; // pos /= 2
        
        v[pos] = max(v[pos*2],v[pos*2+1]);
    }
}

int query(int left, int right, vector<int> &v, int n)
{
    left+=n;
    right+=n+1; // [left,right+1)
    
    int maxe = -1000000005;
    
    if(left == right)
    return v[left];
    
    while(left<right)
    {
        if(left & 1) // left % 2 == 1
        {
            maxe = max(maxe, v[left]);
            
            left++;
        }
        
        if(right & 1) // right % 2 == 1  
        {
            right--;
            
            maxe = max(maxe,v[right]);
        }
        
        left = left>>1;
        right = right>>1;
    }
    
    return maxe;
}

int main()
{
    int n=0;
    cin >> n;
    
    vector<int> a(n,0);
    
    for(int i=0; i<n; i++)
    cin >> a[i];
    
    vector<int> s_tree(4*n,-1232482895);
    
    build(a,n,s_tree);
    
    for(int i:s_tree)
    cout << i << " ";
    
    cout << '\n';
    
    cout << query(0,n-1,s_tree,n) << '\n';
    
    update(2,234,s_tree,n);
    
    for(int i:s_tree)
    cout << i << " ";
    
    cout << '\n';
    
    cout << query(0,n-1,s_tree,n);
    
    return 0;
}