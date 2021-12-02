# ############## 2. pull最新代码 ##############
import os
from git.repo import Repo
 
local_path = os.getcwd()
repo = Repo(local_path)
repo.git.pull()