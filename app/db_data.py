import psycopg2


def getData():
    try:
        connection = psycopg2.connect(user="oeijnwzcwluxmu",
                                      password="f82857995279fc41b70869b10e3abad8edcc43aacdb41fd9c6b91c709d394508",
                                      host="ec2-54-147-209-121.compute-1.amazonaws.com",
                                      port="5432",
                                      database="d7seuhs2uh13ob")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from user_profile"
        cursor.execute(postgreSQL_select_Query)
        return cursor.fetchall()

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if(connection):
            cursor.close()
            connection.close()


def getUser(idNumber):
    try:
        connection = psycopg2.connect(user="Project1",
                                      password="password",
                                      host="localhost",
                                      database="Project1")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from user_profile where id="+idNumber
        cursor.execute(postgreSQL_select_Query)
        return cursor.fetchall()[0]

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if(connection):
            cursor.close()
            connection.close()
