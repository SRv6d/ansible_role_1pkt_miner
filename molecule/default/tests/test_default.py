import os
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_pkt_miner_systemd_service(host):
    pkt_miner_systemd_service = host.service("1pkt-miner")
    assert pkt_miner_systemd_service.is_enabled
    assert pkt_miner_systemd_service.is_running
