# 直方图
# from matplotlib import pyplot as plt
# years = [1, 2, 3, 4, 5, 6]
# gdp = [20, 30, 5, 50, 60, 70]
# plt.plot(years, gdp)
# plt.title("gdp")
# plt.ylabel("gdp")
# plt.xlabel("years")
# plt.show()

# 条形图
# from matplotlib import  pyplot as plt
# movies = ["an", "b", "c", "d", "e"]
# num_oscars =  [5, 11, 3, 8,10]
# xs = [i + 1 for i, _ in enumerate(movies)]
# plt.bar(xs, num_oscars)
# plt.ylabel("numbers")
# plt.title("my fav")
# plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
# plt.show()

# #条形图分布（未正常运行）
# from  matplotlib import pyplot as plt
# grades = [83, 95, 87, 70, 0, 85, 82, 100, 67,73, 0]
# decile = lambda grade: grade // 10*10
# histogram = Counter(decile(grade) for grade in grades)
# plt.bar([x -4 for x in histogram.keys()],
# 		histogram.values(),
# 		8)
#
# plt.axis([-5, 105, 0, 5])
# plt.xticks([10 *i for i in range(11)])
# plt.xlabel("seems")
# plt.ylabel("students")
# plt.title("scores")
# plt.show()

#画 y = sin x图像
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 5, 0.1);
y = np.sin(x)
plt.plot(x, y)
plt.show()

#配置属性 我们可以为每个对象配置它们的属性，应该说有三个方法，一个是通过对象的方法set_属性名（）函数，二是通过对象的set()函数，三是通过pylot模块提供的setp()函数：
# plt.figure()
# line = plt.plot(range(5))[0]
# line.set_color('r')
# line.set_linewidth(2.0)
# plt.show()
#-----------------------
# plt.figure()
# line = plt.plot(range(5))[0]
# line.set(col)
# plt.show()
# #------------------------
# plt.figure()
# lines = plt.plot(range(5),range(5),range(5)，range(8,13))    # plot函数返回一个列表;
# plt.setp(lines, color = 'g',linewidth = 2.0)                # setp函数可以对多条线进行设置的;
# plt.show()


#artist
# import matplotlib.pyplot as plt
# import numpy as np
# fig = plt.figure(1)
# ax = fig.add_axes([0.1, 0.5, 0.8, 0.5])
# ax.set_xlabel('time')
# line = ax.plot(range(5))[0]
# line.set_color('r')
# plt.show()

#figure容器
# axes：Axes对象列表；
# patch：作为背景的Rectangle对象；
# images：FigureImage对象列表，用于显示图像；
# legends：Legend 对象列表，用于显示图示；
# lines：Line2D对象列表；
# patches：Patch对象列表；
# texts：Text 对象列表，用于显示文字；

#使用figure 对象绘制直线
# from matplotlib.lines import Line2D
# import matplotlib.pyplot as plt
# fig = plt.figure()
# line1 = Line2D([0,1], [0,1], transform = fig.transFigure, figure=fig, color="r")
# line2 = Line2D([0,1],[1,0], transform=fig.transFigure, figure=fig, color="b")
# fig.lines.extend([line1, line2])
# fig.show()

#使用axis容器
# from matplotlib.lines import Line2D
# import matplotlib.pyplot as plt
#
# plt.plot([1, 2, 3,], [4, 5, 6])
# axis = plt.gca().xaxis
# axis.get_ticklocs()   #得到刻度位置
# axis.get_ticklabels() #得到刻度标签
# axis.get_ticklines()   #得到刻度线
# axis.get_ticklines(minor=True)   #得到次刻度线
# for label in axis.get_ticklabels():
# 	label.set_color('red')  #设置每个刻度标签的颜色
# 	label.set_rotation(45)    #旋转45度
# 	label.set_fontsize(16)    #设置字体大小
#
# for line in axis.get_ticklines():
# 	line.set_color('green')   #设置颜色
# 	line.set_markersize(15)   #设置刻度线的长短
# #	line.set_markeredgwidth(3)    #设置线的粗细  AttributeError: 'Line2D' object has no attribute 'set_markeredgwidth'
#
# plt.show()

