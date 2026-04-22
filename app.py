import json
import os

import pymysql


def get_connection():
    return pymysql.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        connect_timeout=5,
        cursorclass=pymysql.cursors.DictCursor,
    )


def lambda_handler(event, context):
    connection = None

    try:
        connection = get_connection()

        with connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS items (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100)
                )
                """
            )
            cursor.execute("SELECT COUNT(*) AS total FROM items")
            total = cursor.fetchone()["total"]

        connection.commit()

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps(
                {
                    "message": "Lambda conectada correctamente a RDS MySQL",
                    "items_registrados": total,
                }
            ),
        }
    except Exception as error:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps({"error": str(error)}),
        }
    finally:
        if connection is not None:
            connection.close()
