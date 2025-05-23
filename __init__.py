# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AsbuiltInspector
                                 A QGIS plugin
 an efficient tool for Unifiber
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-04-30
        copyright            : (C) 2025 by Jacops
        email                : toon.vandevoorde@jacops.be
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load AsbuiltInspector class from file AsbuiltInspector.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .LayerInspector import AsbuiltInspector

    return AsbuiltInspector(iface)
