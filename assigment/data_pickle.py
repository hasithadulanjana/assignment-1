class Tes(object):
    def __init__(self):
        pass

    def __str__(self):
        return "Test"


def for_function():
    squares = []
    for x in range(10):
        squares.append(x**2)
    return squares



'''if __name__ == "__main__":
    import pickle
    # test1 = Tes()
    # files need to be opened as binary files
    with open('data.pickle', 'wb') as f:
        # pickle.dump(for_function(), f)
        # pickle.dump(test1, f)
        pickle.dump(Tes, f)
    with open('data.pickle', 'rb') as f:
        data = pickle.load(f)
    # print(id(test1))
    # print(id(data))
    # print(test1 == data)
    print(data)
    test1 = data()
    print(test1)
    print(for_function())
'''