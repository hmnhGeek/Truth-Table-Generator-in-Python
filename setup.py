import cx_Freeze

executables = [cx_Freeze.Executable('Truth Table Generator.py')]

cx_Freeze.setup(
    name='TTG',
    options={"build_exe": {"packages":["os"]}},

    description="TTG",
    executables = executables
    )
