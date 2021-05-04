FROM postgres
WORKDIR /docker-entrypoint-initdb.d
ADD create_tables.sql /docker-entrypoint-initdb.d
EXPOSE 5432