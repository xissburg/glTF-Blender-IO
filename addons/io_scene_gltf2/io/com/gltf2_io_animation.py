"""
 * ***** BEGIN GPL LICENSE BLOCK *****
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 * Contributor(s): Julien Duroure.
 *
 * ***** END GPL LICENSE BLOCK *****
 * This development is done in strong collaboration with Airbus Defence & Space
 """

from .gltf2_io_animation_channel import *
from .gltf2_io_animation_data import *

class PyAnimation():
    def __init__(self, index, json, gltf):
        self.index = index
        self.json  = json # Animation json
        self.gltf  = gltf # Reference to global glTF instance

        # glTF2.0 required properties
        self.channels_ = [] #TODO to be rename, already an attribute with this name in my code
        self.samplers = []

        # glTF2.0 not required properties
        self.name  = None
        self.extensions = {}
        self.extras = {}

        # Animation specific
        self.channels = []