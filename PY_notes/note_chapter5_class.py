# -*- coding:utf-8 -*-

#===============================================================
#    TITLE: 5.1 describe:  Class
#    NOTE: 
#   0. ClassName 通常采用 CamelCase 记法
#   1. 函数第一个参数为self(对象本身) 
#   2. 养成写function和class的doc的习惯
#===============================================================

 
# attributes属性
f = open("temp", 'w')
print('\n'.join(dir(f)))
print("===================")

print(f.mode)
print(f.closed)

# method
f.write("Hi.\n")
f.seek(0)
f.write("Hola.\n")
f.close()
print(f.closed)
import os
os.remove("temp")


class Forest(object):
    '''doc of Forest.'''
    def method(self):
        print("in method function")
        return
    pass
if __name__ == "__main__":
    print(Forest.__doc__)
    forest = Forest()
    forest.method()


#===============================================================
#    describe:  添加属性
#===============================================================

    # 直接添加自己的属性
    forest.tree = 3
    print(forest.tree)
    # 默认新建的并没有
    forest2 = Forest()
    try:
        print(forest2.tree)
    except:
        print("没有该tree属性")


print("#===============================================================")
print("#    describe:  定义的时候添加 通过__init__函数")
print("#===============================================================")

class Forest(): # 默认添加了object
    '''doc of NewForest.'''
    def __init__(self, name = 'init', trees = 0):   #构造函数
        print("构造函数")
        self.name = name
        self.trees = trees
        
    def grow(self):
        self.trees += 1
        print("the tree is growing!")
        
    def number(self):
        if self.trees == 1:
            print('there is 1 tree.')
        else:
            print('there are', self.trees, 'trees.')


forest = Forest("sss", 100)
print(forest.name, forest.trees)
forest.trees += 1
forest.grow() # 执行grow方法
forest.number()  # 执行number方法

forest = Forest()
forest.number()  # 执行number方法

print("# 总结： 首先：")
# Python 2.x中默认都是经典类，只有显式继承了object才是新式类
print("# Python 3.x中默认都是新式类，不必显式的继承object")

# 其次：
print("# ------新式类对象可以直接通过__class__属性获取自身类型:type")
# ------继承搜索的顺序发生了改变,经典类多继承属性搜索顺序: 先深入继承树左侧，再返回，开始找右侧;新式类多继承属性搜索顺序: 先水平搜索，然后再向上移动
# ------新式类增加了__slots__内置属性, 可以把实例属性的种类锁定到__slots__规定的范围之中
# ------新式类增加了__getattribute__方法
# 最后，在多继承中，新式类采用广度优先搜索，而旧式类是采用深度优先搜索。新式类更符合OOP编程思想，统一了python中的类型机制。


#===============================================================
#    describe:  python崇尚的鸭子类型 (无多态,也用不着多态)
#===============================================================

# 在 Python 中，鸭子类型（duck typing）是一种动态类型的风格。所谓鸭子类型，来自于 James Whitcomb Riley 的“鸭子测试”：
# ~~ 当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。
# 假设我们需要定义一个函数，这个函数使用一个类型为鸭子的参数，并调用它的走和叫方法。
# 在鸭子类型的语言中，这样的函数可以接受任何类型的对象，只要这个对象实现了走和叫的方法，否则就引发一个运行时错误。换句话说，任何拥有走和叫方法的参数都是合法的。


class Leaf(object):

    def __init__(self, color="green"):
        self.color = color

    def fall(self):
        print("Splat!")
class MapleLeaf(Leaf):
    
    def change_color(self):
        if self.color == "green":
            self.color = "red"
    def fall(self):
        self.change_color()
        super(MapleLeaf, self).fall()  # super(CurrentClassName, instance) # 返回该类实例对应的父类对象。           

class Acorn(object):
    
    def fall(self):
        print("Plunk!")
# 这三个类都实现了 fall() 方法，因此可以这样使用：


objects = [Leaf(), MapleLeaf(), Acorn()]
for obj in objects:
    obj.fall()


print("# 这里，我们先改变树叶的颜色，然后再找到这个实例对应的父类，并调用父类的 `fall()` 方法：")

mleaf = MapleLeaf()

print(mleaf.color)
mleaf.fall()
print(mleaf.color)

# 类和对象在内存中是如何保存？
# 答：类以及类中的方法在内存中只有一份，而根据类创建的每一个对象都在内存中需要存一份，



#===============================================================
print("#    describe:  类的成员: 属性,方法,特性(三大类)")
#===============================================================

# 属性
    #1. 普通字段(实例属性)
    #2. 静态字段(类属性)


class People(object):
    country = 'name123' #类属性

