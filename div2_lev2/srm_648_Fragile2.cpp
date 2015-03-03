/*============================================================================
* Name : srm_648_Fragile2.cpp
* Author: taikido
* Description: TopCoder SRM 648: Div2 L2 (Brute Force, Graph Theory)
* Sources: http://community.topcoder.com/stat?c=problem_statement&pm=13648
* Date: Tues.Mar.3.2015
*===========================================================================*/


#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

class Fragile2
{

public:
    vector<int> getNeighbors(vector<string> graph, int src)
    {
        string row = graph[src];
        vector<int> n;

        for(int i=0; i<row.length(); i++)
        {
            if (row[i] == 'Y')
                n.push_back(i);
        }

        return n;
    }

    void dfs(vector<string> graph, int src, vector<bool>& visited)
    {

        visited[src] = true;

        vector<int> n = getNeighbors(graph, src);

        for(int i=0; i<n.size(); i++)
        {
            if(!visited[n[i]])
                dfs(graph, n[i], visited);
        }
    }

    int numCC(vector<string> graph)
    {
        // printf("Entering numCC... \n\n");
        int V = graph.size();
        vector<bool> visited(V, false);

        int cc = 0;
        for(int i=0; i<V; i++)
        {
            if(!visited[i] && getNeighbors(graph, i).size() > 0)
            {
                // printf("[numCC] %d not visited \n", i);
                cc++;
                dfs(graph, i, visited);
            }
        }

        return cc;
    }

    vector<string> deleteVertex(vector<string> graph, int src)
    {
        vector<string> result = graph;

        string row = graph[src];

        for(int i=0; i<row.length(); i++)
        {
            if (row[i] == 'Y')
            {
                result[src][i] = 'N';
                result[i][src] = 'N';
            }
        }
        return result;
    }


    int countPairs(vector <string> graph)
    {
        int cc = numCC(graph);
        int V = graph.size();
        int num_pairs = 0;

        vector<bool> visited(V, false);

        for(int i=0; i<V; i++)
            for(int j=0; j<V; j++)
                if (i == j)
                    graph[i][j] = 'Y';


        for(int i=0; i<V; i++)
        {
            for(int j=0; j<V; j++)
            {

                if (i != j)
                {
                    // printf("*Processing (%d, %d)--------------\n\n", i, j);
                    vector <string> result = deleteVertex(graph, i);
                    // printVectors(result);
                    result = deleteVertex(result, j);
                    // printVectors(result); cout << endl;

                    int cc2 = numCC(result);

                    // printf("(%d, %d) -> %d \n\n", i, j, cc2);


                    if (cc2 > cc)
                        num_pairs++;
                }
            }
        }

        return num_pairs/2;
    }


    void printVectors(vector<string> graph)
    {
        int V = graph.size();
        for(int i = 0; i<V; i++)
        {
            for(int j=0; j<V; j++)
                printf("%c ", graph[i][j]);
            printf("\n");
        }
        printf("\n");

    }
};

void test()
{
    // string s[] = {"NYNN", "YNYN", "NYNY", "NNYN"};
    string s[] = {"NYNNNN", "YNYNNN", "NYNNNN", "NNNNYN", "NNNYNY", "NNNNYN"};

 //    string s[] = {"NYNYNNYYNN", "YNNNYNYYNN", "NNNNYNNNYN", "YNNNYYNNNN", "NYYYNNNNYN",
 // "NNNYNNNNYN", "YYNNNNNNNN", "YYNNNNNNYN", "NNYNYYNYNY", "NNNNNNNNYN"};

 //    string s[] = {"NNNYNNYNNNNNNNYYNNNY", "NNNNNNNNYNNNNNNNNNNN", "NNNNNNNNNNNNNNNNNNNN", "YNNNNNNNNNYNNNNNNNNN", "NNNNNNNYNNNNNYNNNNYN",
 // "NNNNNNNNNNNNNNNNYNNY", "YNNNNNNNNNNNNYYYNYNN", "NNNNYNNNNNNNNYYNNNNN", "NYNNNNNNNYNNNNNNNNNN", "NNNNNNNNYNNNYNNNNNYN",
 // "NNNYNNNNNNNNNNYNNNNN", "NNNNNNNNNNNNNNNNNNNN", "NNNNNNNNNYNNNNNNNYNN", "NNNNYNYYNNNNNNNNNNNN", "YNNNNNYYNNYNNNNNNNNN",
 // "YNNNNNYNNNNNNNNNYNNN", "NNNNNYNNNNNNNNNYNYNN", "NNNNNNYNNNNNYNNNYNNN", "NNNNYNNNNYNNNNNNNNNN", "YNNNNYNNNNNNNNNNNNNN"};

    int n = sizeof(s)/sizeof(s[0]);

    printf("n: %d \n", n);

    vector<string> graph(s, s+n);

    Fragile2 f;

    // int c = f.numCC(graph);
    int pairs = f.countPairs(graph);

    // printf("Number of CC: %d \n", c);
    printf("Number of pairs: %d \n", pairs);
}

int main()
{
    test();
}
