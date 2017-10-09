import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


ARDUINO_VERSION = "1.8.5"


def test_arduino_download_directory(host):
    f = host.file('/opt/arduino')
    assert f.exists
    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'root'


def test_arduino_ide_tarball(host):
    f = host.file("/opt/arduino/arduino-{}-linux64.tar.xz".format(
                  ARDUINO_VERSION))
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'


def test_arduino_ide_directory(host):
    f = host.file("/opt/arduino/arduino-{}".format(ARDUINO_VERSION))
    assert f.exists
    assert f.is_directory
    assert f.user != "root"
    assert f.group != "root"
