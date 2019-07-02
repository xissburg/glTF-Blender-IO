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

def update_GLTFLODEntry_child_object(self, context):
    if self.previous_child_object is not None:
        self.previous_child_object.glTF_LOD_parent_object = None
    if self.child_object is not None:
        for entry in self.parent_object.glTF_LOD.entries:
            if entry != self and entry.child_object == self.child_object:
                entry.child_object = None
        self.child_object.glTF_LOD_parent_object = self.parent_object
    self.previous_child_object = self.child_object
    return None


class GLTFLODEntry(bpy.types.PropertyGroup):
    parent_object: bpy.props.PointerProperty(type=bpy.types.Object)
    previous_child_object: bpy.props.PointerProperty(type=bpy.types.Object)
    child_object: bpy.props.PointerProperty(type=bpy.types.Object, update=update_GLTFLODEntry_child_object)
    lod: bpy.props.IntProperty(name='LOD')
    screen_coverage: bpy.props.FloatProperty(name='Screen Coverage', default=1, min=0, max=1)


class GLTFLOD(bpy.types.PropertyGroup):
    screen_coverage_lod_0: bpy.props.FloatProperty(name='Screen Coverage', default=1, min=0, max=1)
    entries: bpy.props.CollectionProperty(type=GLTFLODEntry)


class OBJECT_OT_AddLod(bpy.types.Operator):
    bl_idname = 'object.add_lod'
    bl_label = 'Add LOD'
    bl_description = 'Add a level of detail to this object'

    def execute(self, context):
        obj = context.object
        entry = obj.glTF_LOD.entries.add()
        entry.parent_object = obj
        entry.lod = len(obj.glTF_LOD.entries)
        return {'FINISHED'}


class OBJECT_OT_DeleteLod(bpy.types.Operator):
    bl_idname = 'object.delete_lod'
    bl_label = 'Delete'
    bl_description = 'Delete this level of detail'

    entry_index: bpy.props.IntProperty(default=0)

    def execute(self, context):
        obj = context.object
        entry = obj.glTF_LOD.entries[self.entry_index]
        if entry.child_object is not None:
            entry.child_object.glTF_LOD_parent_object = None
        obj.glTF_LOD.entries.remove(self.entry_index)
        for index, entry in enumerate(obj.glTF_LOD.entries):
            entry.lod = index + 1
        return {'FINISHED'}


class OBJECT_OT_SelectParentLod(bpy.types.Operator):
    bl_idname = 'object.select_parent_lod'
    bl_label = 'Select root LOD object'
    bl_description = 'Selects the first object in this LOD chain'

    def execute(self, context):
        for obj in bpy.data.objects:
            obj.select_set(False)
        context.object.glTF_LOD_parent_object.select_set(True)
        context.view_layer.objects.active = context.object.glTF_LOD_parent_object
        return {'FINISHED'}


def register_lod_properties():
    bpy.types.Object.glTF_LOD = bpy.props.PointerProperty(type=GLTFLOD, options={'HIDDEN'})
    bpy.types.Object.glTF_LOD_parent_object = bpy.props.PointerProperty(type=bpy.types.Object, options={'HIDDEN'})


def unregister_lod_properties():
    del bpy.types.Object.glTF_LOD
    del bpy.types.Object.glTF_LOD_parent_object