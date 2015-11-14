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
