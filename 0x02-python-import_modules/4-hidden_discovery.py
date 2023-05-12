#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    identifiers = dir(hidden_4)
    for identifier in identifiers:
        if identifier[:2] != "__":
            print(identifier)
