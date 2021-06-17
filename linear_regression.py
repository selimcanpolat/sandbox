import sympy as smp

a = [1, 2, 3, 4, 5] # data points for x and y
y = [7,6,9,11,12]

m, n, x = smp.symbols("m n x")

sum = 0
for i in a:
    sum += (m * i + n - y[a.index(i)]) ** 2

J = sum/(2 * len(a)) # constructing the cost function

J_m = smp.diff(J,m) # first partial derivatives
J_n = smp.diff(J,n)

J_mm = smp.diff(J_m,m) # second partial derivatives
J_nn = smp.diff(J_n,n)
J_mn = smp.diff(J_m,n)

D = J_mm*J_nn-(J_mn)**2

critical_points = smp.solve([J_m,J_n]).values() # finding critical points (m, n)
counter = 0
for i in critical_points:
    counter += 1
    if counter == 1:
        m_final = i
    elif counter == 2:
        n_final = i

D.subs([(m,m_final),(n,n_final)]) # classification
J_mm.subs([(m,m_final),(n,n_final)])

if D>0 and J_mm>0:
    model = m_final * x + n_final # building the model

print(model)
