run-db:
	docker run --name youtube_postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysuperpassword -e POSTGRES_DB=youtube -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres
	