#常用函数
#plot
# plot(x, y)             # 画出横轴为x与纵轴为y的图，使用默认的线形与颜色；
# plot(x, y, 'bo')    # 用蓝色，且点的标记用小圆，下面会解释哦
# plot(y)             # 纵轴用y ,横轴用y的每个元素的坐标，即0，1，2……
# plot(y, 'r+')       # 如果其中x或y 为2D的，则会用它的相应的每列来表示哦，是每列哦，是每列哦，是每列哦，（重要的事情说三遍）
# plot(x1, y1, 'g^', x2, y2, 'g-') # 看到了吗，我们可以使用多对的x, y, format 对当作变量的哦，把它们画一个图里；

#线的形状：
# ‘-’ solid line style
# ‘–’ dashed line style
# ‘-.’ dash-dot line style
# ‘:’ dotted line style

#点的标记：
# ‘.’ point marker
# ‘,’ pixel marker
# ‘o’ circle marker
# ‘v’ triangle_down marker
# ‘^’ triangle_up marker
# ‘<’ triangle_left marker
# ‘>’ triangle_right marker
# ‘1’ tri_down marker
# ‘2’ tri_up marker
# ‘3’ tri_left marker
# ‘4’ tri_right marker
# ‘s’ square marker
# ‘p’ pentagon marker
# ‘*’ star marker
# ‘h’ hexagon1 marker
# ‘H’ hexagon2 marker
# ‘+’ plus marker
# ‘x’ x marker
# ‘D’ diamond marker
# ‘d’ thin_diamond marker
# ‘|’ vline marker
# ‘_’ hline marker

#线的颜色
# ‘b’ blue
# ‘g’ green
# ‘r’ red
# ‘c’ cyan
# ‘m’ magenta
# ‘y’ yellow
# ‘k’ black
# ‘w’ white

# import matplotlib.pyplot as plt
# import numpy as np
# plt.figure(1)
# t = np.arange(0.0, 2.0, 0.1)
# s = np.sin(2*np.pi*t)
# plt.plot(t, s, 'r--o', label ='sinx')
# plt.legend()
# plt.xlabel('time(s)')
# plt.ylabel('voltage(mV)')
# plt.title('About as simple as it gets, folks')
# plt.grid(True)
# plt.show()

#subplot
#填充彩色子图
# import matplotlib.pyplot as plt
# import numpy as np
#
# for i, color in enumerate('rgbyck'):
#     plt.subplot(321+i, axis_bgcolor = color)
# plt.show()
#程序未正常运行

#利用subplot_adjust()函数对画多个子图进行调整，优化间隔，
#一共有：left、right，bottom，top，wspace，hspase留个参数，
#取值从0至1.

# import  numpy as np
# import matplotlib.pyplot as plt
# x1 = np.linspace(0.0, 5.0) #生成一个以为的array，linspace（起始点、结束点，点数（默认50））
# x2 = np.linspace(0.2, 2.0)
# y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
# y2 = np.cos(2 * np.pi * x2)
#
# plt.subplot(2, 2, 1)  #表示在subplot 为2*1的样式，病在第一个子图集上画出
# plt.plot(x1, y1, 'yo-')
# plt.title('A tale of 2 subplots')
# plt.ylabel('Damped oscillation')
#
# plt.subplot(2, 2, 2)  #表示在第二个子图集上画个空图
# plt.title('It is a empty figure')
#
# plt.subplot(2, 2, 4)
# plt.plot(x2, y2, 'r.-')
# plt.xlabel('time(s)')
# plt.ylabel('Undamped')
# plt.show()


# import matplotlib.pyplot as plt
# labels = 'frogs', 'hogs', 'dogs', 'logs'
# sizes = [15, 30, 45, 10]
# colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
# explode = (0, 0.1, 0, 0)
# plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
# plt.axis('equal')
# plt.show()

