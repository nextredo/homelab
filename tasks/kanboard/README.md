# KanBoard
## Docker Compose
```bash
wget https://github.com/kanboard/kanboard/raw/refs/heads/main/docker-compose.sqlite.yml
```

## Raw docker run
```
docker run -d --name kanboard -p 80:80 -t kanboard/kanboard:latest
```
