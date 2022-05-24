from euler import Euler
from hamilton import Hamilton
import exceptions

FILE_TO_LOAD = "graph_file.txt"


def load_from_file():
    with open(FILE_TO_LOAD, "r") as graph_file:
        try:
            vertices, edges = map(int, graph_file.readline().split())

            edge_list = []
            for line in graph_file:
                edge = list(map(int, line.split()))
                if len(edge) != 2:
                    raise exceptions.BadValue
                if edge not in edge_list:
                    edge_list.append(edge)
                else:
                    raise exceptions.DoubledValue

            if len(edge_list) != edges:
                raise exceptions.Error
        except ValueError:
            print("Entered wrong value. Make sure the file is ok!")
            exit()
        except exceptions.DoubledValue:
            print("Edge was entered two times. Check the graph file!")
            exit()
        except exceptions.BadValue:
            print("One of edges is not correct. Has less/more than its start and end vertex!")
            exit()
        except exceptions.Error:
            print("Edges list size is not the same as entered edges count!")
            exit()
        return vertices, edge_list


def load_from_console():
    print("usage: <vertices_count> <edges_count>")
    vertices, edges = 0, 0
    edge_list = []
    try:
        vertices, edges = map(int, input().split())

        for _ in range(edges):
            edge = list(map(int, input().split()))
            if len(edge) != 2:
                raise exceptions.BadValue
            if edge not in edge_list:
                edge_list.append(edge)
            else:
                raise exceptions.DoubledValue
        if len(edge_list) != edges:
            raise exceptions.Error
    except ValueError:
        print("Entered wrong value. Make sure the file is ok!")
        exit()
    except exceptions.DoubledValue:
        print("Edge was entered two times. Check the graph file!")
        exit()
    except exceptions.BadValue:
        print("One of edges is not correct. Has less/more than its start and end vertex!")
        exit()
    except exceptions.Error:
        print("Edges list size is not the same as entered edges count!")
        exit()
    return vertices, edge_list


def menu():
    print("Choose loading method: ")
    print("1. console")
    print("2. file")

    method = input()
    if method == "1":
        vertices, edge_list = load_from_console()
        Euler(vertices, edge_list)
        Hamilton(vertices, edge_list)
    elif method == "2":
        vertices, edge_list = load_from_file()
        Euler(vertices, edge_list)
        Hamilton(vertices, edge_list)
    else:
        print("Wrong loading method")


if __name__ == '__main__':
    menu()
