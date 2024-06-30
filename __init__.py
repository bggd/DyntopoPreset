bl_info = {
    "name": "DyntopoPreset",
    "author": "birthggd",
    "description": "preset for dyntopo",
    "blender": (4, 1, 0),
    "version": (1, 1, 1),
    "location": "",
    "warning": "",
    "category": "Interface",
}

import bpy

from . import _refresh_

_refresh_.reload_modules()

from . import dyntopo_preset

def register():
    dyntopo_preset.register_classes()


def unregister():
    dyntopo_preset.unregister_classes()


if __name__ == "__main__":
    register()
