# ansible_role_1pkt_miner

This role will install and configure a 1PKT miner.

## Role Variables

| Variable                         | Required | Default                                     | Choices                                                                    | Comments                             |
| -------------------------------- | -------- | ------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------ |
| pkt_miner_git_repository_url     | no       | https://github.com/cjdelisle/packetcrypt_rs | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | URL to Git repository of 1PKT miner. |
| pkt_miner_git_repository_version | no       | HEAD                                        | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Git repository version.              |
| pkt_miner_service_name           | no       | 1pkt-miner                                  | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Name of the PKT service.             |
| pkt_miner_wallet_address         | **yes**  | undefined                                   | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | PKT address to send rewards to.      |
| pkt_miner_pools                  | **yes**  | undefined                                   | [list](https://developers.google.com/protocol-buffers/docs/proto#scalar)   | List of pools to mine to.            |

## Example Playbook

```yaml
- hosts: 1pkt_miners
  roles:
    - ansible_role_1pkt_miner
  vars:
    1pkt_miner_pools:
      - 1pktpool.acme.com
```

## License

BSD

## Author Information

Marvin Vogt (srv6d@initq.io)
