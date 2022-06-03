
>>> from sympy import solve, Symbol, sin, limit, matrix_symbols, diag, plot, zeros

# Question 1
# Solve the quadratic function x^2 + 2x - 8 = 0

x = Symbol('x')
expr = x ** 2 + 2 * x - 8
print(solve(expr, dict=True))
# [{x: 2}, {x: -4}]

# Question 2
# What is the function f(x) which is equal to its derivative?
expr = x * sin(x * x) + 1 >> expr

# Question 3
# Compute the area under f(x) = x^3 from x = 0 to x = 1

# Question 4
# Calculate

# Question 5
# Calculate

limit(1 + 1 / x, x, '+')
# Question 6
matrix_symbols([2, -3, -8, 7], [-2, -1, 2, -7], [1, 0, -3, 6])
diag()

# Question 7
# Do Matrix row operations. Update Row 2 to R2 + 3 * R1.
matrix_symbols.row(-2, -1, 2, -7) + 3 * (2, -3, -8, 7)
# Question 8
# Find determinant of M
M = matrix_symbols([2, -3, -8, 7], [-2, -1, 2, -7], [1, 0, -3, 6])
M.det()
# Question 9
# Find the following matrix's eigenvalue and eigen vector.
M = matrix_symbols([[9, -2]])
M.eigenvals()
M.eigenvects()
# Question 10
# Implement the Predator-prey model in python
alpha = 1.1
beta = 0.4
delta = 0.1
gamma = 0.4

params = [alpha, beta, delta, gamma]

y0 = [10, 1]

tspan = [0, 50]

plot(2, 1, 1)

plot('Time')
plot('Prey')

plot(2, 1, 2)

plot('Time')
plot('Predators')

alpha = params(1)
beta = params(2)
delta = params(3)
gamma = params(4)

X = 1
Y = 2

dy = zeros(2, 1)

dy = alpha * X - beta * X * Y
dy = delta * X * Y - gamma * Y
