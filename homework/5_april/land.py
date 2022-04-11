K=int(input('обхват по бьюсту:'))
M=int(input('по бедрам:'))
N=int(input('по талии:'))
T=int(input('рост:'))
P=int(input('вес:'))

L=(K*M*T)/((N**2)*P)
print(int(L))
