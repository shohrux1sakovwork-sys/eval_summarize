#!/usr/bin/env bash
# Берёт API_KEY (или DOC_API_KEY) из окружения docker-контейнера и пишет его в .env.
# Ключ не печатается. Использование (из корня проекта):
#   bash tools/get_api_key.sh [контейнер] [путь к .env]
set -euo pipefail
CONTAINER="${1:-}"
OUT="${2:-test_docs/db_test_kirimXat_500_4/.env}"

if [ -z "$CONTAINER" ]; then   # ищем контейнер по порту 8091, затем по имени
    CONTAINER="$(docker ps --filter publish=8091 --format '{{.Names}}' | head -1)"
    [ -z "$CONTAINER" ] && CONTAINER="$(docker ps --format '{{.Names}}' | grep -i summar | head -1 || true)"
    if [ -z "$CONTAINER" ]; then
        echo "Контейнер сервиса не найден. Запущенные контейнеры:"
        docker ps --format '{{.Names}}\t{{.Image}}\t{{.Ports}}'
        exit 1
    fi
    echo "Контейнер: $CONTAINER"
fi

# в контейнере ключ может называться DOC_API_KEY или API_KEY; run_eval.py ждёт DOC_API_KEY
LINE="$(docker inspect "$CONTAINER" --format '{{range .Config.Env}}{{println .}}{{end}}' \
    | grep -E '^(DOC_)?API_KEY=' | head -1 | sed -E 's/^(DOC_)?API_KEY=/DOC_API_KEY=/' || true)"
if [ -z "$LINE" ] || [ "$LINE" = "DOC_API_KEY=" ]; then
    echo "API_KEY / DOC_API_KEY не найден (или пуст) в контейнере $CONTAINER. Имена переменных:"
    docker inspect "$CONTAINER" --format '{{range .Config.Env}}{{println .}}{{end}}' | cut -d= -f1
    exit 1
fi
umask 077
printf '%s\n' "$LINE" > "$OUT"
# под root файл отдаём владельцу проекта, иначе run_eval.py не сможет его прочитать
[ "$(id -u)" = 0 ] && chown "$(stat -c %U:%G .)" "$OUT"
echo "OK: DOC_API_KEY записан в $OUT"
