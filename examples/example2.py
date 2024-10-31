from numba_rvsdg import run_frontend

def f(x, y):
    for i in range(len(x)):
        x[i] = y[i] + 1

ir = run_frontend(f)
ir.dump()

if __name__ == "__main__":
    ir.dump()
