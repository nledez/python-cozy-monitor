#!/usr/bin/python

import os
import mock
import unittest

import cozy_monitor

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


class PopenMock(object):
    def __init__(self, command):
        file_path = '{}/cozy-monitor-outputs/cozy-monitor-{}.txt'
        self.stdout = open(file_path.format(CURRENT_PATH, command))


class CozyMonitor(unittest.TestCase):
    '''
    The cozy_monitor test case.
    '''

    @mock.patch('cozy_monitor.subprocess')
    def testCanGetStatus(self, mock_subprocess):
        '''
        Cozy monitor status can parsed
        '''
        expected = {
            'index': 'up',
            'databrowser': 'up',
            'contacts': 'up',
            'sync': 'up',
            'photos': 'up',
            'couch': 'up',
            'data-system': 'up',
            'controller': 'up',
            'leave-google': 'up',
            'proxy': 'up',
            'home': 'up',
            'calendar': 'stopped',
            'mta': 'up',
            'emails': 'up',
            'files': 'up',
            'kresus': 'up',
        }

        mock_subprocess.Popen.return_value = PopenMock('status')
        full_out = cozy_monitor.status()
        self.assertIsInstance(full_out, dict)
        self.assertEqual(full_out, expected)

        mock_subprocess.Popen.return_value = PopenMock('status')
        app_up = cozy_monitor.status('files')
        self.assertIsInstance(app_up, str)
        self.assertEqual(app_up, 'up')

        mock_subprocess.Popen.return_value = PopenMock('status')
        app_stopped = cozy_monitor.status('calendar')
        self.assertIsInstance(app_stopped, str)
        self.assertEqual(app_stopped, 'stopped')

    @mock.patch('cozy_monitor.subprocess')
    def testCanStartAnApp(self, mock_subprocess):
        '''
        Cozy monitor can start an app
        '''
        expected = PopenMock('start').stdout.read()
        mock_subprocess.Popen.return_value = PopenMock('start')
        start_out = cozy_monitor.start('calendar')
        self.assertIsInstance(start_out, str)
        self.assertEqual(start_out, expected)

    @mock.patch('cozy_monitor.subprocess')
    def testCanStopAnApp(self, mock_subprocess):
        '''
        Cozy monitor can stop an app
        '''
        expected = PopenMock('stop').stdout.read()
        mock_subprocess.Popen.return_value = PopenMock('stop')
        stop_out = cozy_monitor.stop('calendar')
        self.assertIsInstance(stop_out, str)
        self.assertEqual(stop_out, expected)

    @mock.patch('cozy_monitor.subprocess')
    def testCanRestartAnApp(self, mock_subprocess):
        '''
        Cozy monitor can restart an app
        '''
        expected = PopenMock('restart').stdout.read()
        mock_subprocess.Popen.return_value = PopenMock('restart')
        restart_out = cozy_monitor.restart('calendar')
        self.assertIsInstance(restart_out, str)
        self.assertEqual(restart_out, expected)

    @mock.patch('cozy_monitor.subprocess')
    def testCanUpdateAnApp(self, mock_subprocess):
        '''
        Cozy monitor can update an app
        '''
        expected = PopenMock('update').stdout.read()
        mock_subprocess.Popen.return_value = PopenMock('update')
        update_out = cozy_monitor.update('calendar')
        self.assertIsInstance(update_out, str)
        self.assertEqual(update_out, expected)

    @mock.patch('cozy_monitor.subprocess')
    def testCanUninstallAnApp(self, mock_subprocess):
        '''
        Cozy monitor can uninstall an app
        '''
        expected = PopenMock('uninstall').stdout.read()
        mock_subprocess.Popen.return_value = PopenMock('uninstall')
        uninstall_out = cozy_monitor.uninstall('calendar')
        self.assertIsInstance(uninstall_out, str)
        self.assertEqual(uninstall_out, expected)

    @mock.patch('cozy_monitor.subprocess')
    def testCanInstallAnApp(self, mock_subprocess):
        '''
        Cozy monitor can install an app
        '''
        expected = PopenMock('install').stdout.read()
        mock_subprocess.Popen.return_value = PopenMock('install')
        install_out = cozy_monitor.install('calendar')
        self.assertIsInstance(install_out, str)
        self.assertEqual(install_out, expected)

    @mock.patch('cozy_monitor.subprocess')
    def testCanCompactAnApp(self, mock_subprocess):
        '''
        Cozy monitor can compact an app
        '''
        expected = PopenMock('compact').stdout.read()
        mock_subprocess.Popen.return_value = PopenMock('compact')
        compact_out = cozy_monitor.compact()
        self.assertIsInstance(compact_out, str)
        self.assertEqual(compact_out, expected)

    @mock.patch('cozy_monitor.subprocess')
    def testCanCompactAllViewsAnApp(self, mock_subprocess):
        '''
        Cozy monitor can compact-all-views an app
        '''
        expected = PopenMock('compact-all-views').stdout.read()
        mock_subprocess.Popen.return_value = PopenMock('compact-all-views')
        compact_all_views_out = cozy_monitor.compact_all_views()
        self.assertIsInstance(compact_all_views_out, str)
        self.assertEqual(compact_all_views_out, expected)

    @mock.patch('cozy_monitor.subprocess')
    def testCanViewsListAnApp(self, mock_subprocess):
        '''
        Cozy monitor can views-list an app
        '''
        expected = PopenMock('views-list').stdout.read()
        mock_subprocess.Popen.return_value = PopenMock('views-list')
        views_list_out = cozy_monitor.views_list()
        self.assertIsInstance(views_list_out, str)
        self.assertEqual(views_list_out, expected)
