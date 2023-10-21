import numpy as np
from fractions import Fraction

def multiply_polynomial(poly_a,poly_b): #higher power on the right
    # a = [1,1] = x+1
    # b = [-2,2] = 2x-2
    #return = [-2, 0, 2] = 2x^2-2
    results= []
    l = len(poly_a) + len(poly_b) -1
    for i in range(len(poly_a)):
        temp = [0] * l
        for j in range(len(poly_b)):
            temp[i+j] = poly_a[i]*poly_b[j]
        results.append(temp)
    results_sum = [sum(x) for x in zip(*results)]
    return results_sum

def calculate_lagrange_polynomial(points):
    #points = [[1, 3], [4, 4], [16, 5], [13, 9]]
    #input(multiply_polynomial([43,-73.333,38.5,-5.166],[-3,10.333,-5,0.666]))
    #returns with smallest power on the right
    polynomials = []
    for p in range(len(points)):
        new_list = points[:p]+points[p+1:]
        x_i = [sublist[0] for sublist in new_list]
        list_denominator = [points[p][0]-x for x in x_i ]
        denominator =1
        for num in list_denominator:
            denominator*=num
        #inverse = pow(denominator,mod-2,mod)
        numerator = [[1,-x] for x in x_i]
        start_eqn = numerator[0]
        for mul in range(1,len(numerator)):
            start_eqn = multiply_polynomial(start_eqn,numerator[mul])
        #start_eqn = [x%mod for x in start_eqn]
        eqn = [((1/denominator)*points[p][1]*x) for x in start_eqn]
        polynomials.append(eqn)
    sum_poly = [sum(x) for x in zip(*polynomials)]
    #sum_poly = [x%mod for x in sum_poly]
    sum_poly = sum_poly[::-1]
    #input(sum_poly)
    return sum_poly




gate_1 = []
gate_1.append([0,1,0,0,0,0])
gate_1.append([0,1,0,0,0,0])
gate_1.append([0,0,0,1,0,0])

gate_2 = []
gate_2.append([-1,0,0,0,0,0])
gate_2.append([0,1,0,0,0,0])
gate_2.append([0,0,0,0,1,0])

gate_3 = []
gate_3.append([0,0,0,1,1,0])
gate_3.append([1,0,0,0,0,0])
gate_3.append([0,0,0,0,0,1])

gate_4 = []
gate_4.append([-42,0,0,0,0,1])
gate_4.append([1,0,0,0,0,0])
gate_4.append([0,0,1,0,0,0])

gates = []
gates.append(gate_1)
gates.append(gate_2)
gates.append(gate_3)
gates.append(gate_4)


contraints = [[] for _ in range(len(gates[0]))]

for gate in gates:
    for i in range(len(gate)):
        contraints[i].append(gate[i])

# print(contraints)
polynomials = []

for contraint in contraints:
    poly_out = []
    for i in range(len(contraint[0])):
        tmp = []
        for j in range(len(contraint)):
            tmp.append([j+1,contraint[j][i]])
        #print(tmp)
        poly_out.append(calculate_lagrange_polynomial(tmp))
    polynomials.append(poly_out)

A = np.array(polynomials[0])
B = np.array(polynomials[1])
C = np.array(polynomials[2])
s = np.array([1,7,0,49,-7,42])

A_f = []
B_f = []
C_f = []
for i in range(len(A[0])):
    A_f.append(np.dot(A[:,i],s))
    B_f.append(np.dot(B[:,i],s))
    C_f.append(np.dot(C[:,i],s))

t = multiply_polynomial(A_f,B_f)

for i in range(len(C_f)):
    t[i]-=C_f[i]

print(t)


