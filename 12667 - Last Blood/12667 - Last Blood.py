n,t,m = map(int, input().split())

problems = {}

for i in range(n):
    problems[chr(65+i)] = ['-', '-']

lst = []
for i in range(m):
    time, teamID, problem, verdict = input().split()
    
    if verdict == 'Yes' :
        
        if problems[problem][0]=='-':
            problems[problem][0] = time
            # problems[problem][1] = teamID
        elif problems[problem][0]!='-' and problems[problem][1]!=teamID and (problem+teamID) not in lst:
            problems[problem][0] = time
            problems[problem][1] = teamID

        if problem+teamID not in lst:
            lst.append(problem+teamID)


for i in range(n):
    print(chr(65+i), problems[chr(65+i)][0], problems[chr(65+i)][1])
            
        
