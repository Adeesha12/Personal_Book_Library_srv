clean:
	cd app ; \
	py3clean .

# development run
run:
	cd app ; \
	uvicorn main:app --reload

# final product run
docker_run: clean
	docker compose build
	docker compose up

docker_rerun:
	docker compose up

docker_remove:
	docker compose down
	docker rmi personal_book_library_srv-app
