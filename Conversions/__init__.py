class TempConverter:
    @staticmethod
    def f_to_c(f: float) -> float:
        return (f-32) * 5/9

    @staticmethod
    def c_to_f(c: float) -> float:
        return (c * 9/5) + 32
