# __init__.py
#
# Copyright 2025 Carbon751
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw, Gdk, Gio

css_provider = Gtk.CssProvider()
css_provider.load_from_resource('/code/leech/pydemo/style.css')
Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

settings = Gio.Settings.new('code.leech.pydemo')

# Get the default AdwStyleManager instance
style_manager = Adw.StyleManager.get_default()

# Function to update the style manager based on the GSettings value
def update_theme(settings, key, user_data):
    theme_pref = settings.get_string('theme-preference')
    if theme_pref == 'default':
        style_manager.set_color_scheme(Adw.ColorScheme.DEFAULT)
    elif theme_pref == 'light':
        style_manager.set_color_scheme(Adw.ColorScheme.FORCE_LIGHT)
    elif theme_pref == 'dark':
        style_manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK)

# Connect the 'changed' signal to update the theme when the setting changes
settings.connect('changed::theme-preference', update_theme, None)

# Apply the initial theme setting
update_theme(settings, 'theme-preference', None)
