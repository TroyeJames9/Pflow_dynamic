# -*- coding: utf-8 -*-

"""所有跨文件的全局变量由本模块计算并赋值

其他模块需要使用本模块全局变量时，在模块开头导入本模块即可
例子：
    from setting import *...

"""

import os
import sys
import re
from pathlib import Path


FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # program root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

# data
V_DIR = ROOT / "video"
PV_DIR = ROOT / "pre_video"

# config
C_DIR = ROOT / "config"
CONFIG_INI = C_DIR / "config.ini"
