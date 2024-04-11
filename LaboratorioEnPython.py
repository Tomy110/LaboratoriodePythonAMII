# Grupo: Martin Mercado, Pablo Maturano, Macarena Damiani y Tomas Limeres

# Punto 1
def metodo_euler(funcion, x0, y0, x_final, paso):
    x_actual = x0
    y_actual = y0

    while x_actual < x_final:
        y_actual = y_actual + paso * funcion(x_actual, y_actual)
        x_actual += paso

    return y_actual

def funcion(x, y):
    return 0.2 * x * y

x0 = 1
y0 = 1
x_final = 1.5

paso1 = 0.1
y_aprox_1 = metodo_euler(funcion, x0, y0, x_final, paso1)

paso2 = 0.05
y_aprox_2 = metodo_euler(funcion, x0, y0, x_final, paso2)

y_real = metodo_euler(funcion, x0, y0, x_final, 0.001)

error1 = abs(y_real - y_aprox_1)
error2 = abs(y_real - y_aprox_2)

print(f"Con paso de {paso1}: Aproximación de y(1.5) = {y_aprox_1}, Error = {error1}")
print(f"Con paso de {paso2}: Aproximación de y(1.5) = {y_aprox_2}, Error = {error2}")

# Punto 2
def fun(t, I):
    return 15 - 3 * I

def Euler(f, t0, I0, h, tf):
    t = t0
    I = I0
    while t <= tf:
        I += h * f(t, I)
        t += h
    return I

t0 = 0
I0 = 0
tf = 0.5

h = 0.1
aprox = Euler(fun, t0, I0, h, tf)
print(f"Aproximación de la corriente medio segundo después de cerrar el interruptor: {aprox} Amperios")


