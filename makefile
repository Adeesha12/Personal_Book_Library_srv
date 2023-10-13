clean:
	cd app ; \
	find /app -name "*__pycache__" -delete


run:
	cd app ; \
	uvicorn main:app --reload

Docker_run:
	docker compose build
	docker compose up