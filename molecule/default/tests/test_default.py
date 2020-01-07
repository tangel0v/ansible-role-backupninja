import os
import testinfra.utils.ansible_runner
import datetime

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_backupninja_dump_exists(host):
    """Checking if the file generated in default test last step exists"""
    with host.sudo():
        bckdate = datetime.datetime.utcnow().strftime("%Y.%m.%d")
        bckpath = '/def_test/' + 'full-test' + '-' + bckdate + '.tgz'

        f = host.file(bckpath)
        assert f.exists
