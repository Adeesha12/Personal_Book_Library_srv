# Run application 

step 01 <br>
Clone the project and pull latest changes 

### <span style="color:skyblue"> Docker run </span>
Step 02 <br>
Run application using docker   
```bash
# below command will build and run the app using docker containers
make docker_run

#use this command to to just run the docker container if container stop after build and run 
make docker_rerun

# after runnning use this command to stop containers remove image
make docker_remove 
```

### <span style="color:lightyellow"> Development run </span>

step 02 <br>
create virtualenv and activate from your favorite packaging tool <br>
ex:-
```bash
# create env from virtualenv packaging tool
virtualenv env
# activate env
source env/bin/activate
```
step 03 <br>
Create Database for app and enter credential and Db info on .env file under  DB_password, DB_username <br>
<b style="color:skyblue">If use Docker PSQL use below command</b><br>
** remove DB_HOST from .env 
```bash
# replace the sample password and username and name of the contianer for your requirement
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres
```


step 04 <br>
maviagte to Personal_Book_Library_srv/app and run the application
```bash
uvicorn main:app --reload
```