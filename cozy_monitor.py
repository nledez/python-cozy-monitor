#!/usr/bin/env python

import re
import inspect
import subprocess


ANSI_ESCAPE = re.compile(r'\x1b[^m]*m')


def launch_command(command, parameter=''):
    result = ''
    if not isinstance(parameter, list):
        parameter = [parameter]

    for name in parameter:
        result += subprocess.Popen('cozy-monitor {} {}'.format(command, name),
                                   shell=True,
                                   stdout=subprocess.PIPE).stdout.read()
    return result


def stop(app_name):
    return launch_command(inspect.stack()[0][3], app_name)


def start(app_name):
    return launch_command(inspect.stack()[0][3], app_name)


def restart(app_name):
    return launch_command(inspect.stack()[0][3], app_name)


def update(app_name):
    return launch_command(inspect.stack()[0][3], app_name)


def uninstall(app_name):
    return launch_command(inspect.stack()[0][3], app_name)


def install(app_name):
    return launch_command(inspect.stack()[0][3], app_name)


def compact():
    return launch_command(inspect.stack()[0][3])


def views_list():
    return launch_command('views-list')


def compact_views(view):
    return launch_command('compact-views', view)


def compact_all_views():
    return launch_command('compact-all-views')


def status(app_name=None):
    apps = {}
    apps_status = subprocess.Popen('cozy-monitor status',
                                   shell=True,
                                   stdout=subprocess.PIPE).stdout.read()
    apps_status = apps_status.split('\n')

    for app_status in apps_status:
        if app_status:
            app_status = ANSI_ESCAPE.sub('', app_status).split(': ')
            apps[app_status[0]] = app_status[1]

    if app_name:
        return apps[app_name]
    else:
        return apps


def main():
    print status()
    # print stop('contacts')
    # print stop(['contacts', 'calendar'])
    # print status('contacts')
    # print start('contacts')
    # print start(['contacts', 'calendar'])
    # print status('contacts')
    # print status('calendar')
    # print uninstall('contacts')
    # print uninstall(['contacts', 'calendar'])
    # print install(['contacts', 'calendar'])
    # print compact()
    # print views_list()
    # print compact_all_views()

if __name__ == '__main__':
    main()
