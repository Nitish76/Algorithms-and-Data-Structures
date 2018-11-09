# Uses python3
'''The edit distance between two strings is the minimum number of operations (insertions, deletions, and
substitutions of symbols) to transform one string into another. It is a measure of similarity of two strings.
Edit distance has applications, for example, in computational biology, natural language processing, and spell
checking. The goal in this problem is to compute the edit distance between two strings.'''

'''Input Format: Each of the two lines of the input contains a string consisting of lower case latin letters.'''
'''Output Format: The edit distance between the given two strings.'''

'''Constraints: The length of both strings is at least 1 and at most 100'''



def edit_distance(s, t):
    n = len(s); m = len(t);
    D = [[0]*(m+1) for i in range(n+1)]
    for i in range(1,n+1):
        D[i][0] = i
    for i in range(1,m+1):
        D[0][i] = i
    #print(D)
    for j in range(1,m+1):
        for i in range(1,n+1):
            insertion = D[i][j-1] + 1;
            deletion = D[i-1][j] + 1;
            mismatch = D[i-1][j-1] + 1;
            match = D[i-1][j-1];
            if s[i-1]==t[j-1]:
                D[i][j] = min(insertion, deletion, match);
            else:
                D[i][j] = min(insertion, deletion, mismatch);
        
    #write your code here
    return D[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
