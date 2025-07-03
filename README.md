# AsbuiltInspector QGIS Plugin

## Overview
AsbuiltInspector is a QGIS plugin for efficient inspection and summarization of geospatial layers, tailored for Unifiber and similar fiber infrastructure projects. It integrates with the QGIS interface, providing custom tools for feature analysis.

---

## Class and Method Reference

### 1. AsbuiltInspector (LayerInspector.py)
Main plugin class, manages QGIS integration, menu/toolbar actions, and plugin state.

**Methods:**
- `__init__(iface)`: Initializes plugin, sets up localization, menu, and actions.
- `tr(message)`: Returns translated UI string.
- `add_action(icon_path, text, callback, ...)`: Adds a toolbar/menu action to QGIS.
- `initGui()`: Sets up plugin GUI elements (toolbar/menu icons).
- `unload()`: Removes plugin actions from QGIS.
- `run()`: Activates/deactivates the plugin's main tool and dialog.

---

### 2. FeatureSummarizer (LayerInspector_dialog.py)
Utility class for analyzing and summarizing features in QGIS layers.

**Class Variables:**
- `CROSSING_PREFIXES`, `TRENCHING_PREFIXES`: Field name prefixes for feature types.
- `TYPE_MAPPING`: Maps table names to feature types.

**Methods:**
- `parse_db_and_table(layer)`: Extracts database and table names from a layer's data source URI.
- `determine_group_key(feature, layer)`: Determines a grouping key for a feature based on database and project.
- `accumulate_length(features, prefixes)`: Sums feature lengths for fields with specified prefixes.
- `render_length_summary(field_total, feature_count, header)`: Renders a summary of lengths and counts as HTML and text.
- `summarize_crossings(features, group_name)`: Summarizes crossing features.
- `summarize_trenching(features, group_name)`: Summarizes trenching features.
- `summarize_accesspoints(features)`: Summarizes access point materials.
- `generate_summary(found)`: Groups features by database/type and generates a full summary (HTML/text).

---

### 3. AsbuiltInspectorDialog (LayerInspector_dialog.py)
Handles the plugin's interactive dialog and map tool for feature selection.

**Methods:**
- `__init__(iface, parent=None)`: Initializes the dialog, sets up map tool and rubber band for polygon drawing.
- `canvasPressEvent(event)`: Handles mouse events for drawing polygons on the map.
- `finish()`: Completes the polygon, identifies intersecting features, and shows the summary dialog.
- `identifyFeatures(geometry)`: Finds and highlights features in all vector layers that intersect the drawn polygon.
- `save_text_browser_as_png()`: Saves the dialog's text browser content as a PNG image.

---

## Usage
- Enable the plugin in QGIS.
- Use the toolbar/menu action to activate the tool.
- Draw a polygon on the map to select features.
- The plugin will summarize and display information about the selected features.

---

## Development
- Main logic: `LayerInspector.py`
- Dialog/UI: `LayerInspector_dialog.py`, `LayerInspector_dialog_base.ui`
- Resources: `resources.py`, icons, translations in `i18n/`

---

## License
GNU General Public License v2 or later.

## Authors
Jacops (2025)  
Contact: toon.vandevoorde@jacops.be

---
