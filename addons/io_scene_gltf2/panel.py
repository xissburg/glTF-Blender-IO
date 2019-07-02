# Copyright 2018-2019 The glTF-Blender-IO authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import bpy

class PANEL_PT_gltf(bpy.types.Panel):
    bl_label = 'glTF'
    bl_idname = 'PANEL_PT_gltf'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'object'

    @classmethod
    def poll(cls, context):
        return context.object is not None and context.object.type == 'MESH'

    def draw(self, context):
        return


class PANEL_PT_gltf_lod(bpy.types.Panel):
    bl_label = 'Levels of Detail'
    bl_idname = 'PANEL_PT_gltf_lod'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'object'
    bl_parent_id = 'PANEL_PT_gltf'

    @classmethod
    def poll(cls, context):
        return context.object is not None and context.object.type == 'MESH'

    def draw(self, context):
        obj = context.object
        col = self.layout.column(align=True)

        if obj.glTF_LOD_parent_object is not None:
            lod = 0
            for entry in obj.glTF_LOD_parent_object.glTF_LOD.entries:
                if entry.child_object == obj:
                    lod = entry.lod
                    break
            col.label(text="Object is part of a LOD chain (LOD {}).".format(lod))
            row = col.row(align=True)
            op = row.operator('object.select_parent_lod', text="Select root LOD object ({})".format(obj.glTF_LOD_parent_object.name))
        elif len(obj.glTF_LOD.entries) == 0:
            row = col.row(align=True)
            row.operator('object.add_lod')
        else:
            box = col.box()
            row = box.row(align=True)
            row.label(text="LOD 0:")
            row = box.row(align=True)
            row.prop(obj.glTF_LOD, 'screen_coverage_lod_0')
            for index, entry in enumerate(obj.glTF_LOD.entries):
                box = col.box()
                row = box.row(align=True)
                row.label(text="LOD {}:".format(entry.lod))
                row = box.row(align=True)
                row.prop(entry, 'child_object', text='')
                op = row.operator('object.delete_lod', text='', icon='REMOVE')
                op.entry_index = index
                row = box.row(align=True)
                row.prop(entry, 'screen_coverage')
            row = col.row(align=True)
            row.operator('object.add_lod')