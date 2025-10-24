import os
from dotenv import load_dotenv
env= os.getenv("ENV","qa")
dotenv_file = f".env.{env}"

if os.path.exists(dotenv_file):
    load_dotenv(dotenv_file,override=True)
    print(f"Loaded environment from {dotenv_file}")
else:
    print(f"Environment variable not found: {dotenv_file}")
class EnvConfig:
    @property
    def ENV(self):
        return os.getenv("ENV","qa")

    @property
    def BASE_URL(self):
        return os.getenv("BASE_URL")
    #BASE_URL=os.getenv("BASE_URL")
    @property
    def USERNAME(self):
        return os.getenv("USERNAME")

    @property
    def PASSWORD(self):
        return os.getenv("PASSWORD")
    #USERNAME=os.getenv("USERNAME")
    #PASSWORD=os.getenv("PASSWORD")
    @property
    def MAIN_PAGE_URL(self):
        return os.getenv("MAIN_PAGE_URL")

CONFIG = EnvConfig