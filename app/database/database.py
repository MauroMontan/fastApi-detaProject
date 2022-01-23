from dotenv import load_dotenv
import os
from deta import Deta

load_dotenv()

# if you don´t want to use .env, just add it as string. NOT RECOMMENDED
#  example "PROJECTKEY = "FIdwji3'2n"

PROJECTKEY = os.getenv("PROJECTKEY")

deta = Deta(PROJECTKEY)


class Database:
    # add any database you want in
    tables = {
        "USERS": deta.Base("USERS"),
    }

    def __init__(self) -> None:
        pass

    def table(self, databaseName: str):
        return self.tables[databaseName]


db = Database()
