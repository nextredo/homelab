# Immich
## Using This Config
- Follow the [quickstart instructions][quickstart] to get the necessary files

### `.env`
```
TZ=Australia/Melbourne
```

### Post Setup
- `http://<machine-ip-address>:2283`


### Mobile App
- Available from many different sources
- I've just got it through the Google Play store

## TODOs
- [ ] Finish install, basic test on laptop
- [ ] Install on homelab
- [ ] Use a [`config.json`][json-config] instead of configuring it in the GUI
- [ ] Customise `docker-compose.yml`
- [ ] Add a [backup for database & photos][backup-script]
  - I was thinking just cron & rsync
  - But Borg sounds pretty good too

<!-- Links -->
[quickstart]: https://docs.immich.app/overview/quick-start/
[json-config]: https://docs.immich.app/install/config-file
[backup-script]: https://docs.immich.app/guides/template-backup-script/
