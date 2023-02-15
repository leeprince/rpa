# RPA 客户端
---

# 工作目录
工作目录为当前项目`tax_rpa_client`

# 关于环境
- windows 使用 `系统环境`
- macOS 使用 `venv虚拟环境（独立python环境）`

# 编译
## 编译成可执行文件
### 使用 pyinstaller 编译

#### 使用说明
官网地址[https://pyinstaller.org/en/stable/usage.html](https://pyinstaller.org/en/stable/usage.html)

```
# 如何生成
-F, –onefile 
   打包一个单个文件，如果你的代码都写在一个.py文件的话，可以用这个，如果是多个.py文件就别用
-D, –onedir 
   打包多个文件，在dist中生成很多依赖文件，适合以框架形式编写工具代码，我个人比较推荐这样，代码易于维护
   > 当需要将 `chromedriver` 可执行文件一起编译时，建议使用该参数编译 + 程序中获取可执行文件路径找到 `chromedriver` 实现编译后的文件不在要求使用者重新安装
-n NAME, –name=NAME 
   可选的项目(产生的spec的)名字.如果省略,第一个脚本的主文件名将作为spec的名字

# 如何捆绑资源
--add-data <SRC;DEST or SRC:DEST>
   要添加到可执行文件的其他非二进制文件或文件夹。路径分隔符是平台特定的，使用 os.pathsep（在 Windows 上是 ; 在大多数 unix 系统上是 :）。此选项可以多次使用。
--add-binary <SRC;DEST or SRC:DEST>
    要添加到可执行文件的附加二进制文件。有关详细信息，请参阅 --add-data 选项。此选项可以多次使用。
-p DIR, --paths DIR
    设置导入路径(和使用PYTHONPATH效果相似).可以用路径分割符(Windows使用分号,Linux使用冒号)分割,指定多个目录.也可以使用多个-p参数来设置多个导入路径，让pyinstaller自己去找程序需要的资源

# Windows 与 MacOS 的不同
-w,–windowed,–noconsole 
   使用Windows子系统执行.当程序启动的时候不会打开命令行(只对Windows有效)
-c,–nowindowed,–console 
   使用控制台子系统执行(默认)(只对Windows有效)
-i <FILE.ico or FILE.exe,ID or FILE.icns or Image or "NONE">, --icon <FILE.ico or FILE.exe,ID or FILE.icns or Image or "NONE">
    FILE.ico：将图标应用于 Windows 可执行文件。 FILE.exe,ID：从exe中提取带有ID的图标。 FILE.icns：将图标应用到 Mac OS 上的 .app 包。如果输入的图像文件不是平台格式（Windows 上的 ico，Mac 上的 icns），PyInstaller 会尝试使用 Pillow 将图标转换为正确的格式（如果安装了 Pillow）。使用“NONE”不应用任何图标，从而使操作系统显示一些默认值（默认值：应用 PyInstaller 的图标）
```
#### 编译步骤
1. 安装 pyinstaller
```
$ pip install pyinstaller 
```
2. 进入入口文件所在目录
3. 编译成 XXX.py 对应的可执行文件。 
   - 在 windows 操作系统中会生成 XXX.exe 可执行文件
   - 在 macOS 操作系统中会生成 XXX （没有后缀）可执行文件
   - 生成的路径在：`./dist/`

**系统环境（本机python）**
```
# 打包exe
Pyinstaller -F main.py

# 打包exe && 不带控制台的打包
Pyinstaller -F -w main.py

# 打包exe && 指定exe图标打包
Pyinstaller -F -w -i logo.ico main.py

# windows 包含 chromedriver 可执行文件。通过`;`分隔
pyinstaller -F --add-binary "chromedriver.exe";"." main.py
# macOS 包含 chromedriver 可执行文件。通过`:`分隔
pyinstaller -F --add-binary chromedriver:. main.py
pyinstaller -D --add-binary chromedriver:. main.py
Pyinstaller -D -w -i logo.ico  --add-binary chromedriver:. main.py
```

**venv虚拟环境（独立python环境）**
```
# 打包exe
./venv/bin/pyinstaller -F main.py 

# 打包exe && 不带控制台的打包
./venv/bin/pyinstaller -F -w main.py

# windows 包含 chromedriver 可执行文件。通过`;`分隔
./venv/bin/pyinstaller -F --add-binary "chromedriver.exe";"." main.py
# macOS 包含 chromedriver 可执行文件。通过`:`分隔
./venv/bin/pyinstaller -F --add-binary chromedriver:. main.py
./venv/bin/pyinstaller -F -w -i logo.ico --add-binary chromedriver:. main.py
```

### 使用 py2app 编译
1. 安装 py2app
```
pip install py2app
```
2. 安装以后，cd到你的目录，然后构建一个“setup.py”安装文件
```
py2applet --make-setup main.py
```
3. 构建成可执行文件
   - 在 windows 操作系统中会生成 XXX.exe 可执行文件
   - 在 macOS 操作系统中会生成 XXX （没有后缀）可执行文件
   - 生成的路径在：`./dist/`
```
# 自己使用，不包含所需的第三方库，速度快，占用存储空间少，在别人的机器上有可能报错
python setup.py py2app -A
 
# 将所有需要的库包含在里面，适用于别人使用
python setup.py py2app
```