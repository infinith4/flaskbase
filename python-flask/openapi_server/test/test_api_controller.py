# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestApiController(BaseTestCase):
    """ApiController integration test stubs"""

    def test_api_tx(self):
        """Test case for api_tx

        get transaction
        """
        headers = { 
            'Accept': 'text/plain',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/api/tx/{txid}'.format(txid='txid_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
