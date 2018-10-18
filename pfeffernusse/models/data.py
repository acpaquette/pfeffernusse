# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from pfeffernusse.models.base_model_ import Model
from pfeffernusse import util


class Data(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, data: List[object]=None):  # noqa: E501
        """Data - a model defined in Swagger

        :param count: The count of this Data.  # noqa: E501
        :type count: int
        :param data: The data of this Data.  # noqa: E501
        :type data: List[object]
        """
        self.swagger_types = {
            'count': int,
            'data': List[object]
        }

        self.attribute_map = {
            'count': 'count',
            'data': 'data'
        }

        self._count = count
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'Data':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The data of this Data.  # noqa: E501
        :rtype: Data
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self) -> int:
        """Gets the count of this Data.


        :return: The count of this Data.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int):
        """Sets the count of this Data.


        :param count: The count of this Data.
        :type count: int
        """

        self._count = count

    @property
    def data(self) -> List[object]:
        """Gets the data of this Data.


        :return: The data of this Data.
        :rtype: List[object]
        """
        return self._data

    @data.setter
    def data(self, data: List[object]):
        """Sets the data of this Data.


        :param data: The data of this Data.
        :type data: List[object]
        """

        self._data = data