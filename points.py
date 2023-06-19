import math

def distance_points(point_a, point_b):
    xa = point_a[0]
    xb = point_b[0]
    ya = point_a[1]
    yb = point_b[1]

    distance = ((xb - xa)**2 + (yb - ya)**2)**0.5

    return distance

def define_points(parametro):
    points = {}
    points_name = []
    points_name = set("".join(parametro))
    for index in points_name:
            points[index]=[0, 0]
    return [points, points_name]

def check_list(lista):
    for i in range(len(lista) - 1):
        if lista[i] >= lista[i + 1]:
            return False
    return True

def distance_list(parametro, points):
    lista = []
    for param in parametro:
        lista.append(distance_points(points[param[0]], points[param[1]]))

    return lista

def points_circulo(centro_x, centro_y, raio):
    coordenadas = []
    for angulo in range(0, 361, 10):
        radiano = math.radians(angulo)
        x = round(centro_x + raio * math.cos(radiano), 5)
        y = round(centro_y + raio * math.sin(radiano), 5)
        coordenadas.append([x, y])
    return coordenadas

def positions_points(parametro, points, points_name):
    print(not check_list(distance_list(parametro, points)))
    raios = {}
    possiveis_points = {}
    for name in points_name:
        possiveis_points[name] = None
    lista_distancias = distance_list(parametro, points)
    lista_distancias_old = list(lista_distancias)
    direcao = -1
    #while not check_list(distance_list(parametro, points)):
    #direcao = direcao
    for param in parametro[::direcao]:
        id = parametro.index(param)+1 
        if len(parametro) == id:
            raios[param] = id
            possiveis_points[param[1]] = [[0, 0]]
            n =  0
            while not lista_distancias[id-2] < lista_distancias[id-1]:
                pontos_circle = points_circulo(points[param[1]][0], points[param[1]][1], raios[param])
                possiveis_points[param[0]] = pontos_circle
                points[param[0]] = pontos_circle[n]
                n += 1
                if  n > len(pontos_circle):
                    n = 0
                    raios[param] += 0.10
                lista_distancias = distance_list(parametro, points)

        elif id:
            print(id)
            news_param1 = []
            news_param2 = []
            distancias= []
            print(id, lista_distancias)
            #while not lista_distancias_old[id-2] < lista_distancias[id-1] < lista_distancias[id]:
            print(id, id, id)
            params1 = possiveis_points[param[0]]
            params2 = possiveis_points[param[1]]
            if params1 and params2 and lista_distancias[id-1]:
                print("11",id, param)
                for param1 in params1:
                    for param2 in params2:
                        points_test = points
                        points_test[param[0]] = param1
                        points_test[param[1]] = param2
                        if check_list(distance_list(parametro, points_test)[id-1:]):
                            distancias.append(distance_points(param1, param2))
                            news_param1.append(param1)
                            news_param2.append(param2)

                points[param[0]] = news_param1[distancias.index(max(distancias))]
                points[param[1]] = news_param2[distancias.index(max(distancias))]

                possiveis_points[param[0]] = news_param1
                possiveis_points[param[1]] = news_param2
                lista_distancias = distance_list(parametro, points)
                print(lista_distancias)
                print(points)
            elif params1 or params2:
                print("22",id, param)
                if params1:
                    param_def = param[0]
                    param_indef = param[1]
                
                else:
                    param_def = param[1]
                    param_indef = param[0]
                pontos = []
                raios[param] = (lista_distancias[id])-1
                while not lista_distancias_old[id-2] < lista_distancias[id-1] < lista_distancias[id]:
                    for coor in possiveis_points[param_def]:
                        pontos_circle = points_circulo(coor[0], coor[1], raios[param])
                        pontos += pontos_circle
                        
                    possiveis_points[param_indef] = pontos
                    points[param_indef] = pontos_circle[0]
                    lista_distancias = distance_list(parametro, points)

        #lista_distancias_old = list(lista_distancias)
             

    return points, distance_list(parametro, points)
                

parametro = ["HB","HF","VH","VB","FB","VF"]
#parametro = ["HF", "HV","FV"]
points = define_points(parametro)[0]
points_name = define_points(parametro)[1]
#points = {"H":[0,0], "B":[0,2], "F":[1,2], "V":[2,0]}


print(positions_points(parametro, points, points_name))
#print(distance_list(parametro, points))