print(hasattr(People, 'country'))   # hasattr函数，判断类是否拥有属性
print("1:", People.country) 
p = People()
print("2:", p.country)
p.country = 'xiaoke' 
print("3:", p.country)      #实例属性会屏蔽掉同名的类属性
print("4:", People.country)
del p.country    #删除实例属性
print("5:", p.country)
People.country = 'modify shuxing of Class'
print("6:", p.country)

People.country2 = "ddd"
print(People.country2)
print(p.country)
print(p.country2)

print("hasattr, getattr")
if hasattr(p, 'country'):  
    print(getattr(p, 'country'))  # 通过getattr函数得到属性值
    
if hasattr(People, 'country2'):
    print(getattr(People, 'country2'))



#===============================================================
#    describe:  属性与方法的绑定
#===============================================================

import types   
  
class Student(object):  
    pass  
      
def hello(self,name):  
    print('hello ,',name)  

m=Student()  
n=Student()  


m.my_hello = types.MethodType(hello,m) #为实例mt绑定一个my_hello方法，方法指向hello
m.my_hello('Appleyk')  
# WARN:
print("n.my_hello('Kobe')  # !!!! error")

Student.my_hello = types.MethodType(hello,Student) #为类Student绑定一个my_hello方法，方法指向hello
m.my_hello('Appleyk')  
n.my_hello('Kobe')  # OK

Student.my_hello = hello
m.my_hello('Appleyk')  
n.my_hello('Kobe')  # OK



#===============================================================
#    TITLE: 5.2
#    describe:  __slots__ = ('name', 'sex') :当前类只可绑定这俩属性,其子类不受限
#===============================================================

# WARN: 有__slot__的情况下:如果先添加类属性,再添加同名的实例属性,则会报错(属性只读),或反过来,然后同时访问类属性和实例属性,结果不明白




times in msec
 clock   self+sourced   self:  sourced script
 clock   elapsed:              other lines

