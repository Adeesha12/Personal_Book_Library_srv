step 01
Clone the project 

## Docker run
Step 02
run application using docker   
```bash
# below command will build and run the app using docker containers
make Docker_run

#use this command to to just run the docker container if container stop after build and run 
make Docker_rerun

# after runnning use this command to stop containers remove image
make Docker_remove 
```

## Development run 

step 02 <br>
create virtualenv and activate from your favorite packaging tool 
ex:-
```bash
# create env from virtualenv packaging tool
virtualenv env
# activate env
source env/bin/activate
```
step 03 <br>
create db for app and enter data on .env file under  DB_password, DB_username
if use Docker PSQL use this command
```bash
# replace the sample password and username and name of the contianer for your requirement
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres
```


step 04 <br>
maviagte to Personal_Book_Library_srv/app and run the application
```bash
uvicorn main:app --reload
```