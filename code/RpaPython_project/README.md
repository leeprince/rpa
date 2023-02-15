# RPA
RPA（机器人流程自动化）通过模拟人的界面操作，自动完成跨系统、跨平台重复有规律的工作流任务，成倍提升人的工作效率。

# 目录结构


# 一、RPA-Python
> 地址：https://github.com/leeprince/RPA-Python

该工具以前称为 TagUI for Python

## 安装
为 RPA（机器人过程自动化）安装这个 Python 包
```
pip install rpa
```

## python程序导入包
```
import rpa as r
```

## 运行`rpa-python-test`目录下的测试用例
- 需要先初始化 tagui：r.init()
  - 这部分报错：建议先看 [RPA-Python 核心](# 1. init()： 初始化 tagui)

## (一) RPA-Python 核心

### 1. init()： 初始化 tagui
- tagui.py
  - {pythonPath}/lib/site-packages/tagui.py
- 检查 {tagui_executable} 的路径。windows:{tagui_executable}==~\AppData\Roaming\tagui\...;
  - 检查是否存在 tagui 文件夹，存在则当作已安装tagui，否则执行 setup() 方法

### 2. setup()：安装 tagui
> 建议第一次启动可以搭梯子，会自动安装相关依赖。
>  - 如果没有梯子则会出现下载各种依赖包失败的情况, 同样可以按照下面的步骤检查,并手动安装相关依赖
>    - Windows
>      - 搭梯子之后，成功自动安装相关依赖。 
>      - 手动下载各种依赖并打包放在 `rpa-python相关包/windows_rpa_python.zip解压后无tagui文件夹/rpa_python.zip`
>        - 说明：因为 Windows 依赖就多，搭梯子安装成功，未继续手动打包（仍有部分包未打包进去）
>    - MacOS 
>      - 报错：`＜urlopen error [Errno 61] Connection refused＞`
>        - 原因：即使搭梯子也一直报错，具体原因暂不清楚
>        - 解决：手动下载各种依赖并打包放在 `rpa-python相关包/macos_rpa_python.zip解压后不包含tagui文件夹/rpa_python已包含setup()依赖.zip`
>          - `rpa_python已包含setup()依赖.zip` 需查看下面的执行流程，重命名为`rpa_python.zip`并放到工作目录下

> 说明：安装的绝大多数依赖包都可以在 `rpa-python相关包/RPA-Python-Tump` 及操作系统对应的{tagui_zip_file}中找到

- 检查`os.path(默认：应用程序执行的当前路径。可指定检查的绝对路径或者相对路径)`是否存在 rpa_python.zip
  - 存在
    - 移动到成 {home_directory}/{tagui_zip_file}
      - 不同操作系统{home_directory}({home_directory}=tagui_location())不一样。
        - tagui_location()
          - windows:`~\AppData\Roaming\`
          - macos:`~`
      - 不同操作系统{tagui_zip_file}不一样。
        - TagUI_Linux.zip
        - TagUI_macOS.zip
        - TagUI_Windows.zip
    > 注意：移动到成 {home_directory}/{tagui_zip_file} 后会自动检查 {home_directory} 是否存在 `tagui` 文件夹，没有则创建。
    > 所以 rpa_python.zip 解压后的包不应包含 `tagui` 文件夹，否则报错 `unable to unzip TagUI to {home_directory}`
  - 不存在则执行下载
    - 下载路径为：`https://github.com/tebelorg/Tump/releases/download/v1.0.0/{tagui_zip_file}`
      - 如windows:`https://github.com/tebelorg/Tump/releases/download/v1.0.0/TagUI_Windows.zip`）
      - 如MacOs:`https://github.com/tebelorg/Tump/releases/download/v1.0.0/TagUI_macOS.zip`）
    - 下载 到{home_directory}/{tagui_zip_file}中，并解压成 {home_directory}/{tagui}
    
    > 注意：下载 `https://github.com/tebelorg/Tump/releases/download/v1.0.0/{tagui_zip_file}` 压缩包，解压后自动包含 `tagui` 文件夹
  > 注意：解压后检查 tagui 是否有效：检查 {home_directory}\tagui\src\tagui 是否是一个文件

- 重命名 {home_directory}/{tagui} 为 {tagui_directory}
  - windows:{home_directory}/tagui
  - macos:{home_directory}/.tagui

  - _tagui_delta():从{tagui_delta_url}下载稳定的 delta 文件到 {tagui_delta_file} = base_directory + '/' + 'src' + '/' + delta_file
    - delta 文件列表({delta_file}列表)：`['tagui', 'tagui.cmd', 'end_processes', 'end_processes.cmd', 'tagui_header.js', 'tagui_parse.php', 'tagui.sikuli/tagui.py']`
    - tagui_delta_url = `https://raw.githubusercontent.com/tebelorg/Tump/master/TagUI-Python/'{delta_file}`
    - {tagui_delta_file} = {base_directory}/src/{delta_file}
    - prince.lee@commt
      - 添加：先检查包中是否包含{delta_file}文件，没有再下载
        - 源码：
          ```
          for delta_file in delta_list:
              tagui_delta_url = 'https://raw.githubusercontent.com/tebelorg/Tump/master/TagUI-Python/' + delta_file
              tagui_delta_file = base_directory + '/' + 'src' + '/' + delta_file
          
              # --- 先检查本地是否存在 prince.lee@commt 2022/5/29 12:05
              if os.path.isfile(tagui_delta_file):
                  print('[RPA][INFO][_tagui_delta] - have tagui_delta_file', tagui_delta_file)
                  continue
              else:
                  print('[RPA][INFO][_tagui_delta] - not have tagui_delta_file', tagui_delta_file)
              # --- 先检查本地是否存在-end prince.lee@commt 2022/5/29 12:05
          
              if not download(tagui_delta_url, tagui_delta_file): return False
          ```
        - 目的：允许手动解压好的包中，包含{delta_file}文件
      
- _patch_macos_pjs(): 修补 PhantomJS 以解决 OpenSSL 问题
  - 检查操作系统及指定路径下是否包含`phantomjs_old`:`if platform.system() == 'Darwin' and not os.path.isdir(tagui_location() + '/.tagui/src/phantomjs_old'):`
    - 获取当前工作目录的路径：`original_directory = os.getcwd();`
    - 改变当前工作目录到指定的路径：`os.chdir(tagui_location() + '/.tagui/src')`
    - prince.lee@commt
      - 添加：先检查已改变当前工作目录到指定的路径下是否包含