000.008  000.008: --- VIM STARTING ---
000.120  000.112: Allocated generic buffers
000.568  000.448: locale set
000.593  000.025: GUI prepared
000.596  000.003: clipboard setup
000.606  000.010: window checked
001.152  000.546: inits 1
001.161  000.009: parsing arguments
005.502  004.341: expanding arguments
009.262  003.760: shell init
009.705  000.443: Termcap init
009.753  000.048: inits 2
012.233  002.480: init highlight
012.700  000.314  000.314: sourcing $VIM/vimrc
021.245  008.219  008.219: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/filetype.vim
023.760  002.380  002.380: sourcing /Users/iff/.vim/autoload/plug.vim
028.845  001.996  001.996: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/ftoff.vim
039.310  000.026  000.026: sourcing /Users/iff/.vim/plugged/vim-fugitive/ftdetect/fugitive.vim
039.554  008.627  008.601: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/filetype.vim
039.899  000.065  000.065: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/ftplugin.vim
040.254  000.064  000.064: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/indent.vim
041.433  000.447  000.447: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/syncolor.vim
041.615  000.916  000.469: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/synload.vim
041.662  001.256  000.340: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/syntax.vim
042.346  000.359  000.359: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/nosyntax.vim
043.198  000.280  000.280: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/syncolor.vim
043.373  000.747  000.467: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/synload.vim
043.416  001.567  000.461: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/syntax.vim
044.015  000.029  000.029: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/filetype.vim
044.334  000.024  000.024: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/ftplugin.vim
046.934  000.807  000.807: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/pack/dist/opt/matchit/plugin/matchit.vim
047.009  002.366  001.559: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/macros/matchit.vim
047.425  000.031  000.031: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/filetype.vim
047.732  000.026  000.026: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/ftplugin.vim
048.055  000.023  000.023: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/indent.vim
048.884  000.029  000.029: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/filetype.vim
049.210  000.026  000.026: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/ftplugin.vim
050.175  000.288  000.288: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/syncolor.vim
051.043  000.286  000.286: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/syncolor.vim
055.499  005.021  004.735: sourcing /Users/iff/.vim/plugged/vim-monokai-tasty/colors/vim-monokai-tasty.vim
055.741  042.939  010.902: sourcing $HOME/.vimrc
055.749  000.263: sourcing vimrc file(s)
056.939  000.693  000.693: sourcing /Users/iff/.vim/plugged/vim-surround/plugin/surround.vim
057.831  000.703  000.703: sourcing /Users/iff/.vim/plugged/vim-rails/plugin/rails.vim
058.913  000.261  000.261: sourcing /Users/iff/.vim/plugged/nerdtree/autoload/nerdtree.vim
061.103  000.809  000.809: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/path.vim
061.406  000.183  000.183: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/menu_controller.vim
061.637  000.119  000.119: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/menu_item.vim
061.906  000.162  000.162: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/key_map.vim
062.333  000.319  000.319: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/bookmark.vim
062.754  000.309  000.309: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/tree_file_node.vim
063.470  000.606  000.606: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/tree_dir_node.vim
063.886  000.306  000.306: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/opener.vim
064.322  000.331  000.331: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/creator.vim
064.506  000.082  000.082: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/flag_set.vim
064.812  000.202  000.202: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/nerdtree.vim
065.346  000.436  000.436: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/ui.vim
065.493  000.043  000.043: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/event.vim
065.672  000.073  000.073: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/notifier.vim
066.352  000.571  000.571: sourcing /Users/iff/.vim/plugged/nerdtree/autoload/nerdtree/ui_glue.vim
070.269  000.163  000.163: sourcing /Users/iff/.vim/plugged/nerdtree/nerdtree_plugin/exec_menuitem.vim
071.205  000.863  000.863: sourcing /Users/iff/.vim/plugged/nerdtree/nerdtree_plugin/fs_menu.vim
071.343  000.063  000.063: sourcing /Users/iff/.vim/plugged/nerdtree/nerdtree_plugin/vcs.vim
071.879  013.850  007.949: sourcing /Users/iff/.vim/plugged/nerdtree/plugin/NERD_tree.vim
072.694  000.608  000.608: sourcing /Users/iff/.vim/plugged/auto-pairs/plugin/auto-pairs.vim
073.098  000.210  000.210: sourcing /Users/iff/.vim/plugged/vim-autopep8/plugin/python_autopep8.vim
079.703  006.412  006.412: sourcing /Users/iff/.vim/plugged/nerdcommenter/plugin/NERD_commenter.vim
081.288  001.347  001.347: sourcing /Users/iff/.vim/plugged/tagbar/plugin/tagbar.vim
082.077  000.176  000.176: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/init.vim
082.758  000.154  000.154: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/parts.vim
084.307  000.193  000.193: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/util.vim
084.378  002.878  002.355: sourcing /Users/iff/.vim/plugged/vim-airline/plugin/airline.vim
084.657  000.044  000.044: sourcing /Users/iff/.vim/plugged/vim-airline-themes/plugin/airline-themes.vim
088.139  003.247  003.247: sourcing /Users/iff/.vim/plugged/emmet-vim/plugin/emmet.vim
088.917  000.543  000.543: sourcing /Users/iff/.vim/plugged/FixedTaskList.vim/plugin/tasklist.vim
089.705  000.040  000.040: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/autoloclist.vim
089.827  000.035  000.035: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/balloons.vim
089.945  000.034  000.034: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/checker.vim
090.062  000.034  000.034: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/cursor.vim
090.180  000.035  000.035: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/highlighting.vim
090.296  000.034  000.034: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/loclist.vim
090.411  000.033  000.033: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/modemap.vim
090.528  000.035  000.035: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/notifiers.vim
090.646  000.037  000.037: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/registry.vim
090.765  000.037  000.037: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/signs.vim
092.845  001.634  001.634: sourcing /Users/iff/.vim/plugged/syntastic/autoload/syntastic/util.vim
107.041  000.258  000.258: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/autoloclist.vim
107.371  000.171  000.171: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/balloons.vim
107.979  000.531  000.531: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/checker.vim
108.285  000.228  000.228: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/cursor.vim
108.568  000.207  000.207: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/highlighting.vim
109.601  000.958  000.958: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/loclist.vim
109.971  000.258  000.258: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/modemap.vim
110.208  000.152  000.152: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/notifiers.vim
110.784  000.490  000.490: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/registry.vim
111.016  000.148  000.148: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/signs.vim
112.338  021.492  016.457: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic.vim
113.372  000.256  000.256: sourcing /Users/iff/.vim/plugged/vim-gitgutter/autoload/gitgutter/utility.vim
114.193  000.193  000.193: sourcing /Users/iff/.vim/plugged/vim-gitgutter/autoload/gitgutter/highlight.vim
115.311  002.719  002.270: sourcing /Users/iff/.vim/plugged/vim-gitgutter/plugin/gitgutter.vim
116.058  000.510  000.510: sourcing /Users/iff/.vim/plugged/vim-fugitive/plugin/fugitive.vim
117.445  000.998  000.998: sourcing /Users/iff/.fzf/plugin/fzf.vim
120.198  002.532  002.532: sourcing /Users/iff/.vim/plugged/fzf.vim/plugin/fzf.vim
120.985  000.545  000.545: sourcing /Users/iff/.vim/plugged/YouCompleteMe/plugin/youcompleteme.vim
121.370  000.182  000.182: sourcing /Users/iff/.vim/plugged/vim-keysound/plugin/keysound.vim
122.258  000.107  000.107: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/getscriptPlugin.vim
122.645  000.299  000.299: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/gzip.vim
123.066  000.337  000.337: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/logiPat.vim
123.219  000.064  000.064: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/manpager.vim
123.576  000.274  000.274: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/matchparen.vim
124.396  000.735  000.735: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/netrwPlugin.vim
124.583  000.079  000.079: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/rrhelper.vim
124.735  000.058  000.058: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/spellfile.vim
125.068  000.239  000.239: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/tarPlugin.vim
125.325  000.159  000.159: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/tohtml.vim
125.671  000.253  000.253: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/vimballPlugin.vim
126.053  000.278  000.278: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/zipPlugin.vim
126.463  000.095  000.095: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/pack/dist/opt/matchit/plugin/matchit.vim
126.484  008.891: loading plugins
126.668  000.184: loading packages
127.689  000.714  000.714: sourcing /Users/iff/.vim/plugged/indentLine/after/plugin/indentLine.vim
127.757  000.375: loading after plugins
127.771  000.014: inits 3
135.373  007.602: reading viminfo
135.475  000.102: setting raw mode
135.498  000.023: start termcap
135.544  000.046: clearing screen
137.265  000.687  000.687: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions.vim
137.703  000.122  000.122: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/quickfix.vim
138.212  000.319  000.319: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline.vim
138.619  000.087  000.087: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/netrw.vim
138.940  000.087  000.087: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/term.vim
139.397  000.152  000.152: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/hunks.vim
139.774  000.124  000.124: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tagbar.vim
140.449  000.386  000.386: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/branch.vim
140.882  000.113  000.113: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/fugitiveline.vim
141.271  000.105  000.105: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/syntastic.vim
141.794  000.234  000.234: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/whitespace.vim
142.383  000.135  000.135: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/po.vim
142.806  000.189  000.189: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/wordcount.vim
143.337  000.285  000.285: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tabline.vim
143.703  000.116  000.116: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tabline/autoshow.vim
144.209  000.182  000.182: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tabline/tabs.vim
144.931  000.315  000.315: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tabline/buffers.vim
145.434  000.075  000.075: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/keymap.vim
149.859  000.151  000.151: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/section.vim
150.578  000.412  000.412: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/highlighter.vim
155.510  000.158  000.158: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/themes.vim
155.638  001.308  001.150: sourcing /Users/iff/.vim/plugged/vim-monokai-tasty/autoload/airline/themes/monokai_tasty.vim
162.969  000.652  000.652: sourcing /Users/iff/.vim/plugged/vim-monokai-tasty/autoload/airline/themes/monokai_tasty.vim
195.304  000.323  000.323: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/builder.vim
196.004  000.181  000.181: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/default.vim
226.797  000.345  000.345: sourcing /Users/iff/.vim/plugged/syntastic/autoload/syntastic/log.vim
227.528  084.899: opening buffers
229.983  000.215  000.215: sourcing /Users/iff/.vim/plugged/vim-gitgutter/autoload/gitgutter.vim
230.263  002.520: BufEnter autocommands
230.266  000.003: editing files in windows
239.094  007.202  007.202: sourcing /Users/iff/.vim/plugged/vim-fugitive/autoload/fugitive.vim
241.736  001.140  001.140: sourcing /Users/iff/.vim/plugged/YouCompleteMe/autoload/youcompleteme.vim
389.182  150.574: VimEnter autocommands
389.208  000.026: before starting main loop
390.913  000.368  000.368: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tabline/ctrlspace.vim
391.781  000.325  000.325: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tabline/builder.vim
392.298  000.155  000.155: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tabline/buflist.vim
396.839  000.144  000.144: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tabline/formatters/default.vim
409.609  006.266  006.266: sourcing /Users/iff/.vim/plugged/tagbar/autoload/tagbar.vim
410.066  000.147  000.147: sourcing /Users/iff/.vim/plugged/tagbar/autoload/tagbar/debug.vim
454.385  001.143  001.143: sourcing /Users/iff/.vim/plugged/tagbar/autoload/tagbar/types/ctags.vim
454.835  000.144  000.144: sourcing /Users/iff/.vim/plugged/tagbar/autoload/tagbar/prototypes/typeinfo.vim
467.663  000.480  000.480: sourcing /Users/iff/.vim/plugged/vim-gitgutter/autoload/gitgutter/hunk.vim
468.686  070.306: first screen update
468.688  000.002: --- VIM STARTED ---
