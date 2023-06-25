class FizzBuzz:
    @classmethod
    def fizzbuzz(cls, number: int):
        result = ""
        if number % 3 == 0:
            result = "Fizz"
        if number % 5 == 0:
            result += "Buzz"
        if result:
            return result
        return None


def main():
    print(type(FizzBuzz.fizzbuzz(2)))

if __name__=='__main__':
    main()






