
# 🌐 Mobproxy-analyzer-web

A Flask-based web interface for analyzing traffic logs captured by [MobSafe Proxy CLI](https://github.com/secwithripz/MobSafeSuite).

This tool reads `logs/traffic.json` and shows real-time alerts for:

- 🔑 Passwords in request bodies
- 🔐 API key leakage
- 📧 Email addresses
- 💳 Credit card numbers
- ⚠️ Insecure protocols

---

## 📦 Folder Structure
MobSafeWebApp/
├── app.py # Flask app
├── logs/ # Captured traffic logs (from mitmdump)
├── templates/
│ └── index.html # Web UI

Built with ❤️ by Rifnas Mohd

