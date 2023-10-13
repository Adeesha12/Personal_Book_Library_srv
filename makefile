clean:
	cd app ; \
	find /app -name "*__pycache__" -delete

# development run
run:
	cd app ; \
	uvicorn main:app --reload

# final product run
Docker_run:
	docker compose build
	docker compose up

Docker_rerun:
	docker compose up

Docker_remove:
	docker compose down
	docker rmi personal_book_library_srv-app
