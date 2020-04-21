import psycopg2


def getData():
    try:
        connection = psycopg2.connect(user="foawmaqxxdiizl",
                                      password="c04d6c9147e4b5429cb4d0c5f01a9e8999b447a6e724f8bba7ef54a02fded82a",
                                      host="ec2-52-87-58-157.compute-1.amazonaws.com",
                                      port="5432",
                                      database="d6dvr900ccamgj")
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
