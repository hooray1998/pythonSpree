seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons, start=1)))

# 打印乘法表

# first
print('\n'.join(["%d"%i for i in range(1,10)]))
# second
i =  5
print('\t'.join(["%d * %d = %d"%(i,j,i*j) for j in range(1,i+1)]))

#finally
print('\n'.join(['\t'.join(["%d * %d = %d"%(i,j,i*j) for j in range(1,i+1)]) for i in range(1,10)]))
#print('\n'.join(['\t'.join(["%d * %d = %d"%(j,i,i*j) for i in range(1,j+1)]) for j in range(1, 10)]))

names = ['bob', 'tom', 'alice', 'jerry']
print([s.upper() for s in names if len(s) > 3])

bob = {'pay': 3000, 'job': 'dev', 'age': 42, 'name': 'bob smith'}
sue = {'pay': 4000, 'job': 'hdw', 'age': 45, 'name': 'sue jones'}
people = [bob, sue]

[rec['age']+100 if rec['age'] >= 45 else rec['age'] for rec in people] # 注意for位置
