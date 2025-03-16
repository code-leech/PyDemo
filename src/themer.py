# themer.py
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

from gi.repository import Adw, Gtk, Gio

@Gtk.Template(resource_path='/code/leech/pydemo/themer.ui')
class PydemoThemer(Gtk.Box):
    __gtype_name__ = 'PydemoThemer'

    follow = Gtk.Template.Child()
    light = Gtk.Template.Child()
    dark = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Initialize GSettings
        self.settings = Gio.Settings.new('code.leech.pydemo')

        # Map checkbuttons to theme preference values
        self.theme_map = {
            self.follow: 'default',
            self.light: 'light',
            self.dark: 'dark'
        }

        # Connect toggled signals for user interaction
        self.follow.connect('toggled', self.on_theme_toggled)
        self.light.connect('toggled', self.on_theme_toggled)
        self.dark.connect('toggled', self.on_theme_toggled)

        # Connect to GSettings 'changed' signal for external updates
        self.settings.connect('changed::theme-preference', self.on_theme_changed)

        # Set initial state based on current GSettings value
        self.on_theme_changed(self.settings, 'theme-preference')

    def on_theme_toggled(self, button):
        """Callback when a checkbutton is toggled by the user."""
        if button.get_active():
            value = self.theme_map[button]
            self.settings.set_string('theme-preference', value)

    def on_theme_changed(self, settings, key):
        """Callback when the GSettings 'theme-preference' key changes."""
        value = settings.get_string(key)
        if value == 'default':
            self.follow.set_active(True)
        elif value == 'light':
            self.light.set_active(True)
        elif value == 'dark':
            self.dark.set_active(True)

