import cmath

class RootFindingProblem:
    def __init__(self, f=None, df=None, g=None):
        self.f = f
        self.df = df
        self.g = g

    def solve(self, method, **kwargs):
        if method == "bisection":
            return self._bisection(**kwargs)
        elif method == "fixed_point":
            return self._fixed_point(**kwargs)
        elif method == "newton":
            return self._newton(**kwargs)
        elif method == "secant":
            return self._secant(**kwargs)
        elif method == "false_position":
            return self._false_position(**kwargs)
        elif method == "steffensen":
            return self._steffensen(**kwargs)
        elif method == "horner":
            return self._horner(**kwargs)
        elif method == "muller":
            return self._muller(**kwargs)
        else:
            raise ValueError("Unknown Method")

    def _bisection(self, a, b, tol=1e-6, max_iter=100):
        for _ in range(max_iter):
            c = (a + b) / 2
            if abs(self.f(c)) < tol:
                return c
            if self.f(a) * self.f(b) < 0:
                b = c
            else:
                a = c
        return c

    def _fixed_point(self, x0, tol=1e-6, max_iter=100):
        x = x0
        for _ in range(max_iter):
            x_new = self.g(x)
            if abs(x_new - x) < tol:
                return x_new
            x = x_new
        return x

    def _newton(self, x0, tol=1e-6, max_iter=100):
        x = x0
        for _ in range(max_iter):
            x_new = x - self.f(x) / self.df(x)
            if abs(x_new - x) < tol:
                return x_new
            x = x_new
        return x

    def _secant(self, x0, x1, tol=1e-6, max_iter=100):
        for _ in range(max_iter):
            x2 = x1 - (self.f(x1) * (x1 - x0)) / (self.f(x1) - self.f(x0))
            if abs(x2 - x1) < tol:
                return x2
            x0, x1 = x1, x2
        return x2

    def _false_position(self, a, b, tol=1e-6, max_iter=100):
        for _ in range(max_iter):
            c = (a * self.f(b) - b * self.f(a)) / (self.f(b) - self.f(a))
            if abs(self.f(c)) < tol:
                return c
            if self.f(a) * self.f(c) < 0:
                b = c
            else:
                a = c
        return c

    def _steffensen(self, x0, tol=1e-6, max_iter=100):
        x = x0
        for _ in range(max_iter):
            gx = self.g(x)
            ggx = self.g(gx)
            denominator = ggx - 2 * gx + x
            x_new = x - ((gx - x) ** 2) / denominator
            if abs(x_new - x) < tol:
                return x_new
            x = x_new
        return x

    def _horner(self, coeffs, x):
        result = coeffs[0]
        for c in coeffs[1:]:
            result = result * x + c
        return result

    def _muller(self, x0, x1, x2, tol=1e-6, max_iter=100):
        for _ in range(max_iter):
            h0 = x1 - x0
            h1 = x2 - x1
            d0 = (self.f(x1) - self.f(x0)) / h0
            d1 = (self.f(x2) - self.f(x1)) / h1
            a = (d1 - d0) / (h0 + h1)
            b = a * h1 + d1
            c = self.f(x2)
            rad = cmath.sqrt(b * b - 4 * a * c)
            if abs(b + rad) > abs(b - rad):
                den = b + rad
            else:
                den = b - rad
            x3 = x2 - (2 * c) / den
            if abs(x3 - x2) < tol:
                return x3
            x0, x1, x2 = x1, x2, x3
        return x3
