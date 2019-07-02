[![Blender](misc/Blender_logo.png)](http://www.blender.org/) [![glTF](misc/glTF_logo.png)](https://www.khronos.org/gltf/)  

Blender glTF 2.0 Importer and Exporter
======================================

Version
-------

Beta

Credits
-------

Developed by [UX3D](https://www.ux3d.io/) and [Julien Duroure](http://julienduroure.com/), with support from the [Khronos Group](https://www.khronos.org/), [Mozilla](https://www.mozilla.org/), and [Airbus Defense & Space](https://www.airbus.com/space.html).

Introduction
------------

Official Khronos Group Blender [glTF](https://www.khronos.org/gltf/) 2.0 importer and exporter.  

This project contains all features from the [previous exporter](https://github.com/KhronosGroup/glTF-Blender-Exporter), and all future development will happen on this repository. In addition, this repository contains a Blender importer, with common Python code shared between exporter and importer for round-trip workflows. New features are included or under development, but usage and menu functionality remain the same.

Major change compared to the current Khronos glTF 2.0 exporter is, that the Blender glTF importer and exporter code is maintained in one place. Installation is simpler and the user experience regarding the menu functionality the same. On the development side, synergies do exist by sharing common code between the importer and exporter. Having the solution in one place, this also allows importing and exporting glTF files like loading and saving them.

The shared code base is organised into common (Blender-independent) and Blender-specific packages:  

![Packages](docs/packages.png)  
Package organisation  

This structure allows easier Blender 2.79 to 2.80 updates, and enables common code to be reused by third-party Python packages working with the glTF 2.0 format.

![Process](docs/io_process.png)  
Import & export process

The main importer and exporter interface is the Python glTF scene representation.  
Blender scene data is first extracted and converted into this scene description. This glTF scene description is exported to the final JSON glTF file. Any compression of mesh, animation, or texture data happens here.  
For import, glTF data is parsed and written into the Python glTF scene description. Any decompression is executed in this step. Using the imported glTF scene tree, the Blender internal scene representation is generated from this information.

Installation
------------

The Khronos glTF 2.0 importer and exporter is enabled by default in beta versions of [Blender 2.8](https://www.blender.org/2-8/). To reinstall it — for example, when testing recent or upcoming changes — copy the `addons/io_scene_gltf2` folder into the `scripts/addons/` directory of the Blender installation, then enable it under the *Add-ons* tab. For additional development documentation, see [Debugging](DEBUGGING.md).

Usage Documentation
-------------------

See: https://docs.blender.org/manual/en/dev/addons/io_gltf2.html

Debugging
---------

- [Debug with PyCharm](https://code.blender.org/2015/10/debugging-python-code-with-pycharm) **NOTE:** If you are using Blender 2.80, you need the [updated debugger script](https://github.com/ux3d/random-blender-addons/blob/master/remote_debugger.py)
- [Debug with VSCode](DEBUGGING.md)

Continuous Integration Tests
----------------------------

Several companies, individuals, and glTF community members contribute to Blender glTF I/O. Functionality is added and bugs are fixed regularly. Because hobbyists and professionals using Blender glTF I/O rely on its stability for their daily work, continuous integration tests are enabled. After each commit or pull request, the following tests are run:

-	Export Blender scene and validate using the [glTF validator](https://github.com/KhronosGroup/glTF-Validator/)
-	Round trip import-export and comparison of glTF validator results  

These quality-assurance checks improve the reliability of Blender glTF I/O.  

[![CircleCI](https://circleci.com/gh/KhronosGroup/glTF-Blender-IO.svg?style=svg)](https://circleci.com/gh/KhronosGroup/glTF-Blender-IO)

Running the Tests Locally
-------------------------

To run the tests locally, your system should be modified to include `blender279b` and `blender28` as shell scripts (or Windows `.bat` files) in the path that launch their respective versions of Blender, including all command-line arguments.

The latest version of [Yarn](https://yarnpkg.com/en/) should also be installed.

Then, in the `tests` folder of this repository, run `yarn install`, followed by `yarn run test`.  You can limit the test suite to one version of Blender with `yarn run test-blender279b` or `yarn run test-blender28`.

MSFT_lod Extension
------------------

To setup LODs for export using the [MSFT_lod extension](https://github.com/KhronosGroup/glTF/tree/master/extensions/2.0/Vendor/MSFT_lod), select the high definition model (LOD 0) and go to the _Properties_ panel, _Object_ tab and you'll find a _glTF_ panel. Inside of it you'll find a _Levels of Detail_ section with an _Add LOD_ button. Click _Add LOD_ and a new LOD entry will be created. Then pick the LOD 1 object and adjust its _Screen Coverage_ property. Repeat for the other LODs. You should also set the LOD 0 screen converage property at the top, since LOD 0 is drawn from values 1 until the value set in this field. LOD preview is not supported in the Blender viewport yet.
