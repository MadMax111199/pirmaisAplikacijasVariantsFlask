import ast
import pymysql
from flask import Flask, render_template, request, session, redirect
import re
import numpy as np
import datetime


#////////// config
SECRET_KEY = 'dsvrsgkvergwerfercdgrwhjhrgregtwrhkokokojwfoeowg'
host = "maxonbtc.beget.tech"
user = "maxonbtc_test"
password = "cagnN%9n"
db_name = "maxonbtc_test"


app = Flask(__name__)
app.config['TESTING'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object(__name__)


arrFull = ["Daugavpils", "Ogre", "Liepaja", "Ventspils", "Sigulda", "Balvi", "Saldus"] #plus Riga

def sort(array):
    start_time = datetime.datetime.now()
    returnArr = []

    towns = np.towns = mainArr = \
        ([[0, 226, 36, 217, 188, 55, 220, 120],
        [226, 0, 191, 406, 397, 210, 182, 318],
        [36, 191, 0, 253, 223, 51, 210, 154],
        [217, 406, 253, 0, 117, 268, 434, 99],
        [188, 397, 223, 117, 0, 238, 404, 108],
        [55, 210, 51, 268, 238, 0, 169, 170],
        [220, 182, 210, 434, 404, 169, 0, 335],
        [120, 318, 154, 99, 108, 170, 335, 0], ])

    notDelete = []
    delete = []
    notDelete.append(0)

    for spec in array:
        if spec["city"] == 'Rīga': notDelete.append(0)
        if spec["city"] == 'Daugavpils': notDelete.append(1)
        if spec["city"] == 'Ogre': notDelete.append(2)
        if spec["city"] == 'Liepaja': notDelete.append(3)
        if spec["city"] == 'Ventspils': notDelete.append(4)
        if spec["city"] == 'Sigulda': notDelete.append(5)
        if spec["city"] == 'Balvi': notDelete.append(6)
        if spec["city"] == 'Saldus': notDelete.append(7)


    for x in range(len(towns)):
        if x not in notDelete:
            delete.append(x)

    newArr = []

    for town in towns:
        row = np.row = np.delete(town, delete)
        row = row.tolist()
        newArr.append(row)

    for arrNum in range(len(newArr)-1, -1, -1):
        if arrNum in delete:
            newArr.pop(arrNum)


    path = []
    pathGlobal = 0
    distance = 0
    counter = 0
    minPath = 10000
    minCounter = 0

    if len(newArr) == 2:
        returnArr = array
        for x in range(len(mainArr)):
            if array[0]['city'] == arrFull[x]:
                distance = int(mainArr[0][x+1]) * 2
                break

    if len(newArr) == 3:
        for i1 in range(1):
            for i2 in range(len(newArr)):
                for i3 in range(len(newArr)):
                    for i4 in range(1):
                        if (i1 != i2) and (i1 != i3) and (i2 != i3) and (i1 == i4) and (i2 != i4) and (i3 != i4):
                            path.insert(counter, str(i1 + 1) +str(i2 + 1) +str(i3 + 1)+ str(i4 + 1))
                            if ((newArr[i1][i2] + newArr[i2][i3] + towns[i3][i4]) < minPath):
                                a = newArr[i1][i2]
                                b = newArr[i2][i3]
                                c = newArr[i3][i4]
                                minPath = a + b + c
                                minCounter = counter
                            counter += 1
        print('Путь с самой короткой длиной маршрута: ' + str(path[minCounter]) + '(' + str(minPath) + ' км.)')
        pathGlobal = str(path[minCounter])
        distance = minPath

    if len(newArr) == 4:
        for i1 in range(1):
            for i2 in range(len(newArr)):
                for i3 in range(len(newArr)):
                    for i4 in range(len(newArr)):
                        for i5 in range(1):
                            if (i1 != i2) and (i1 != i3) and (i1 != i4) and (i1 == i5) and (i2 != i3) and (i2 != i4) and (i2 != i5) and (i3 != i4) and (i3 != i5) and (i4 != i5):
                                path.insert(counter, str(i1 + 1)+ str(i2 + 1)+ str(i3 + 1)+ str(i4 + 1)+ str(i5 + 1))
                                if ((newArr[i1][i2] + newArr[i2][i3] + towns[i3][i4] + towns[i4][i5]) < minPath):
                                    a = newArr[i1][i2]
                                    b = newArr[i2][i3]
                                    c = newArr[i3][i4]
                                    d = towns[i4][i5]
                                    minPath = a + b + c + d
                                    minCounter = counter
                                counter += 1
        print('Путь с самой короткой длиной маршрута: ' + str(path[minCounter]) + '(' + str(minPath) + ' км.)')
        pathGlobal = str(path[minCounter])
        distance = minPath

    if len(newArr) == 5:
        for i1 in range(1):
            for i2 in range(len(newArr)):
                for i3 in range(len(newArr)):
                    for i4 in range(len(newArr)):
                        for i5 in range(len(newArr)):
                            for i6 in range(1):
                                if (i1 != i2) and (i1 != i3) and (i1 != i4) and (i1 != i5) and (i1 == i6) and (i2 != i3) and (i2 != i4) and (i2 != i5) and (i2 != i6) and (i3 != i4) and (i3 != i5) and (i3 != i6) and (i4 != i5) and (i4 != i6) and (i5 != i6):
                                    path.insert(counter, str(i1 + 1) + str(i2 + 1) + str(i3 + 1) + str(i4 + 1) + str(i5 + 1)+ str(i6 + 1))
                                    if ((newArr[i1][i2] + newArr[i2][i3] + towns[i3][i4] + towns[i4][i5] + towns[i5][i6]) < minPath):
                                        a = newArr[i1][i2]
                                        b = newArr[i2][i3]
                                        c = newArr[i3][i4]
                                        d = towns[i4][i5]
                                        e = towns[i5][i6]
                                        minPath = a + b + c + d + e
                                        minCounter = counter
                                    counter += 1
        print('Путь с самой короткой длиной маршрута: ' + str(path[minCounter]) + '(' + str(minPath) + ' км.)')
        pathGlobal = str(path[minCounter])
        distance = minPath

    if len(newArr) == 6:
        for i1 in range(1):
            for i2 in range(len(newArr)):
                for i3 in range(len(newArr)):
                    for i4 in range(len(newArr)):
                        for i5 in range(len(newArr)):
                            for i6 in range(len(newArr)):
                                for i7 in range(1):
                                    if (i1 != i2) and (i1 != i3) and (i1 != i4) and (i1 != i5) and (i1 != i6) and (i1 == i7) and (i2 != i3) and (i2 != i4) and (i2 != i5) and (i2 != i6) and (i2 != i7) and (i3 != i4) and (i3 != i5) and (i3 != i6) and (i3 != i7) and (i4 != i5) and (i4 != i6) and (i4 != i7) and (i5 != i6) and (i5 != i7) and (i6 != i7):
                                        path.insert(counter, str(i1 + 1) + str(i2 + 1) + str(i3 + 1) + str(i4 + 1) + str(i5 + 1)+ str(i6 + 1)+ str(i7 + 1))
                                        if ((newArr[i1][i2] + newArr[i2][i3] + towns[i3][i4] + towns[i4][i5] + towns[i5][i6]+ towns[i6][i7]) < minPath):
                                            a = newArr[i1][i2]
                                            b = newArr[i2][i3]
                                            c = newArr[i3][i4]
                                            d = towns[i4][i5]
                                            e = towns[i5][i6]
                                            f = towns[i6][i7]
                                            minPath = a + b + c + d + e + f
                                            minCounter = counter
                                        counter += 1
        print('Путь с самой короткой длиной маршрута: ' + str(path[minCounter]) + '(' + str(minPath) + ' км.)')
        pathGlobal = str(path[minCounter])
        distance = minPath

    if len(newArr) == 7:
        for i1 in range(1):
            for i2 in range(len(newArr)):
                for i3 in range(len(newArr)):
                    for i4 in range(len(newArr)):
                        for i5 in range(len(newArr)):
                            for i6 in range(len(newArr)):
                                for i7 in range(len(newArr)):
                                    for i8 in range(1):
                                        if (i1 != i2) and (i1 != i3) and (i1 != i4) and (i1 != i5) and (i1 != i6) and (i1 != i7) and (i1 == i8) and (i2 != i3) and (i2 != i4) and (i2 != i5) and (i2 != i6) and (i2 != i7) and (i2 != i8) and (i3 != i4) and (i3 != i5) and (i3 != i6) and (i3 != i7) and (i3 != i8) and (i4 != i5) and (i4 != i6) and (i4 != i7) and (i4 != i8) and (i5 != i6) and (i5 != i7) and (i5 != i8)  and (i6 != i7)  and (i6 != i8)  and (i7 != i8):
                                            path.insert(counter, str(i1 + 1) + str(i2 + 1) + str(i3 + 1) + str(i4 + 1) + str(i5 + 1)+ str(i6 + 1)+ str(i7 + 1)+ str(i8 + 1))
                                            if ((newArr[i1][i2] + newArr[i2][i3] + towns[i3][i4] + towns[i4][i5] + towns[i5][i6]+ towns[i6][i7]+ towns[i7][i8]) < minPath):
                                                a = newArr[i1][i2]
                                                b = newArr[i2][i3]
                                                c = newArr[i3][i4]
                                                d = towns[i4][i5]
                                                e = towns[i5][i6]
                                                f = towns[i6][i7]
                                                g = towns[i7][i8]
                                                minPath = a + b + c + d + e + f + g
                                                minCounter = counter
                                            counter += 1
        print('Путь с самой короткой длиной маршрута: ' + str(path[minCounter]) + '(' + str(minPath) + ' км.)')
        pathGlobal = str(path[minCounter])
        distance = minPath

    if len(newArr) == 8:
        for i1 in range(1):
            for i2 in range(len(newArr)):
                for i3 in range(len(newArr)):
                    for i4 in range(len(newArr)):
                        for i5 in range(len(newArr)):
                            for i6 in range(len(newArr)):
                                for i7 in range(len(newArr)):
                                    for i8 in range(len(newArr)):
                                        for i9 in range(1):
                                            if (i1 != i2) and (i1 != i3) and (i1 != i4) and (i1 != i5) and (i1 != i6) and (i1 != i7) and (i1 != i8) and (i1 == i9) and (i2 != i3) and (i2 != i4) and (i2 != i5) and (i2 != i6) and (i2 != i7) and (i2 != i8) and (i2 != i9) and (i3 != i4) and (i3 != i5) and (i3 != i6) and (i3 != i7) and (i3 != i8) and (i3 != i9) and (i4 != i5) and (i4 != i6) and (i4 != i7) and (i4 != i8) and (i4 != i9) and (i5 != i6) and (i5 != i7) and (i5 != i8) and (i5 != i9) and (i6 != i7) and (i6 != i8) and (i6 != i9) and (i7 != i8) and (i7 != i9) and (i8 != i9):
                                                path.insert(counter, str(i1 + 1) + str(i2 + 1) + str(i3 + 1) + str(i4 + 1) + str(i5 + 1)+ str(i6 + 1)+ str(i7 + 1)+ str(i8 + 1)+ str(i9 + 1))
                                                if ((newArr[i1][i2] + newArr[i2][i3] + towns[i3][i4] + towns[i4][i5] + towns[i5][i6]+ towns[i6][i7]+ towns[i7][i8]) < minPath):
                                                    a = newArr[i1][i2]
                                                    b = newArr[i2][i3]
                                                    c = newArr[i3][i4]
                                                    d = towns[i4][i5]
                                                    e = towns[i5][i6]
                                                    f = towns[i6][i7]
                                                    g = towns[i7][i8]
                                                    h = towns[i8][i9]
                                                    minPath = a + b + c + d + e + f + g + h
                                                    minCounter = counter
                                                counter += 1
        print('Путь с самой короткой длиной маршрута: ' + str(path[minCounter]) + '(' + str(minPath) + ' км.)')
        pathGlobal = str(path[minCounter])
        distance = minPath

        if len(newArr) == 8:
            for i1 in range(1):
                for i2 in range(len(newArr)):
                    for i3 in range(len(newArr)):
                        for i4 in range(len(newArr)):
                            for i5 in range(len(newArr)):
                                for i6 in range(len(newArr)):
                                    for i7 in range(len(newArr)):
                                        for i8 in range(len(newArr)):
                                            for i9 in range(1):
                                                if (i1 != i2) and (i1 != i3) and (i1 != i4) and (i1 != i5) and (
                                                        i1 != i6) and (i1 != i7) and (i1 != i8) and (i1 == i9) and (
                                                        i2 != i3) and (i2 != i4) and (i2 != i5) and (i2 != i6) and (
                                                        i2 != i7) and (i2 != i8) and (i2 != i9) and (i3 != i4) and (
                                                        i3 != i5) and (i3 != i6) and (i3 != i7) and (i3 != i8) and (
                                                        i3 != i9) and (i4 != i5) and (i4 != i6) and (i4 != i7) and (
                                                        i4 != i8) and (i4 != i9) and (i5 != i6) and (i5 != i7) and (
                                                        i5 != i8) and (i5 != i9) and (i6 != i7) and (i6 != i8) and (
                                                        i6 != i9) and (i7 != i8) and (i7 != i9) and (i8 != i9):
                                                    path.insert(counter, str(i1 + 1) + str(i2 + 1) + str(i3 + 1) + str(
                                                        i4 + 1) + str(i5 + 1) + str(i6 + 1) + str(i7 + 1) + str(
                                                        i8 + 1) + str(i9 + 1))
                                                    if ((newArr[i1][i2] + newArr[i2][i3] + towns[i3][i4] + towns[i4][
                                                        i5] + towns[i5][i6] + towns[i6][i7] + towns[i7][i8]) < minPath):
                                                        a = newArr[i1][i2]
                                                        b = newArr[i2][i3]
                                                        c = newArr[i3][i4]
                                                        d = towns[i4][i5]
                                                        e = towns[i5][i6]
                                                        f = towns[i6][i7]
                                                        g = towns[i7][i8]
                                                        h = towns[i8][i9]
                                                        minPath = a + b + c + d + e + f + g + h
                                                        minCounter = counter
                                                    counter += 1
            print('Путь с самой короткой длиной маршрута: ' + str(path[minCounter]) + '(' + str(minPath) + ' км.)')
            pathGlobal = str(path[minCounter])
            distance = minPath

    if len(newArr) == 9:
        for i1 in range(1):
            for i2 in range(len(newArr)):
                for i3 in range(len(newArr)):
                    for i4 in range(len(newArr)):
                        for i5 in range(len(newArr)):
                            for i6 in range(len(newArr)):
                                for i7 in range(len(newArr)):
                                    for i8 in range(len(newArr)):
                                        for i9 in range(len(newArr)):
                                            for i10 in range(1):
                                                if (i1 != i2) and (i1 != i3) and (i1 != i4) and (i1 != i5) and (i1 != i6) and (i1 != i7) and (i1 != i8) and (i1 != i9) and (i1 == i10) and (i2 != i3) and (i2 != i4) and (i2 != i5) and (i2 != i6) and (i2 != i7) and (i2 != i8) and (i2 != i9) and (i2 != i10) and (i3 != i4) and (i3 != i5) and (i3 != i6) and (i3 != i7) and (i3 != i8) and (i3 != i9) and (i3 != i10) and (i4 != i5) and (i4 != i6) and (i4 != i7) and (i4 != i8) and (i4 != i9) and (i4 != i10) and (i5 != i6) and (i5 != i7) and (i5 != i8) and (i5 != i9) and (i5 != i10) and (i6 != i7) and (i6 != i8) and (i6 != i9) and (i6 != i10) and (i7 != i8) and (i7 != i9) and (i7 != i10) and (i8 != i9) and (i8 != i10) and (i9 != i10):
                                                    path.insert(counter, str(i1 + 1) + str(i2 + 1) + str(i3 + 1) + str(i4 + 1) + str(i5 + 1)+ str(i6 + 1)+ str(i7 + 1)+ str(i8 + 1)+ str(i9 + 1)+ str(i10 + 1))
                                                    if ((newArr[i1][i2] + newArr[i2][i3] + towns[i3][i4] + towns[i4][i5] + towns[i5][i6]+ towns[i6][i7]+ towns[i7][i8]+ towns[i8][i9]) < minPath):
                                                        a = newArr[i1][i2]
                                                        b = newArr[i2][i3]
                                                        c = newArr[i3][i4]
                                                        d = towns[i4][i5]
                                                        e = towns[i5][i6]
                                                        f = towns[i6][i7]
                                                        g = towns[i7][i8]
                                                        h = towns[i8][i9]
                                                        q = towns[i9][i10]
                                                        minPath = a + b + c + d + e + f + g + h + q
                                                        minCounter = counter
                                                    counter += 1
        print('Путь с самой короткой длиной маршрута: ' + str(path[minCounter]) + '(' + str(minPath) + ' км.)')
        pathGlobal = str(path[minCounter])
        distance = minPath


    arrFilter = []
    arrTrueDirection = []

    if len(newArr) != 2:
        for x in array:
            arrFilter.append(x["city"])
    if len(newArr) != 2:
        for x in arrFull:
            if x in arrFilter:
                arrTrueDirection.append(x)
            else:
                continue
    arrSortedDirection = []
    if len(newArr) != 2:
        for x in str(pathGlobal):
            if int(x) != 1:
                arrSortedDirection.append(arrTrueDirection[int(x)-2])
    if len(newArr) != 2:
        for poz in range(len(arrSortedDirection)):
            for x in array:
                if x['city'] == arrSortedDirection[poz]:
                    returnArr.append(x)
    for x in range(len(returnArr)):
        returnArr[x]['distance'] = distance
    print(datetime.datetime.now() - start_time)
    return returnArr

@app.route('/')
def loginCheck():
    try:
        if session["acces"] == True:
            return redirect("/route")
        else:
            return redirect("/main")
    except:
        return redirect("/main")
def userRequest():
    users = []
    try:
        connection = pymysql.connect(host=host, port=3306, user=user, password=password, database=db_name,cursorclass=pymysql.cursors.DictCursor)
        print('Succses!')
        try:
            with connection.cursor() as cursor:
                create_table_query = "select * from users"
                cursor.execute(create_table_query)
                rows = cursor.fetchall()
                for row in rows:
                    users.append(row)
                print('Table done!')
        finally:
            connection.close()
    except Exception as ex:
        print('Ereror')
        print(ex)

    return users

@app.before_first_request
def before_first_request_func():
    userRequest()

@app.route('/main')
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    users = userRequest()
    if request.method == 'POST':
        username = str(request.form['username'])
        userPassword = str(request.form['password'])
        for user in users:
            if str(user["username"]) == str(username) and str(user["password"]) == str(userPassword):
                session["acces"] = True
                session["username"] = username
                session["userPassword"] = userPassword
                if user["route"]:
                    new = re.sub('@', '\'', user["route"])
                    session["routs"] = ast.literal_eval(new)
                    session["routs"] = session["routs"]
                    return redirect("/route")
                else:
                    session["routs"] = []
                    return redirect("/route")
            else:
                session["acces"] = False
                session["username"] = username
                session["userPassword"] = userPassword
        return render_template('login.html')
    return render_template('login.html')

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        username = str(request.form['username'])
        mail = str(request.form['email'])
        userPassword = str(request.form['password'])
        try:
            connection = pymysql.connect(host=host, port=3306, user=user, password=password, database=db_name,cursorclass=pymysql.cursors.DictCursor)
            print('Succses!')
            try:
                with connection.cursor() as cursor:
                    create_table_query = f"INSERT INTO `users` (`username`, `mail`, `password`) " \
                                         f"VALUES ('{str(username)}', '{str(mail)}', '{str(userPassword)}')"
                    cursor.execute(create_table_query)
                    connection.commit()
                    create_table_query = "select * from users"
                    cursor.execute(create_table_query)
                    cursor.fetchall()
                    print('Table done!')
            finally:
                connection.close()
                return render_template('login.html')
        except Exception as ex:
            print('Error')
            print(ex)
    return render_template('register.html')

@app.route('/route', methods=["POST", "GET"])
def route():
    if session["acces"] == True:
        if request.method == 'POST':
            req = request.get_json(force=True)
            if (str(req['type']) == 'clean'):
                try:
                    connection = pymysql.connect(host=host, port=3306, user=user, password=password, database=db_name,cursorclass=pymysql.cursors.DictCursor)
                    print('Succses!')
                    try:
                        with connection.cursor() as cursor:
                            create_table_query = f"UPDATE `users` SET `route` = '[]' WHERE `users`.`username` = '{str(session['username'])}'"
                            cursor.execute(create_table_query)
                            connection.commit()
                    finally:
                        connection.close()
                except Exception as ex:
                    print('Error')
                    print(ex)
                session["routs"] = []
            else:
                addList = {}
                addList["name"] = str(req['peopleName'])
                addList["surname"] = str(req['peopleSurname'])
                addList["city"] = str(req['peopleCity'])
                addList["adress"] = str(req['peopleAdress'])
                addList["tel"] = str(req['peopleTel'])
                addList["distance"] = ''
                session["routs"].append(addList)
                session["routs"] = session["routs"]
                session["routs"] = sort(session["routs"])
                try:
                    connection = pymysql.connect(host=host, port=3306, user=user, password=password, database=db_name,cursorclass=pymysql.cursors.DictCursor)
                    print('Succses!')
                    try:
                        with connection.cursor() as cursor:
                            query = f"{str(session['routs'])}"
                            newQuery = re.sub('\'', '@', str(query))
                            create_table_query = f"UPDATE `users` SET `route` = '{newQuery}' WHERE `users`.`username` = '{str(session['username'])}'"
                            cursor.execute(create_table_query)
                            connection.commit()
                    finally:
                        connection.close()
                except Exception as ex:
                    print('Error')
                    print(ex)
        exSesionCity = []
        exCity = []
        for x in session["routs"]:
            exSesionCity.append(x['city'])
        for x in arrFull:
            if x not in exSesionCity:
                exCity.append(x)
        return render_template('table.html', exCity=exCity)
    else:
        return redirect("/main")

@app.route('/singout', methods=["POST", "GET"])
def singout():
    session["acces"] = False
    session["username"] = ''
    session["userPassword"] = ''
    session["userPassword"] = []
    return redirect("/main")

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

