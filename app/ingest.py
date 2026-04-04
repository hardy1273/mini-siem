from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

doc = {
    "event": "login_failed",
    "user": "alice",
    "ip": "192.168.1.10",
    "timestamp": "2026-04-04T10:01:22"
}

es.index(index="security-events", document=doc)

print("Inserted test event")