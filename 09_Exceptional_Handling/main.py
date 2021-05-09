

class SmallSizeException(Exception):
    pass

def printList(list_):
    try:
        if len(list_) < 10:
            raise SmallSizeException("The list size is too small")
        else:
            print(list_)
    except SmallSizeException as e:
        print(e)
    finally:
        pass

printList([i for i in range(5)])