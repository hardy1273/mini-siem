from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch("http://localhost:9200")

doc = {
    "event": "login_failed",
    "user": "alice",
    "ip": "192.168.1.10",
    "timestamp": datetime.utcnow().isoformat()
}

es.index(index="security-events", document=doc)

print("Inserted test event")