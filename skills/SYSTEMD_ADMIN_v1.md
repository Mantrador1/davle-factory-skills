# SYSTEMD Service Administration

## Purpose
Manage factory systemd services: restart, check status, view logs, fix crashes.

## Services
- factory-panel-mvp (Flask UI on port 5000)
- factory-ideogram-runner (Ideogram API worker)
- factory-brain-bridge (OpenAI orchestrator)

## Sudo Access
Password stored: `/opt/factory/secrets/deploy_sudo_password`

## Commands
```bash
# Restart service
cat /opt/factory/secrets/deploy_sudo_password | sudo -S systemctl restart SERVICE

# Check status
sudo systemctl status SERVICE --no-pager

# View logs (last 50 lines)
sudo journalctl -u SERVICE -n 50 --no-pager

# Enable service
sudo systemctl enable SERVICE
Common Fixes
IndentationError: Python file broken → fix with proper tabs
Permission denied: sudo chown deploy:deploy FILE
Port in use: sudo lsof -i :5000 → kill process
Crash loop: Check logs for error, fix code, restart
Evidence
Always save service status to evidence directory after fixes.
