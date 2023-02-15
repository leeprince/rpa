# RPA �ͻ���
---

# ����Ŀ¼
����Ŀ¼Ϊ��ǰ��Ŀ`tax_rpa_client`

# ���ڻ���
- windows ʹ�� `ϵͳ����`
- macOS ʹ�� `venv���⻷��������python������`

# ����
## ����ɿ�ִ���ļ�
### ʹ�� pyinstaller ����

#### ʹ��˵��
������ַ[https://pyinstaller.org/en/stable/usage.html](https://pyinstaller.org/en/stable/usage.html)

```
# �������
-F, �Conefile 
   ���һ�������ļ��������Ĵ��붼д��һ��.py�ļ��Ļ������������������Ƕ��.py�ļ��ͱ���
-D, �Conedir 
   �������ļ�����dist�����ɺܶ������ļ����ʺ��Կ����ʽ��д���ߴ��룬�Ҹ��˱Ƚ��Ƽ���������������ά��
   > ����Ҫ�� `chromedriver` ��ִ���ļ�һ�����ʱ������ʹ�øò������� + �����л�ȡ��ִ���ļ�·���ҵ� `chromedriver` ʵ�ֱ������ļ�����Ҫ��ʹ�������°�װ
-n NAME, �Cname=NAME 
   ��ѡ����Ŀ(������spec��)����.���ʡ��,��һ���ű������ļ�������Ϊspec������

# ���������Դ
--add-data <SRC;DEST or SRC:DEST>
   Ҫ��ӵ���ִ���ļ��������Ƕ������ļ����ļ��С�·���ָ�����ƽ̨�ض��ģ�ʹ�� os.pathsep���� Windows ���� ; �ڴ���� unix ϵͳ���� :������ѡ����Զ��ʹ�á�
--add-binary <SRC;DEST or SRC:DEST>
    Ҫ��ӵ���ִ���ļ��ĸ��Ӷ������ļ����й���ϸ��Ϣ������� --add-data ѡ���ѡ����Զ��ʹ�á�
-p DIR, --paths DIR
    ���õ���·��(��ʹ��PYTHONPATHЧ������).������·���ָ��(Windowsʹ�÷ֺ�,Linuxʹ��ð��)�ָ�,ָ�����Ŀ¼.Ҳ����ʹ�ö��-p���������ö������·������pyinstaller�Լ�ȥ�ҳ�����Ҫ����Դ

# Windows �� MacOS �Ĳ�ͬ
-w,�Cwindowed,�Cnoconsole 
   ʹ��Windows��ϵͳִ��.������������ʱ�򲻻��������(ֻ��Windows��Ч)
-c,�Cnowindowed,�Cconsole 
   ʹ�ÿ���̨��ϵͳִ��(Ĭ��)(ֻ��Windows��Ч)
-i <FILE.ico or FILE.exe,ID or FILE.icns or Image or "NONE">, --icon <FILE.ico or FILE.exe,ID or FILE.icns or Image or "NONE">
    FILE.ico����ͼ��Ӧ���� Windows ��ִ���ļ��� FILE.exe,ID����exe����ȡ����ID��ͼ�ꡣ FILE.icns����ͼ��Ӧ�õ� Mac OS �ϵ� .app ������������ͼ���ļ�����ƽ̨��ʽ��Windows �ϵ� ico��Mac �ϵ� icns����PyInstaller �᳢��ʹ�� Pillow ��ͼ��ת��Ϊ��ȷ�ĸ�ʽ�������װ�� Pillow����ʹ�á�NONE����Ӧ���κ�ͼ�꣬�Ӷ�ʹ����ϵͳ��ʾһЩĬ��ֵ��Ĭ��ֵ��Ӧ�� PyInstaller ��ͼ�꣩
```
#### ���벽��
1. ��װ pyinstaller
```
$ pip install pyinstaller 
```
2. ��������ļ�����Ŀ¼
3. ����� XXX.py ��Ӧ�Ŀ�ִ���ļ��� 
   - �� windows ����ϵͳ�л����� XXX.exe ��ִ���ļ�
   - �� macOS ����ϵͳ�л����� XXX ��û�к�׺����ִ���ļ�
   - ���ɵ�·���ڣ�`./dist/`

**ϵͳ����������python��**
```
# ���exe
Pyinstaller -F main.py

# ���exe && ��������̨�Ĵ��
Pyinstaller -F -w main.py

# ���exe && ָ��exeͼ����
Pyinstaller -F -w -i logo.ico main.py

# windows ���� chromedriver ��ִ���ļ���ͨ��`;`�ָ�
pyinstaller -F --add-binary "chromedriver.exe";"." main.py
# macOS ���� chromedriver ��ִ���ļ���ͨ��`:`�ָ�
pyinstaller -F --add-binary chromedriver:. main.py
pyinstaller -D --add-binary chromedriver:. main.py
Pyinstaller -D -w -i logo.ico  --add-binary chromedriver:. main.py
```

**venv���⻷��������python������**
```
# ���exe
./venv/bin/pyinstaller -F main.py 

# ���exe && ��������̨�Ĵ��
./venv/bin/pyinstaller -F -w main.py

# windows ���� chromedriver ��ִ���ļ���ͨ��`;`�ָ�
./venv/bin/pyinstaller -F --add-binary "chromedriver.exe";"." main.py
# macOS ���� chromedriver ��ִ���ļ���ͨ��`:`�ָ�
./venv/bin/pyinstaller -F --add-binary chromedriver:. main.py
./venv/bin/pyinstaller -F -w -i logo.ico --add-binary chromedriver:. main.py
```

### ʹ�� py2app ����
1. ��װ py2app
```
pip install py2app
```
2. ��װ�Ժ�cd�����Ŀ¼��Ȼ�󹹽�һ����setup.py����װ�ļ�
```
py2applet --make-setup main.py
```
3. �����ɿ�ִ���ļ�
   - �� windows ����ϵͳ�л����� XXX.exe ��ִ���ļ�
   - �� macOS ����ϵͳ�л����� XXX ��û�к�׺����ִ���ļ�
   - ���ɵ�·���ڣ�`./dist/`
```
# �Լ�ʹ�ã�����������ĵ������⣬�ٶȿ죬ռ�ô洢�ռ��٣��ڱ��˵Ļ������п��ܱ���
python setup.py py2app -A
 
# ��������Ҫ�Ŀ���������棬�����ڱ���ʹ��
python setup.py py2app
```