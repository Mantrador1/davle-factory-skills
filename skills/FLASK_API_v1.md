Flask API Development
Purpose
Maintain Control Panel Flask app at /opt/factory/apps/panel_mvp/
File Structure
panel_mvp/
├── panel_mvp.py (main app)
├── static/ (CSS/JS/screenshots)
└── templates/ (if needed)
Common Patterns
# Sanitize input
def sanitize_order_id(order_id):
    if not re.match(r'^WF_[A-Z0-9_]+$', order_id):
        return None
    return order_id

# Serve files
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('/opt/factory/panel/static', path)

# API endpoint
@app.route('/api/endpoint', methods=['POST'])
def api_endpoint():
    data = request.get_json()
    return jsonify({"status": "ok"})
Testing
curl -X POST http://localhost:5000/api/decision \
  -H 'Content-Type: application/json' \
  -d '{"orderId": "WF_TEST", "decision": "ACCEPT"}'
Deployment
Edit /opt/factory/apps/panel_mvp/panel_mvp.py
Test syntax: python3 -m py_compile panel_mvp.py
Restart: sudo systemctl restart factory-panel-mvp
Check logs: sudo journalctl -u factory-panel-mvp -n 20
