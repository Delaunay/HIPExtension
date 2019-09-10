from setuptools import setup
from hipext.extension import CUDAExtension, BuildExtension

ext_modules = []
extension = CUDAExtension(
    'torch_test_cpp_extension.cuda', [
        'cuda_extension.cpp',
        'cuda_extension_kernel.cu',
        'cuda_extension_kernel2.cu',
    ],
    extra_compile_args={
        'cxx': [],
        'nvcc': ['-O2']
    }
)
ext_modules.append(extension)

setup(
    name='torch_test_cpp_extension',
    packages=['torch_test_cpp_extension'],
    ext_modules=ext_modules,
    cmdclass={'build_ext': BuildExtension}
)
