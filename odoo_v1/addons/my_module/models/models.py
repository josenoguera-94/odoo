# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import logging

_logger = logging.getLogger(__name__)

class my_module(models.Model):
    _name = 'my_module.my_module'
    _description = 'my_module.my_module'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.model
    def create(self, vals):
        record = super(my_module, self).create(vals)
        _logger.info('Record created:')
        try:
            self._post_to_endpoint(record)
        except Exception as e:
            # record.unlink()
            _logger.info('Failed to post data to endpoint %s', e)
        return record

    def write(self, vals):
        result = super(my_module, self).write(vals)
        _logger.info('Record updated:')
        for record in self:
            try:
                self._post_to_endpoint(record)
            except Exception as e:
                _logger.info('Failed to post data to endpoint %s', e)

        return result

    def _post_to_endpoint(self, record):
        url = 'http://172.26.0.1:5000/post'
        data = {
            'name': record.name,
            'value': record.value,
            'value2': record.value2,
            'description': record.description,
        }
        headers = {'Content-Type': 'application/json'}
        _logger.info('Data to post:')
        _logger.info(data)
        response = requests.post(url, json=data, headers=headers)
        if response.status_code != 200:
            raise Exception('Failed to post data to endpoint')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
