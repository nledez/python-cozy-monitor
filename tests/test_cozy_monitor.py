#!/usr/bin/python

import os
import mock
import unittest

import cozy_monitor

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


class PopenMock(object):
    def __init__(self, text):
        self.stdout = open('{}/cozy-monitor-outputs/{}'.format(CURRENT_PATH,
                                                               text))


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
        mock_subprocess.Popen.return_value = PopenMock('cozy-monitor-status.txt')

        full_out = cozy_monitor.status()
        self.assertIsInstance(full_out, dict)
        self.assertEqual(full_out, expected)

        mock_subprocess.Popen.return_value = PopenMock('cozy-monitor-status.txt')
        app_up = cozy_monitor.status('files')
        self.assertIsInstance(app_up, str)
        self.assertEqual(app_up, 'up')

        mock_subprocess.Popen.return_value = PopenMock('cozy-monitor-status.txt')
        app_stopped = cozy_monitor.status('calendar')
        self.assertIsInstance(app_stopped, str)
        self.assertEqual(app_stopped, 'stopped')
