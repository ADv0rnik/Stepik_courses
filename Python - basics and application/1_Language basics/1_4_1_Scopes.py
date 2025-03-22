"""
Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку создания
пространств имен и добавление в них переменных.
"""

namespaces = {
    "global": {
        "vars": set(),
        "parent": None
    },
}


def add_variable(namespace: str, var: str):
    if namespace in namespaces:
        namespaces[namespace].get("vars").add(var)


def create_namespace(namespace: str, parent: str):
    if namespace not in namespaces:
        namespaces[namespace] = {"vars": set(), "parent": parent}


def get_namespace(namespace: str, var: str):
    if var in namespaces[namespace]["vars"]:
        print(namespace)
    else:
        if namespaces[namespace]["parent"]:
            get_namespace(namespaces[namespace]["parent"], var)
        else:
            print(None)


functions = {
    "create": create_namespace,
    "add": add_variable,
    "get": get_namespace
}


def main(num: int):
    for _ in range(num):
        function_name, namespace, var = input().split()
        function = functions.get(function_name)
        function(namespace, var)


if __name__ == "__main__":
    n = int(input())
    main(n)
