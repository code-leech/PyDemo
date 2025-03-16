# window.py
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

from gi.repository import Adw, Gtk, GLib
from .themer import PydemoThemer

@Gtk.Template(resource_path='/code/leech/pydemo/window.ui')
class PydemoWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'PydemoWindow'

    menubtn = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menubtn.get_popover().add_child(PydemoThemer(), "themer")

    def button_reset(self, button):
        button.set_label("Click me!")
        button.set_css_classes(["suggested-action", "pill", "title-3"])
        button.set_sensitive(True)

    @Gtk.Template.Callback()
    def button_cb(self, button):
        button.set_sensitive(False)
        button.set_label("Thanks!")
        button.set_css_classes(["destructive-action", "pill", "title-3"])
        GLib.timeout_add_seconds(2, self.button_reset, button)

