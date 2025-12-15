# DNS
## Notes
### Local DNS records
- <https://discourse.pi-hole.net/t/howto-using-pi-hole-as-lan-dns-server/533>
- <https://docs.pi-hole.net/main/faq/?h=local+dns+records#in-which-order-are-locally-defined-dns-records-used>
- Spin up pihole
- Login to the web browser
- Settings --> Local DNS records

### Basic usage
- Pihole works when you
- `sudo systemctl disable systemd-resolved.service`
- `sudo systemctl stop systemd-resolved.service`
- Then, in the pihole directory
- `sudo docker compose up`

## TODO
- [ ] Don't look up domains with `.local` TLD
- [ ] Move DNS configs into a version controlled file in this repo
  - Use thru docker bind mounts
