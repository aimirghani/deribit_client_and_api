import typer
from database.create_db import init_db
from dotenv import find_dotenv, load_dotenv, set_key
from deribit_client import run_deribit_client
from os import system, getenv, environ

app = typer.Typer()

envfile = find_dotenv()
load_dotenv(envfile)


@app.command()
def createdb():
    db_created = int(getenv("DB_CREATED"))
    if not db_created:
        init_db()
        environ["DB_CREATED"] = str(1)
        set_key(envfile, "DB_CREATED", environ["DB_CREATED"])
        print("A DataBase has been created.")
    else:
        print("There exist a DataBase already.")


@app.command()
def call_deribit():
    run_deribit_client()


@app.command()
def run_api():
    system("uvicorn api_app:app --reload")


if __name__ == "__main__":
    app()
