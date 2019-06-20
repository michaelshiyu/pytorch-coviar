from distutils.core import setup, Extension
import numpy as np

coviar_utils_module = Extension('coviar_loader',
		sources = ['coviar_data_loader.c'],
		include_dirs=[np.get_include(), './ffmpeg/include/'],
		extra_compile_args=['-DNDEBUG', '-O3'],
		extra_link_args=['-lavutil', '-lavcodec', '-lavformat', '-lswscale', '-L./ffmpeg/lib/']
)

setup ( name = 'coviar_loader',
	version = '0.1',
	description = 'Utils for coviar_loader training.',
	ext_modules = [ coviar_utils_module ]
)
