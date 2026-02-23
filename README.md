# BCFM Case

Basit bir Flask API case projesi.

## Endpointler

- `GET /` -> `{"msg":"BCFM"}`
- `GET /health` -> `{"status":"healthy"}`
- `POST /post` -> Body'den gelen `key` ve `value` alanlarini geri doner

## Goruntuler

### `/` Endpoint

![Home endpoint](assets/images/home-endpoint.svg)

### `/health` Endpoint

![Health endpoint](assets/images/health-endpoint.svg)

## Lokal Calistirma

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Uygulama varsayilan olarak `8093` portunda calisir.

## Docker

```bash
docker compose up -d --build
```

## Test Ornekleri

```bash
curl http://localhost:8093/
curl http://localhost:8093/health
curl -X POST http://localhost:8093/post \
  -H "Content-Type: application/json" \
  -d '{"key":"a","value":"b"}'
```
