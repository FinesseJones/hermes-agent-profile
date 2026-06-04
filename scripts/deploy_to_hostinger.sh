#!/bin/bash
# deploy_to_hostinger.sh - Automates migration of Hermes Core Runtime to Hostinger VPS

set -e

VPS_HOST="srv1726890.hstgr.cloud"
VPS_USER="root"
VPS_DIR="/docker/hermes-agent-ttiy/data"
LOCAL_HERMES="$HOME/.hermes"
TEMP_ZIP="/tmp/hermes_runtime.zip"

echo "=== [1/5] Packaging Local Hermes Core Runtime ==="
# Clean old zip if exists
rm -f "$TEMP_ZIP"

# Zip ~/.hermes excluding massive folders (logs, sessions, cache, .git, profiles, node, hermes-agent, bin)
cd "$LOCAL_HERMES"
zip -q -y -r "$TEMP_ZIP" . \
  -x "*/sessions/*" \
  -x "*/logs/*" \
  -x "*/audio_cache/*" \
  -x "*/image_cache/*" \
  -x "*/sandboxes/*" \
  -x "backups/*" \
  -x "migration/*" \
  -x ".git/*" \
  -x "profiles/*" \
  -x "node/*" \
  -x "hermes-agent/*" \
  -x "bin/*" \
  -x "state-snapshots/*" \
  -x "bootstrap-cache/*" \
  -x "*.DS_Store" \
  -x "*.zip"

echo "Zip package created at $TEMP_ZIP ($(du -sh $TEMP_ZIP | cut -f1))"

echo "=== [2/5] Uploading Runtime Package to Hostinger VPS ==="
scp "$TEMP_ZIP" "$VPS_USER@$VPS_HOST:/tmp/hermes_runtime.zip"

echo "=== [3/5] Extracting Runtime on VPS ==="
ssh "$VPS_USER@$VPS_HOST" "
  set -e
  # Backup existing data folder
  echo 'Backing up existing VPS config...'
  mkdir -p /tmp/hermes_backup
  cp -p $VPS_DIR/cli-config.yaml /tmp/hermes_backup/ 2>/dev/null || true
  cp -p $VPS_DIR/.env /tmp/hermes_backup/ 2>/dev/null || true

  # Extract zip
  echo 'Extracting files into $VPS_DIR...'
  unzip -o -q /tmp/hermes_runtime.zip -d $VPS_DIR

  # Restore backup config files if they existed on the server
  if [ -f /tmp/hermes_backup/cli-config.yaml ]; then
    echo 'Restoring original VPS cli-config.yaml...'
    cp /tmp/hermes_backup/cli-config.yaml $VPS_DIR/
  fi
  if [ -f /tmp/hermes_backup/.env ]; then
    echo 'Restoring original VPS .env...'
    cp /tmp/hermes_backup/.env $VPS_DIR/
  fi

  # Fix permissions for the hermes user (UID 10000)
  echo 'Adjusting permissions to UID 10000...'
  chown -R 10000:10000 $VPS_DIR

  # Cleanup temporary files
  rm -f /tmp/hermes_runtime.zip
  rm -rf /tmp/hermes_backup
"

echo "=== [4/5] Restarting Hermes Agent Container on VPS ==="
ssh "$VPS_USER@$VPS_HOST" "
  cd /docker/hermes-agent-ttiy && docker compose restart hermes-agent
"

echo "=== [5/5] Verifying Deployment Status ==="
ssh "$VPS_USER@$VPS_HOST" "
  echo '=== Docker Containers ==='
  docker compose -f /docker/hermes-agent-ttiy/docker-compose.yml ps
  echo ''
  echo '=== Container Logs (last 15 lines) ==='
  docker compose -f /docker/hermes-agent-ttiy/docker-compose.yml logs --tail=15 hermes-agent
"

echo "=== Migration Successfully Completed! ==="
