
class Prime:
    @classmethod
    def is_prime(cls, number: int):
        if not isinstance(number, int):
            return False
        if number <= 1:
            return False
        for checker in range(2, number):
            if number % checker == 0:
                return False
        return True


def main():
    Prime.is_prime(5)
    Prime.is_prime(6)
    Prime.is_prime(7)
    Prime.is_prime(9)
    Prime.is_prime(23)
    Prime.is_prime(1)
    Prime.is_prime(0.3)


if __name__ == '__main__':
    main()
