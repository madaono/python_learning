#比起JS中习惯的NPM 跟 YARN，py的包管理工具是pip/
# 安装一个Pillow pip install Pillow

from PIL import Image
im = Image.open('liangzi.jpg')
print(im.format, im.size, im.mode)
# JPEG (1920, 1080) RGB
im.thumbnail((200, 100))
im.save('liangzi1.jpg', 'JPEG')
# PYTHON真好玩啊，哈哈哈
# python模块的搜索路径是：默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中

# 如果我们要添加自己的搜索目录，有两种方法：
#
# 一是直接修改sys.path，添加要搜索的目录：
#
# >>> import sys
# >>> sys.path.append('/Users/michael/my_py_scripts')