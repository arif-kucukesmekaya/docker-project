#!/bin/bash

LOG_FILE="/home/arif/docker-project/logs/app.log"
ARCHIVE_DIR="/home/arif/docker-project/log_archive"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

mkdir -p "$ARCHIVE_DIR"

if [ -f "$LOG_FILE" ]; then
    ARCHIVE_FILE="$ARCHIVE_DIR/app_${TIMESTAMP}.log"
    cp "$LOG_FILE" "$ARCHIVE_FILE"
    echo "$(date): Log dosyası arşivlendi: $ARCHIVE_FILE" >> "$ARCHIVE_DIR/archive.log"
fi
r
docker exec myapp_postgres pg_dump -U postgres mydb > "$ARCHIVE_DIR/db_backup_${TIMESTAMP}.sql" 2>/dev/null

if [ $? -eq 0 ]; then
    echo "$(date): Veritabanı yedeği alındı: db_backup_${TIMESTAMP}.sql" >> "$ARCHIVE_DIR/archive.log"
fi

find "$ARCHIVE_DIR" -name "*.log" -mtime +30 -delete
find "$ARCHIVE_DIR" -name "*.sql" -mtime +30 -delete

