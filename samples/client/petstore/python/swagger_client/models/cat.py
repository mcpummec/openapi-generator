# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class Cat(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Cat - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'class_name': 'str',
            'color': 'str',
            'declawed': 'bool'
        }

        self.attribute_map = {
            'class_name': 'className',
            'color': 'color',
            'declawed': 'declawed'
        }

        self._class_name = None
        self._color = 'red'
        self._declawed = None

    @property
    def class_name(self):
        """
        Gets the class_name of this Cat.


        :return: The class_name of this Cat.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """
        Sets the class_name of this Cat.


        :param class_name: The class_name of this Cat.
        :type: str
        """
        
        self._class_name = class_name

    @property
    def color(self):
        """
        Gets the color of this Cat.


        :return: The color of this Cat.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this Cat.


        :param color: The color of this Cat.
        :type: str
        """
        
        self._color = color

    @property
    def declawed(self):
        """
        Gets the declawed of this Cat.


        :return: The declawed of this Cat.
        :rtype: bool
        """
        return self._declawed

    @declawed.setter
    def declawed(self, declawed):
        """
        Sets the declawed of this Cat.


        :param declawed: The declawed of this Cat.
        :type: bool
        """
        
        self._declawed = declawed

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

