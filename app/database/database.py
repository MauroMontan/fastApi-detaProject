from dotenv import load_dotenv
import os
from deta import Deta

load_dotenv()

# if you don´t want to use .env, just add it as string.
#  example "PROJECTKEY = "FIdwji3'2n"
# WARNING: USING THE PROJECT KEY AS STRING IS DANGEROUS 

PROJECTKEY = os.getenv("PROJECTKEY")

deta = Deta(PROJECTKEY)

# add any database you want
database = {
    "USERS": deta.Base("USERS"),
}
