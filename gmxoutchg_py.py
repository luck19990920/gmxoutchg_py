from  dataclasses import dataclass
from collections import OrderedDict
import re

@dataclass
class molecule:
    num_molecule: int  # 分子的个数
    num_atom: int  = 0    # 一种分子中原子的数量
    charge: tuple  | None = None   # 一种分子中每个原子的电荷

print(f'Extract atomic charges from formatted .tpr file (For gromacs 2018.8)\n'
      f'Version 1.0, release date: 2024-Jun-20\n'
      f'Programmed by Jian Zhang (jian_zhang@cug.edu.cn)\n'
)

gmxoutchg_inf = OrderedDict()   # 键为分子的名字,值为molecule对象

regex = re.compile(r'moltype\s\(\d+\)')
regex_name = re.compile(r'\s+name=\"(.+)\"')
atom_num_regex = re.compile(r'atom\s\((\d+)\):')
atom_q_regex = re.compile(r'atom\[\s+\d+\]={.+q=(.+),\smB.+}')
print('Loading dump.txt!!!')
with open('./dump.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].strip()

        if line.startswith('grp['):
            break

        if line.startswith('moltype'):
            if '=' in line:
                molecule_name = line.split()[-1].strip('"')   # 获取分子的名字
                molecule_num = int(lines[i+1].strip().split('=')[-1])   # 获取体系中每种分子的个数
                if molecule_name in gmxoutchg_inf:
                    gmxoutchg_inf[molecule_name].num_molecule += molecule_num
                else:
                    gmxoutchg_inf[molecule_name] = molecule(num_molecule=molecule_num)
            else:
                molecule_name = str(lines[i+1].strip().split('=')[-1].strip('"')) # type: ignore
                atom_num = int(re.search(atom_num_regex, lines[i+3]).group(1))   # type: ignore # 获取每个分子中原子的个数
                charge = []      # 存储分子中原子电荷信息的列表
                for k in range(atom_num):
                    charge.append(float(re.search(atom_q_regex, lines[i+4+k]).group(1)))   # type: ignore # 存储电荷信息
                gmxoutchg_inf[molecule_name].num_atom += atom_num # type: ignore
                gmxoutchg_inf[molecule_name].charge = tuple(charge)

print(f'Number of molecular type:{len(gmxoutchg_inf):>10}')
for molecule_name in list(gmxoutchg_inf.keys()):
    print(f'Number of atoms in molecular type {molecule_name} (Number of molecular):{gmxoutchg_inf[molecule_name].num_atom:>10} ({gmxoutchg_inf[molecule_name].num_molecule})')
with open('./charge.txt', 'w', encoding='utf-8') as f:
    mole_num = 1  # 分子序号
    atom_num = 1  # 原子序号
    for j in range(len(gmxoutchg_inf)):
        key, value = gmxoutchg_inf.popitem(last=False)
        for m in range(value.num_molecule):
            for n in range(value.num_atom):
                f.write(f'{value.charge[n]:>12.6f}{mole_num:>8}{atom_num:>12}\n')
                atom_num += 1
            mole_num += 1

print(f'Number of molecules:{mole_num-1:>10}')


print('charge.txt has been successfully created in this folder')
input('Press Enter to exit...')

