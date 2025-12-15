# Nextcloud ➡️☁️
- [Nextcloud AIO GitHub & README][aio]

## Setup
```bash
# Initialise the submodule
git submodule init
git submodule update

# Get new changes from upstream, merge them in if possible
git submodule update --remote --merge

# Run the container
sudo docker compose up -d
```

## Links
- [Upgrading](./all-in-one/readme.md#how-to-update-the-containers)
- [Reverse Proxy Use](./all-in-one/readme.md/reverse-proxy.md)
- [Syncing Backups](./all-in-one/readme.md#sync-local-backups-regularly-to-another-drive)

<!-- Links -->
[aio]: https://github.com/nextcloud/all-in-one
