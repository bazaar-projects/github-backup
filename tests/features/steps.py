from lettuce import *
import os
import os.path
import subprocess
import sys
import tempfile

@step(u'an empty directory')
def empty_directory(step):
    world.directory = tempfile.mkdtemp()

@step(u'a subdirectory (\S+)')
def subdirectory(step, name):
    os.mkdir(os.path.join(world.directory, name))

@step(u'a local repository (\S+)')
def local_repository(step, name):
    directory = os.path.join(world.directory, name)
    os.mkdir(directory)
    cwd = os.getcwd()
    os.chdir(directory)
    subprocess.call(['git', 'init'],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    os.chdir(cwd)

@step(u'I back up (\w+)\'s repositories')
def back_up_repositories(step, user):
    script = os.path.join(os.path.dirname(__file__), '../../github_backup.py')
    subprocess.call([sys.executable, script, user, world.directory],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@step(u'there are (\d+) subdirectories')
def count_subdirectories(step, n):
    entries = os.listdir(world.directory)
    entries = map(lambda entry: os.path.join(world.directory, entry), entries)
    
    assert int(n) == len(entries), 'Got {0}'.format(len(entries))
    assert all(os.path.isdir(entry) for entry in entries), 'Got {0}'.format(entries)

@step('(\S+) is tracking (\S+)')
def check_tracking_repository(step, subdirectory, expected_url):
    cwd = os.getcwd()
    os.chdir(os.path.join(world.directory, subdirectory))
    # It's the same code as in github_backup.py. Probably a bad idea...
    process = subprocess.Popen(['git', 'config', 'remote.origin.url'],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors = process.communicate()
    url = output.decode('utf-8').strip()
    os.chdir(cwd)
    assert expected_url == url, 'Got {0}'.format(url)

@step('(\S+) is (|not )?a Git repository')
def check_not_git_repository(step, subdirectory, expected):
    cwd = os.getcwd()
    os.chdir(os.path.join(world.directory, subdirectory))
    result = subprocess.call(['git', 'status'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    os.chdir(cwd)
    assert (result == 0) == (expected == '')

@before.each_scenario
def setup(scenario):
    pass

@after.each_scenario
def teardown(scenario):
    world.directory = None
