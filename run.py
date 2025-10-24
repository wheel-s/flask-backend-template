from app import create_app


lwapp = create_app()



if __name__  == "__main__":
    lwapp.run(debug=True)