FROM postgres:17

# Copy maintenance scripts
COPY docker/dockerfiles/postgres/maintenance /usr/local/bin/maintenance
RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin && rmdir /usr/local/bin/maintenance
