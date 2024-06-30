import bpy
from bl_operators.presets import AddPresetBase


class VIEW3D_MT_dyntopo_preset(bpy.types.Menu):
    bl_label = "New Preset"
    preset_subdir = "dyntopo_preset"
    preset_operator = "script.execute_preset"
    draw = bpy.types.Menu.draw_preset


class VIEW3D_OT_dyntopo_preset_add(AddPresetBase, bpy.types.Operator):
    bl_idname = "dyntopo_preset.add"
    bl_label = "Add Dyntopo Preset"
    preset_menu = "VIEW3D_MT_dyntopo_preset"

    preset_defines = ["sculpt = bpy.context.scene.tool_settings.sculpt"]

    preset_values = [
        "sculpt.detail_type_method",
        "sculpt.constant_detail_resolution",
        "sculpt.detail_size",
        "sculpt.detail_percent",
        "sculpt.detail_refine_method",
    ]

    preset_subdir = VIEW3D_MT_dyntopo_preset.preset_subdir


classes = (
    VIEW3D_MT_dyntopo_preset,
    VIEW3D_OT_dyntopo_preset_add,
)


def preset_menu(self, context):
    row = self.layout.row(align=True)
    row.menu(
        VIEW3D_MT_dyntopo_preset.__name__,
        text=VIEW3D_MT_dyntopo_preset.bl_label,
    )
    row.operator(VIEW3D_OT_dyntopo_preset_add.bl_idname, text="", icon="ADD")
    row.operator(
        VIEW3D_OT_dyntopo_preset_add.bl_idname, text="", icon="REMOVE"
    ).remove_active = True


def register_classes():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.VIEW3D_PT_sculpt_dyntopo.prepend(preset_menu)


def unregister_classes():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.types.VIEW3D_PT_sculpt_dyntopo.remove(preset_menu)
