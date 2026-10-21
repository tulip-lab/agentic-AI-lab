#!/bin/sh
# Run in your private flowise-lab folder, after copying the starter files.
set -eu

if [ -e .env ]; then
    printf '%s\n' '.env already exists; keeping your existing secrets.' >&2
    exit 1
fi
command -v openssl >/dev/null 2>&1 || {
    printf '%s\n' 'Install OpenSSL or use a terminal that provides it, then retry.' >&2
    exit 1
}
test -f runtime.env.example || {
    printf '%s\n' 'Copy runtime.env.example into this folder first.' >&2
    exit 1
}

umask 077
temp_env=$(mktemp .env.XXXXXX)
trap 'rm -f "$temp_env"' EXIT HUP INT TERM
cat runtime.env.example > "$temp_env"
printf '\n' >> "$temp_env"
for secret_name in JWT_AUTH_TOKEN_SECRET JWT_REFRESH_TOKEN_SECRET EXPRESS_SESSION_SECRET TOKEN_HASH_SECRET; do
    secret_value=$(openssl rand -hex 32)
    printf '%s=%s\n' "$secret_name" "$secret_value" >> "$temp_env"
done
# Refuse replacement even if another process created .env while generating keys.
ln "$temp_env" .env
printf '%s\n' 'Created private .env; no secret values were printed. Keep it out of submissions.'
