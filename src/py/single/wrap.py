def exec(func):
    def internal(input):
        print("Input:", input)
        output = func(input)
        print("Output:", output)

        return output

    return internal