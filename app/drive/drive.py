from dotenv import load_dotenv
import os
from deta import Deta

load_dotenv()


# if you don´t want to use .env, just add it as string.
#  example "PROJECTKEY = "FIdwji3'2n"
# This drive file is for uploading files or images

PROJECTKEY = os.getenv("PROJECTKEY")

deta = Deta(PROJECTKEY)

# add any drives you want
drives = {
}
