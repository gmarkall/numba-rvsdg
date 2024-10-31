from numba_rvsdg import run_frontend

def f(x, y):
    if GLOBAL:
        return x
    else:
        return y

ir = run_frontend(f)

if __name__ == "__main__":
    ir.dump()
