`gmxoutchg_py`是<a href='http://bbs.keinsci.com/thread-5417-1-1.html' target='_blank'>`gmxoutchg`</a>的python版本。其操作方法与`gmxoutchg`完全一致。目前该软件只对`gromacs 2018.8`兼容，对其他版本的`gromacs`兼容性未知。`gmxoutchg_py.exe`为Windows版可执行文件，`gmxoutchg_py.py`为`gmxoutchg_py`的python源代码。`charge.tcl`为使VMD读入电荷信息的TCL脚本。

### 使用方法
* <strong>Step1</strong>: 将`gromacs`产生的二进制`tpr`文件转换采用`gmx dump -s XX.tpr > dump.txt`(XX.tpr为需要转换的`tpr`文件)转换成`dump.txt`文件。
* <strong>Step2</strong>: 将`dump.txt`文件放置在`gmxoutchg_py.exe`同级目录下。启动`gmxoutchg_py.exe`。随后，就可以看到如下图所示的界面。
  ```
  Extract atomic charges from formatted .tpr file (For gromacs 2018.8)
  Version 1.0, release date: 2024-Jun-20
  Programmed by Jian Zhang (jian_zhang@cug.edu.cn)
  
  Loading dump.txt!!!
  Number of molecular type:         5
  Number of atoms in molecular type LI (Number of molecular):         1 (11)
  Number of atoms in molecular type MG (Number of molecular):         1 (11)
  Number of atoms in molecular type CL (Number of molecular):         1 (33)
  Number of atoms in molecular type SOL (Number of molecular):         3 (1703)
  Number of atoms in molecular type COF (Number of molecular):       228 (5)
  Number of molecules:      1763
  charge.txt has been successfully created in this folder
  Press Enter to exit...
  ```
* <strong>Step3</strong>: 键入回车即可关闭该界面，然后在该目录下生成了`charge.txt`文件。`charge.txt`文件内容如下。
  ```
    1.000000       1           1
    1.000000       2           2
    1.000000       3           3
    1.000000       4           4
    1.000000       5           5
    1.000000       6           6
    1.000000       7           7
    1.000000       8           8
    1.000000       9           9
    1.000000      10          10
    1.000000      11          11
    2.000000      12          12
    2.000000      13          13
    2.000000      14          14
    2.000000      15          15
    ...
  ```
  文件中的第一列、第二列和第三列分别是原子电荷、分子序号和原子序号。
### 鸣谢
在开发`gmxoutchg_py`的过程中，参考了<a href='http://bbs.keinsci.com/thread-5417-1-1.html' target='_blank'>`gmxoutchg`</a>的Fortran源码。此外，还使用到了`dataclasses`库中的`dataclass`，`collections`库中的`OrderedDict`以及`re`库和`PyInstaller`库。在此对上述库或程序的开发者表示感谢。

### 许可证
`gmxoutchg_py`基于MIT许可证开源。这意味着您可以自由地使用，修改和分发代码。
